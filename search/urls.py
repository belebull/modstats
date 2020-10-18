from django.conf.urls import url
from search import views

urlpatterns = [
    url('', views.index, name='search_idx')
]
