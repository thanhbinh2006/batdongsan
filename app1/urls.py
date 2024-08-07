from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_app1),
    path('1/',views.get_app1_1),
]
