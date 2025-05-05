from rest_framework import serializers
from .models import User, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def validate_user(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("A user with such ID does not exist.")
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user')
        user = User.objects.get(id=user_id)
        return Order.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        if 'user' in validated_data:
            user_id = validated_data.pop('user')
            if not User.objects.filter(id=user_id).exists():
                raise serializers.ValidationError("Пользователь с таким ID не существует.")
            instance.user = User.objects.get(id=user_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance