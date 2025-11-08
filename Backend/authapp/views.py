import os
import json
import requests
from pprint import pprint
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import cloudinary
import cloudinary.uploader
from rest_framework.decorators import api_view
from rest_framework.response import Response






#@api_view(['POST'])
#def log_in(request):
    # You can later replace this with actual authentication logic
#    return Response({"message": "Login endpoint is working ✅"})


# ............................................................... CLOUDINARY ......................................
secure = os.getenv('SECURE')          
cloudinary.config( 
    cloud_name=os.getenv('cloud_name'),      
    api_key = os.getenv('api_key'),           
    api_secret = os.getenv('api_secret'),          
    secure=True
)
# ............................................................... CLOUDINARY ......................................




# ....................................................................... sign_in ............................................ 
@api_view(['POST'])
def sign_in(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        #print(username)
        if not username or not password or not email:
            return Response({"error": "Username, password, and email are required"}, status=HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        print('Save on Database...')

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        #print(access_token)
        #print(refresh_token)
        

        response = Response({
            "message": "User registered successfully",
            "access": access_token,
            "refresh": refresh_token,
        }, status=HTTP_201_CREATED)

        

        secure = False  
        response.set_cookie('access', access_token, httponly=True, secure=secure, samesite='Lax')
        response.set_cookie('refresh', refresh_token, httponly=True, secure=secure, samesite='Lax')

        return response

    except Exception as e:
        return Response({"error": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
# ....................................................................... sign_in ............................................  

# ....................................................................... current user ...............................................
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email, 
    })
# ....................................................................... current user ...............................................

# ....................................................................... Login ..........................................................


@api_view(['POST'])
def login_user(request):
    phone = request.data.get('phone_number')
    password = request.data.get('password')

    ADMINS = [
        {"name": "NANTU DAS ADHIKARI", "phone": "9547783824", "password": "Nantu@4655"},
        {"name": "ARPAN PATRA", "phone": "9876543210", "password": "Arpan@123"},
        {"name": "RAHUL SINGH", "phone": "9123456789", "password": "Rahul@987"},
        {"name": "SOMA ROY", "phone": "9000000000", "password": "Soma@999"},
    ]

    if not phone or not password:
        return Response({'error': 'Phone number and password required'}, status=status.HTTP_400_BAD_REQUEST)


    matched_admin = next((admin for admin in ADMINS if admin["phone"] == phone and admin["password"] == password), None)

    if matched_admin:
        return Response({
            'message': 'Login successful',
            'redirect': '/AdminDashboard',
            'admin_name': matched_admin["name"]
        }, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid phone number or password'}, status=status.HTTP_401_UNAUTHORIZED)
# ....................................................................... Login ..........................................................

# ....................................................................... logout ..........................................................
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"message": "Logout successful"}, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)
# ....................................................................... logout ..........................................................

