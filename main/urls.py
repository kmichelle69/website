from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^contactus', views.ContactView.as_view()),

]
