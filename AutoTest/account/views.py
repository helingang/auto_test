from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
# from .forms import LoginForm
from .models import User
from django.http import HttpResponse, JsonResponse
import json
from django.views import View

from django.views.decorators.csrf import csrf_exempt, csrf_protect
# csrf_exempt : 不验证csrf
# csrf_protect : 验证csrf
from django.utils.decorators import method_decorator


@method_decorator([csrf_exempt], name='dispatch')  # 此视图不验证csrf
class LoginView(View):
    def post(self, request, *args, **kwargs):
        username = json.loads(request.body).get('username', None)
        password = json.loads(request.body).get('password', None)

        user = User.objects.filter(username=username, password=password).values()
        if len(user) == 1:
            print(user)
            return JsonResponse({
                'msg': '登录成功',
                'code': 1,
                'data': {
                    'userid': user[0]['id'],
                    'token': '12345',
                    'username': user[0]['username']
                }
            })
        else:
            return JsonResponse({
                'msg': '登录失败',
                'code': 0,
                'data': {}
            })

@method_decorator([csrf_exempt], name='dispatch')  # 此视图不验证csrf
class registerView(View):
    def post(self, request, *args, **kwargs):
        username = json.loads(request.body).get('username', None)
        password = json.loads(request.body).get('password', None)
        print(username)
        print(password)
        insert_res = User.objects.create(username=username, password=password).save()
        print(insert_res)

        return JsonResponse({
            'msg': '注册成功',
            'code': 1
        })