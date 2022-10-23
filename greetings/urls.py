from django.urls import path
from django.views.generic import TemplateView
from greetings.views import welcome

urlpatterns = [
    path('', welcome, name="welcome"),
    path('about/', TemplateView.as_view(template_name="greetings/about.html")),
    path('contact/', TemplateView.as_view(template_name="greetings/contact.html")),
]