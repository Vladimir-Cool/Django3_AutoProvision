from django.urls import path
from .views import *

#/gateway/
urlpatterns = [
    #path('', gateway_home, name='gateway_home'),
    path('views_all/', all_main_gw, name='gateway_all'),
    path('create_main/', MainGatewayCreate.as_view(), name='gateway_create'),
    path('views/<str:name_gw>/', MainGatewayView.as_view(), name='gateway_view'),
    path('views/<str:name_gw>/update/', MainGatewayUpdate.as_view(), name='gateway_update'),
    path('views/<str:name_gw>/delete/', MainGatewayDelete.as_view(), name='gateway_delete'),
    path('views/<str:name_gw>/render/', MainGatewayRender.as_view(), name='gateway_render'),

    path('views_type_all/', all_type, name='type_all'),
    path('create_type/', TypeGatewayCreate.as_view(), name='type_create'),
    path('views_type/<str:name_type>/', TypeGatewayView.as_view(), name='type_view'),
    path('views_type/<str:name_type>/update/', TypeGatewayUpdate.as_view(), name='type_update'),
    path('views_type/<str:name_type>/delete/', TypeGatewayDelete.as_view(), name='type_delete'),

    path('views_port_all/', all_ports, name='ports_all'),
    path('create_ports/', LoginPasswordCreate.as_view(), name='ports_create'),


]