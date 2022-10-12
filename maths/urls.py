# maths/urls.py
from django.urls import path
from maths.views import math, add, sub, mul, div

app_name = "maths"
urlpatterns = [
    path('', math),
    path('add/<a>/<b>', add),
    path('sub/<a>/<b>', sub),
    path('mul/<a>/<b>', mul),
    path('div/<a>/<b>', div),
]