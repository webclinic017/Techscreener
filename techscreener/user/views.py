from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = redirect('/login?message=Registered')
        return response

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')

        payload = {
            'id': user.id,
            'name': user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=600),
            'iat': datetime.datetime.utcnow()
         }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response(template_name='index.html')

        response.set_cookie(key='auth_token', value=token, httponly=True)

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('auth_token')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.payload(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def get(self, request):
        response = Response(template_name='index.html')
        response.delete_cookie('auth_token')
        return response
