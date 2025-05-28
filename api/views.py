
from rest_framework import viewsets, status,permissions,parsers,serializers,generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from cart.models import CartItem,Product
from api.serializers import CartItemSerializer,LoginSerializer, ProductSerializer,RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class LoginAPIView(generics.CreateAPIView):
    permission_classes = []  
    serializer_class = LoginSerializer  

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return CartItem.objects.none()
        return CartItem.objects.filter(user=user)

    @transaction.atomic
    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data.get('total_quantity', 0)

        if product.quantity < quantity:
            raise serializers.ValidationError("Not enough product in stock.")

        existing_item = CartItem.objects.filter(user=self.request.user, product=product).first()

        if existing_item:

            if product.quantity < (existing_item.total_quantity + quantity):
                raise serializers.ValidationError("Not enough product in stock to update cart item.")

            existing_item.total_quantity += quantity
            existing_item.total_price = existing_item.total_quantity * product.price
            product.quantity -= quantity
            product.save()
            existing_item.save()
        else:
            
            total_price = product.price * quantity
            serializer.save(user=self.request.user, total_quantity=quantity, total_price=total_price)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        total_price = sum(item.total_price for item in queryset)
        total_quantity = sum(item.total_quantity for item in queryset)
        
        return Response({
            "items": serializer.data,
            "total_price": total_price,
            "total_quantity": total_quantity
        })
    @action(detail=False, methods=['delete'], url_path='clear')
    def clear_cart(self, request):
        """Clear all cart items for the current user."""
        self.get_queryset().delete()
        return Response({"message": "Cart cleared successfully."}, status=status.HTTP_204_NO_CONTENT)

