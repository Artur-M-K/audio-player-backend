from django.conf.urls import url
from .views import first

urlpatterns = [
    url('first', first)
]