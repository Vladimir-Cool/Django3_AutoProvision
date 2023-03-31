from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.urls import reverse
from django.core.paginator import Paginator


from .forms import FormAudiocodesMP112, FormMainGateway, FormTypeGateway, FormLoginPasswordGW
from .models import MainGateway, TypeGateway, LoginPasswordGW
from .utils import CreateObjectsMixin


class MainGatewayView(View):

    def get(self, request, name_gw):
        data = get_object_or_404(MainGateway, name_gw__exact=name_gw)
        return render(request, 'voicegateway/main_gateway_view.html', context={'data': data})


class MainGatewayRender(View):

    def get(self, request, name_gw):
        data = get_object_or_404(MainGateway, name_gw__exact=name_gw)
        data.render_config()
        return render(request, 'voicegateway/main_gateway_view.html', context={'data': data})


class TypeGatewayView(View):

    def get(self, request, name_type):
        data = get_object_or_404(TypeGateway, name_type__exact=name_type)
        return render(request, 'voicegateway/type_gateway_view.html', context={'data': data})


class MainGatewayCreate(CreateObjectsMixin, View):
    model_form = FormMainGateway
    templates = 'voicegateway/main_gateway_create.html'


class TypeGatewayCreate(CreateObjectsMixin, View):
    model_form = FormTypeGateway
    templates = 'voicegateway/type_gateway_create.html'


class LoginPasswordCreate(CreateObjectsMixin, View):
    model_form = FormLoginPasswordGW
    templates = 'voicegateway/ports_create.html'
    redirect_target = 'ports_all'


class MainGatewayUpdate(View):

    def get(self, request, name_gw):
        data = MainGateway.objects.get(name_gw__exact=name_gw)
        bound_form = FormMainGateway(instance=data)
        return render(request, 'voicegateway/main_gateway_update.html', context={'data': data, 'form': bound_form})


    def post(self, request, name_gw):
        data = MainGateway.objects.get(name_gw__exact=name_gw)
        bound_form = FormMainGateway(request.POST, instance=data)

        if bound_form.is_valid():
            new_objects = bound_form.save()
            return redirect(new_objects)
        return render(request, 'voicegateway/main_gateway_update.html', context={'data': data, 'form': bound_form})


class TypeGatewayUpdate(View):

    def get(self, request, name_type):
        data = TypeGateway.objects.get(name_type__exact=name_type)
        bound_form = FormTypeGateway(instance=data)
        return render(request, 'voicegateway/type_gateway_update.html', context={'data': data, 'form': bound_form})


    def post(self, request, name_type):
        data = TypeGateway.objects.get(name_type__exact=name_type)
        bound_form = FormTypeGateway(request.POST, request.FILES, instance=data)

        if bound_form.is_valid():
            new_objects = bound_form.save()
            return redirect(new_objects)
        return render(request, 'voicegateway/type_gateway_update.html', context={'data': data, 'form': bound_form})


class MainGatewayDelete(View):

    def get(self, request, name_gw):
        data = MainGateway.objects.get(name_gw__exact=name_gw)
        return render(request, 'voicegateway/main_gateway_delete.html', context={'data': data})


    def post(self, request, name_gw):
        data = MainGateway.objects.get(name_gw__exact=name_gw)
        data.delete()
        return redirect(reverse('gateway_all'))


class TypeGatewayDelete(View):

    def get(self, request, name_type):
        data = TypeGateway.objects.get(name_type__exact=name_type)
        return render(request, 'voicegateway/type_gateway_delete.html', context={'data': data})


    def post(self, request, name_type):
        data = TypeGateway.objects.get(name_type__exact=name_type)
        data.delete()
        return redirect(reverse('type_all'))







def all_main_gw(request):
    data = MainGateway.objects.all()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)  #/?page=1
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }

    return render(request, 'voicegateway/main_gateway_all.html', context=context)


def all_type(request):
    data = TypeGateway.objects.all()

    paginator = Paginator(data, 10)
    page_number = request.GET.get('page', 1)  #/?page=1
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }
    return render(request, 'voicegateway/type_gateway_all.html', context=context)


def all_ports(request):
    data = LoginPasswordGW.objects.all
    return render(request, 'voicegateway/ports_all.html', context={'data': data})










