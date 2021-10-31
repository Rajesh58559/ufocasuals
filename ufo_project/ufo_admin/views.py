from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ufo_admin.models import Category, Product
from ufo_admin.serializers import CategorySerializer, ProductSerializer


# Create your views here.

@csrf_exempt
def categoryApi(request, id=0):
    if request.method == 'GET':
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("added successfully", safe=False)
        return JsonResponse("failed to add.", safe=False)
    elif request.method == 'PUT':
        category_data = JSONParser.parse(request)
        category = Category.objects.object.get(CategoryId=category_data['CategoryId'])
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("updated succesfully", safe=False)
        return JsonResponse("failed to update", safe=False)
    elif request.method == 'DELETE':
        category = Category.objects.get(CategoryID=id)
        category.delete()
        return JsonResponse("delelted succesfully", safe=False)
