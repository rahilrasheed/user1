from django.urls import path
from . import views
urlpatterns = [
   path('user',views.fnuser),
   path('user1',views.fnuser1),
   path('home',views.fnhome),
   path('prod',views.fnprod),
   path('Fboot',views.fnFboot),
   path('Lboot',views.fnLboot),
   path('NTboot2',views.fnNTboot2),
   path('new',views.fnnew),
   path('modjum',views.fnmod),
   path('gridb',views.fngridb),
   path('wb',views.fnwb),
   path('java1',views.fnjava1),
   path('promcon',views.fnpromcon),
   path('arith',views.fnarith),
   path('grade',views.fngrade),
   path('switch1',views.fnswitch1),
   path('fibinocci',views.fnfibi),
   path('ques',views.fnques),
   path('while',views.fnwhile),
   path('hw',views.fnhw),
   path('cyber',views.fncyber)
]
