from django.urls import path
from.import views
urlpatterns=[
    path('',views.index),
    path('parliament/',views.parliamentInfo),
    path('politics/',views.politicsInfo),
    path('sports/',views.sportsInfo),
]