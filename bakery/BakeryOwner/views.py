from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from .models import Products, Ingredients
from .serializers import ProductSerializer, IngredientSerializer
from django.views.decorators.csrf import csrf_exempt
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
# Create your views here.
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'product_list': '/product-list',
        'detailview': '/product-detail/<int:id>',
        'create': '/product-create/',
        'update': '/product-update/<int:id>',
        'delete': '/product-delete/<int:id>',
        'ingredient_list': '/ingredient-list',
        'AddIngredient': '/ingredient-create/',
        'deleteIngredient': '/ingredient-delete/<int:id>',
    }

    return Response(api_urls)

@api_view(['GET'])
def showall(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products,many=True)
    return JsonResponse(serializer.data)

@api_view(['GET'])
def viewproduct(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return JsonResponse(serializer.data)

@api_view(['POST'])
def createproduct(request):
    data = JSONParser().parse(request)
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data)

@api_view(['POST'])
def updateproduct(request,pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def deleteproduct(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()

    return Response('Item deleted Successfully')

#@api_view(['POST'])
@csrf_exempt
def addingredient(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)

@api_view(['GET'])
def showingredient(request):
    ingredients = Ingredients.objects.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def deleteingredient(request, pk):
    ingredient = Ingredients.objects.get(id=pk)
    ingredient.delete()

    return Response('Item deleted Successfully')