from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Product_Model,CommentModel,ReviewModel,Order



class UserSerializerView(serializers.ModelSerializer):

    class Meta:
       model = User
       fields = ['username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializerView()
    class Meta:
        model = Profile
        fields = '__all__'
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Model
        fields = '__all__'





class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = CommentModel
        fields = '__all__'
        depth = 1

class ReviewtSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewModel
        fields = '__all__'


class orderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'