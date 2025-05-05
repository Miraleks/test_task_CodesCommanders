from rest_framework import serializers
from .models import User, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def validate_user(self, value):
        if not User.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("User with this ID does not exist.")
        return value