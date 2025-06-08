from rest_framework import viewsets
from .models import User, Property, Image, Favorite, Inquiry
from .serializers import UserSerializer, PropertySerializer, ImageSerializer, FavoriteSerializer, InquirySerializer
from .permissions import IsAgentOrAdmin, IsBuyerOrAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # You can set permissions if needed
    # permission_classes = [IsAuthenticatedOrReadOnly]


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAgentOrAdmin]

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsBuyerOrAdmin, IsAuthenticatedOrReadOnly]

class InquiryViewSet(viewsets.ModelViewSet):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsBuyerOrAdmin, IsAuthenticatedOrReadOnly]


# (UserViewSet and ImageViewSet can use IsAuthenticatedOrReadOnly or as needed)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Optionally, set permission_classes

