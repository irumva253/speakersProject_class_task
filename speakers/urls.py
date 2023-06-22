from django.urls import path, re_path
from speakers import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('create/',views.Register,name='Register'),
    path('<int:id>/',views.Specific,name='Ident'),
    path('<int:id>/update/',views.Update,name='Update'),
    path('<int:id>/delete/',views.Delete,name='Delete'),



]