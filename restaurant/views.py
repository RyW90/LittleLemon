from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializer import BookingSerializer
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('title', 'price', 'inventory')


class MenuItemView(ListCreateAPIView):

    def get_queryset(self):
        return Menu.objects.all()

    def get_serializer_class(self):
        return MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView, DestroyAPIView):

    def get_queryset(self):
        return Menu.objects.all()

    def get_serializer_class(self):
        return MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



