from .views import list, note_detail,add,update,delete
from django.urls import path

urlpatterns = [
    path('list/',list),
    path('<int:pk>/',note_detail),
    path('add/',add),
    path('update/<int:pk>/',update),
    path('delete/<int:pk>/',delete)
]