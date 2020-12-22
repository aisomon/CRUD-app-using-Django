from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('read/', views.viewData, name = "read"),
    path('read/edit/<int:id>/', views.editData, name = "edit"),
    path('read/delate/<int:id>/', views.delateData, name = "delate"),
    path('register/',views.registration, name="register"),
    # path('login/',views.login,name="login"),

]
