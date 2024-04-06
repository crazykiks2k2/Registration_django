from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.say_hello),
    path('aboutus',views.say_hi),
    path('page',views.print_txt),
]
