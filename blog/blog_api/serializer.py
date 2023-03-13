from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User



class BlogSerializer(serializers.ModelSerializer):
    time_posted = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = ("id","title", "content","author", "time_posted", "category")

    def get_time_posted(self, obj):
        return obj.time_posted.strftime('%Y-%m-%d %H:%M:%S')
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password", "email")
    def create(self, validated_data):
        email = validated_data.pop("email", None)
        instance = self.Meta.model(**validated_data)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Invalid Email...! Try Another")
        instance.save()
        return instance

