from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer, ProductSerializer, CommentSerializer, ReviewtSerializer
from .models import Profile, Product_Model, CommentModel, ReviewModel, Order


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_product(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.add_product_model'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    # request.data.update(user=request.user.id) # the same thing
    request.data["user"] = request.user.id  # the same as above
    new_product = ProductSerializer(data=request.data)
    if new_product.is_valid():
        new_product.save()
        return Response({"Product": new_product.data})
    else:
        print(new_product.errors)
    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_product(request: Request):
    Product = Product_Model.objects.all()

    dataResponse = {
        "msg": "List of All Products",
        "Products": ProductSerializer(instance=Product, many=True).data
    }
    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_product(request: Request, product_id):
    ""
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.change_product_model'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    product = Product_Model.objects.get(id=product_id)
    updated_product = ProductSerializer(instance=product, data=request.data)
    if updated_product.is_valid():
        updated_product.save()
        responseData = {
            "msg": "updated successefully"
        }

        return Response(responseData)
    else:
        print(updated_product.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_product(request: Request, product_id):
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.delete_product_model'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    product = Product_Model.objects.get(id=product_id)
    product.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def add_comment(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    print(request.user.is_staff)
    new_Comment = CommentSerializer(data=request.data)
    if new_Comment.is_valid():
        new_Comment.save()
        dataResponse = {
            "msg": "Created Successfully",
            "product": new_Comment.data
        }
        return Response(dataResponse)
    else:
        print(new_Comment.errors)
        dataResponse = {"msg": "couldn't create a comment"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_comment(request: Request, comment_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    comment = CommentModel.objects.get(id=comment_id)
    comment.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_comment(request: Request):
    comment = CommentModel.objects.all()
    dataResponse = {
        "msg": "List of All comment",
        "comment": CommentSerializer(instance=comment, many=True).data
    }
    return Response(dataResponse)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def list_profile(request: Request):
    profile = Profile.objects.all()
    dataResponse = {
        "msg": "List of All profile",
        "Profile": ProfileSerializer(instance=profile, many=True).data
    }
    return Response(dataResponse)


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_profile(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.add_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    request.data["user"] = request.user.id
    new_profile = ProfileSerializer(data=request.data)
    if new_profile.is_valid():
        new_profile.save()
        return Response({"Profile": new_profile.data})
    else:
        print(new_profile.errors)
    return Response("no", status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request: Request, profile_id):
    '''

    '''
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.delete_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    profile = Profile.objects.get(id=profile_id)
    profile.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_profile(request: Request, profile_id):
    if not request.user.is_authenticated or not request.user.has_perm('MatajerApp.change_profile'):
        return Response("Not Allowed", status=status.HTTP_400_BAD_REQUEST)
    profile = Profile.objects.get(id=profile_id)
    updated_profile = ProductSerializer(instance=profile, data=request.data)
    if updated_profile.is_valid():
        updated_profile.save()
        responseData = {
            "msg": "updated successefully"
        }
        return Response(responseData)
    else:
        print(updated_profile.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)