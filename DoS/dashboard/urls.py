from django.urls import path, include
from .views import pickup,bulk_dashboard,dos_pickup,dos_dashboard


urlpatterns = [
    path('', bulk_dashboard,name='bulk_dashboard'),
    path('pickup', pickup,name ="pickup"),
    path('dos_dashboard', dos_dashboard,name ="dos_dashboard"),
    path('dos_pickup/<int:id>', dos_pickup,name ="dos_pickup"),

]