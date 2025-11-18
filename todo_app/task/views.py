from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Todo

# Single-page view: list + create
class TodoListView(View):
    template_name = 'todo_list.html'

    def get(self, request):
        tasks = Todo.objects.all().order_by('-created_at')
        return render(request, self.template_name, {'tasks': tasks})

    def post(self, request):
        # Handle new task creation
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        Todo.objects.create(
            title=title,
            description=description,
            due_date=due_date
        )
        return redirect('todo_list')


# Update task view
class TodoUpdateView(View):
    template_name = 'todo_update.html'

    def get(self, request, id):
        task = get_object_or_404(Todo, id=id)
        return render(request, self.template_name, {'task': task})

    def post(self, request, id):
        task = get_object_or_404(Todo, id=id)
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('todo_list')


# Mark task as complete
class TodoCompleteView(View):
    def get(self, request, id):
        task = get_object_or_404(Todo, id=id)
        task.is_completed = True
        task.save()
        return redirect('todo_list')


# Delete task
class TodoDeleteView(View):
    def get(self, request, id):
        task = get_object_or_404(Todo, id=id)
        task.delete()
        return redirect('todo_list')
