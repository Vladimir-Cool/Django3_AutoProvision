from django.contrib import admin
from .models import AudiocodesMP112, TypeAudiocodesMP112, MainGateway, TypeGateway, LoginPasswordGW



admin.site.register(MainGateway)
admin.site.register(TypeGateway)
admin.site.register(LoginPasswordGW)