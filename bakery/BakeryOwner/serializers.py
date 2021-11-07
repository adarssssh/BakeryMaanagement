from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Products,Ingredients

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'user_type')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # self.validated_data = validated_data
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        # user_type=validated_data['user_type'],
                                        validated_data['password'],
                                        )

        return user


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ('id','ingredient', 'quantity')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_name', 'i1', 'i2', 'i3', 'i4', 'i5', 'cost', 'Selling_price')
