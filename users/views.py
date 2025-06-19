from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from telegrambot.tasks import send_welcome_email
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET'])
def hello_view(request):
    return Response({"message": "Hello from the Django server!"})
@api_view(['POST'])
def signup_view(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    if not username or not email or not password:
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create(
        username=username,
        email=email,
        password=make_password(password)  # Hash the password!
    )
    send_welcome_email.delay(email)
    return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if user is not None:
        return Response({"message": "Login successful!"})
    else:
        return Response({"error": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello, {request.user.username}! This is a protected API."})
