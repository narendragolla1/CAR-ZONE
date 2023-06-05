
from django.urls import path
from . import views
urlpatterns = [
        path('',views.cars,name="cars"),
        path('detail/',views.car_detail,name="car-detail"),
]
