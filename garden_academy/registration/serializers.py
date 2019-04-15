from rest_framework import serializers
from .models import Register
from rest_framework.validators import UniqueTogetherValidator


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = '__all__'

    def create(self, validated_data):
        return Register.objects.create(**validated_data)



# class EmailSerializer(serializers.Serializer):

#     # fullname = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)

#     def validate_email(self, value):
#         try:
#             register = Register.objects.get(email=value)
#         except:
#             return value
#         raise serializers.ValidationError({'status': 'Failure',
#                             'message': 'Not Approved',
#                             'body': 'Email address already registered'})
    
#     def create(self, validated_data):
#         return Register.objects.create(**validated_data)
