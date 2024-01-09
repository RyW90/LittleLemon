from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index, name="index"),
    path('', views.index, name="home"),
    path('api/bookings/', views.BookingViewSet.as_view({'get': 'list'}), name="bookings"),
    path('api/menu/', views.MenuItemView.as_view(), name="menu"),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)

    ]