from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User
from .serializers import (
    UserSerializer, RegisterSerializer,
    JobSeekerRegistrationSerializer, CompanyRegistrationSerializer,
    LoginSerializer
)

class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=JobSeekerRegistrationSerializer,
        responses={
            201: openapi.Response(
                description="Successful registration",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Bad Request"
        }
    )
    @action(detail=False, methods=['post'])
    def jobseeker_register(self, request):
        serializer = JobSeekerRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_type'] = 'jobseeker'
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Registration successful!',
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=CompanyRegistrationSerializer,
        responses={
            201: openapi.Response(
                description="Successful registration",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            400: "Bad Request"
        }
    )
    @action(detail=False, methods=['post'])
    def employer_register(self, request):
        serializer = CompanyRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user_type'] = 'employer'
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Registration successful!',
                'user': UserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description="Successful login",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING),
                        'user': openapi.Schema(type=openapi.TYPE_OBJECT),
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                    }
                )
            ),
            401: "Unauthorized",
        }
    )
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                role = "Job Seeker" if user.user_type == 'jobseeker' else "Employer"
                return Response({
                    'message': f'Welcome back! You are logged in as {role}.',
                    'user': UserSerializer(user).data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]



