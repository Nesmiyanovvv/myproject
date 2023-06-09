from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer, UserSerializerDetail
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import UserForm
from .models import Core


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class IndexView(APIView):
    @staticmethod
    def get(request):
        user = User.objects.filter(id=request.user.id)
        if len(user) != 0:
            core = Core.object.get(user=request.user)
            return render(request, 'index.html')
        else:
            return redirect('login')


class UserLoginView(APIView):
    @staticmethod
    def post(request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'invalid': True})

    @staticmethod
    def get(request):
        return render(request, 'login.html', {'invalid': False})


class UserLogoutView(APIView):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('login')


class UserRegistrationView(APIView):
    @staticmethod
    def post(request):
        form = UserForm(request.data)
        if form.is_valid():
            username = form.cleaned_data['username']
            existing_user = User.objects.filter(username=username)
            if len(existing_user) == 0:
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, '', password)
                user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                core = Core(user=user)
                core.save()
                return redirect('index')
            else:
                return render(request, 'registration.html', {'invalid': True, 'form': form})

    @staticmethod
    def get(request):
        form = UserForm()
        return render(request, 'registration.html', {'invalid': False, 'form': form})
