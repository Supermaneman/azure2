from django.urls import path
from . import views

app_name='project_app'

urlpatterns = [
    path('',views.landing, name="landing"),
    path('rooms',views.rooms, name="rooms"),
    path('aboutus',views.aboutus, name="aboutus"),
    path('contact',views.contact, name="contact"),
    path('reserve',views.reserve, name="reserve"),
]



# def landing(request):
#     return render(request, "user/landing.html")
