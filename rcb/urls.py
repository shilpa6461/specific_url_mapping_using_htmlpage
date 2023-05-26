from django.urls import path
from rcb.views import *
app_name='pushpa'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]