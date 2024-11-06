from rest_framework import viewsets
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
)
from django.contrib.auth.models import User
from store.models import Category, Product, Order, OrderItem
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    OrderSerializer,
    OrderItemSerializer,
    UserSerializer,
    TokenSerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class BaseViewSet(viewsets.ModelViewSet):
    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ["post"]


class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer
