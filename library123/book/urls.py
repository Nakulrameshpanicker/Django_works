from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('', views.Add_book.as_view(), name="home"),
    path('addbooks/', views.Add_book.as_view(), name="addbooks"),
    path('viewbooks/', views.ViewBooks.as_view(), name="viewbooks"),
    path('detail/<int:i>', views.Detail.as_view(), name='detail'),
    path('delete/<int:i>', views.Del.as_view(), name='delete'),
path('edit/<int:i>', views.Edit_book.as_view(), name="edit"),

]
