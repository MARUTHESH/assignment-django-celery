from django.urls import path, include
from .import views
from rest_framework import routers

app_name = 'apiapp'

router = routers.DefaultRouter()
router.register('urls', views.UrlsView)
router.register('dataset', views.DataSetView)

urlpatterns = [
    path('', include(router.urls))
]
