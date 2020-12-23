from django.urls import path, include
from .views import login,register,logout_view

urlpatterns = [
    path('', login,name='login'),
    path('logout', logout_view,name='logout'),
    path('signup/<str:user_type>', register,name ="signup"),

]