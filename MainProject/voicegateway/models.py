from django.db import models
from django.shortcuts import reverse
from django.template import loader


class MainGateway(models.Model):
    name_gw = models.CharField(max_length=30, unique=True)
    type = models.ForeignKey('TypeGateway', on_delete=models.RESTRICT) #restrict защита от удаление в связанной таблице
    ip = models.GenericIPAddressField(unique=True)
    mac = models.CharField('MAC адрес', max_length=13, unique=True)


    class Meta:
        verbose_name = 'Голосовой шлюз'
        verbose_name_plural = 'Голосовые шлюзы'
        ordering = ['name_gw'] #Определяет порядок выгрузки всем элементов objects.

    def render_config(self):
        """
        Собирает конфиг из шаблона типа конфигурации и настроек ГШ
        """
        typegw = TypeGateway.objects.get(name_type__exact=self.type)
        context = self.get_context()

        data = loader.render_to_string(typegw.template_file.name, context)

        with open('voicegateway/media/ftp/{}.cfg'.format(self.mac), 'w') as fp:
            fp.write(data)
        return None


    def get_context(self):
        """
        Собирает словарь с нужными параметрами для создания конфигурации:
        [Логины/пароли со всех портов, ip, mac]
        :return: > Словарь
        """
        context = dict()
        list_login = LoginPasswordGW.objects.filter(gateway=self.id)

        for el in list_login:
            context['login{}'.format(el.number_ports)] = el.login
            context['password{}'.format(el.number_ports)] = el.password
        context['mac'] = self.mac
        context['ip'] = self.ip

        return context

    def get_absolute_url(self):
        return reverse('gateway_view', kwargs={'name_gw': self.name_gw})


    def get_ubdate_url(self):
        return reverse('gateway_update', kwargs={'name_gw': self.name_gw})


    def get_delete_url(self):
        return reverse('gateway_delete', kwargs={'name_gw': self.name_gw})

    def get_render_url(self):
        return reverse('gateway_render', kwargs={'name_gw': self.name_gw})



    def __str__(self):
        return self.name_gw


class TypeGateway(models.Model):
    name_type = models.CharField(max_length=50, unique=True)
    softswitch = models.CharField('Платформа', max_length=50)
    ports = models.IntegerField()
    template_file = models.FileField(max_length=50, upload_to='type/', default='-')


    class Meta:
        verbose_name = 'Таблица типов голосовых шлюзов'
        verbose_name_plural = 'Таблицы типов голосовых шлюзов'
        ordering = ['name_type']  # Определяет порядок выгрузки всем элементов мотодом objects.


    # в метод .save() добавляеться проверка наличия файла, Исключение для создания ового объекта
    def save(self, *args, **kwargs):
        try:
            check_obj = TypeGateway.objects.get(id__exact=self.id)
            if check_obj.template_file != self.template_file:
                check_obj.template_file.delete(save=False)
        except:
            pass
        super(TypeGateway, self).save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        self.template_file.delete(save=False)
        super(TypeGateway, self).delete(*args, **kwargs)




    def get_absolute_url(self):
        return reverse('type_view', kwargs={'name_type': self.name_type})


    def get_update_url(self):
        return reverse('type_update', kwargs={'name_type': self.name_type})


    def get_delete_url(self):
        return reverse('type_delete', kwargs={'name_type': self.name_type})


    def __str__(self):
        return self.name_type


class LoginPasswordGW(models.Model):
    login = models.CharField('Логин', max_length=20, null=True, blank=True)
    password = models.CharField('Пароль', max_length=20, null=True, blank=True)
    gateway = models.ForeignKey('MainGateway', on_delete=models.CASCADE)
    number_ports = models.IntegerField()


    def __str__(self):
        return str(self.login) + str(self.number_ports)


    class Meta:
        unique_together = ('gateway', 'number_ports')
        verbose_name = 'Таблица логинов и паролей'
        verbose_name_plural = 'Таблицы логинов и паролей'
        ordering = ['number_ports']


class TypeAudiocodesMP112(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'TypeAudiocodesMP112'
        verbose_name_plural = 'TypeAudiocodesMP112s'


class AudiocodesMP112(models.Model):
    name = models.CharField('Название', max_length=30, unique=True)
    type = models.ForeignKey('TypeAudiocodesMP112', on_delete=models.CASCADE)
    ip = models.GenericIPAddressField('ip адрес', unique=True)
    mac = models.CharField('MAC адрес', max_length=13, unique=True)
    login1 = models.CharField('Логин 1 порта', max_length=20, null=True, blank=True,)
    password1 = models.CharField('Пароль 1 порта', max_length=20, null=True, blank=True,)
    login2 = models.CharField('Логин 2 порта', max_length=20, null=True, blank=True,)
    password2 = models.CharField('Пароль 2 порта', max_length=20, null=True, blank=True,)
    description = models.CharField('Описание ГШ', max_length=150, null=True, blank=True,)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('gateway_view', kwargs={'name': self.name})


    class Meta:
        verbose_name = 'AudiocodesMP112'
        verbose_name_plural = 'AudiocodesMP112s'

