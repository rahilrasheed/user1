from django.urls import path
from . import views
urlpatterns = [
   path('user',views.fnuser),
   path('user1',views.fnuser1),
   path('home',views.fnhome)
]
