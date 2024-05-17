from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuItemSerializer, BookingSerializer
from .models import MenuItem, Booking
from django.contrib.auth.models import User
from rest_framework import permissions
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer
from .models import MenuItem, Booking
# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]