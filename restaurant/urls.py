from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('home', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('menu/<int:pk>/', views.display_menu_item, name="menu_item"),
    # Add the remaining URL path configurations here
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)