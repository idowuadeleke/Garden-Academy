from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Register
# from .serializers import EmailSerializer, RegisterSerializer
from .serializers import RegisterSerializer
from rest_framework.renderers import JSONRenderer


class RegisterList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        registered_user = Register.objects.all()
        serializer = RegisterSerializer(registered_user, many=True)
        return Response(serializer.data)

    def post(self, request):
        user_data = request.data.get('registration_data')

        # Create an article from the above data
        serializer = RegisterSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            registration_saved = serializer.save()
            return Response({'status': 'successful',
                            'message': 'approved',
                            'body': 'Registration Successful'})


# class CheckEmail(APIView):
#     permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         user_data = request.data

#         # Create an article from the above data
#         serializer = EmailSerializer(data=user_data)
#         if serializer.is_valid(raise_exception=True):
#             registration_saved = serializer.save()
#             return Response({"email": {
#                                         'status': 'successful',
#                                         'message': 'Email is available',
#                                         'body': 'User can use this email'}})