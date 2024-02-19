
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from ai_tool.controller.home import HomeController
from django.conf import settings
from django.conf.urls.static import static
router = SimpleRouter()
 
api_routes = [
    path('home', HomeController.as_view({'post': 'home'}), name="home")
    #  path(r'^$', HomeController.as_view({'get': 'home'}), name="home"),
]
 
urlpatterns = api_routes
urlpatterns = format_suffix_patterns(urlpatterns)