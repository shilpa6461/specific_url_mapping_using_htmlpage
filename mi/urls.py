from django.urls import path
from mi.views import *
app_name='srivalli'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]