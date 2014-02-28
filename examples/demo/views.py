# encoding: utf-8
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import FormView, TemplateView
from django.conf import settings

from nocaptcha.client import captcha
from forms import DevForm, ProductionForm


class IndexView(TemplateView):
    template_name = 'base.html'


class CaptchaView(FormView):
    template_name = 'form.html'

    # def get_context_data(self, **kwargs):
    #     return {
    #
    #     }

    def form_invalid(self, form):
        messages.error(self.request, u'Форма заполнена неправильно, ниже будут пояснения')
        return super(CaptchaView, self).form_invalid(form)

    def form_valid(self, form):
        messages.info(self.request, u'С капчей всё ок и тут мы отсылаем сообщение для пользователя «{name}» с почтой «{email}»'.format(
            **form.cleaned_data
        ))

        return HttpResponseRedirect('/')


class CustomProductionView(CaptchaView):
    template_name = 'custom_form.html'
    form_class = ProductionForm

    def get_context_data(self, **kwargs):
        kwargs['heading'] = u'Без библиотеки через боевой сервер'
        kwargs['public_key'] = settings.PRODUCTION_PUBLIC_KEY
        kwargs['private_key'] = settings.PRODUCTION_PRIVATE_KEY
        kwargs['server_url'] = settings.PRODUCTION_SERVER
        print settings.TEMPLATE_DEBUG
        return kwargs


class CustomDevView(CaptchaView):
    template_name = 'custom_form.html'
    form_class = DevForm

    def get_context_data(self, **kwargs):
        kwargs['is_dev'] = True
        kwargs['heading'] = u'Без библиотеки через девелоперский сервер'
        kwargs['public_key'] = settings.DEV_PUBLIC_KEY
        kwargs['private_key'] = settings.DEV_PRIVATE_KEY
        kwargs['server_url'] = settings.DEV_SERVER
        return kwargs


class LibraryProductionView(CaptchaView):
    template_name = 'library_form.html'
    form_class = ProductionForm

    def get_context_data(self, **kwargs):
        kwargs['heading'] = u'С библиотекой через боевой сервер'
        kwargs['public_key'] = settings.PRODUCTION_PUBLIC_KEY
        kwargs['private_key'] = settings.PRODUCTION_PRIVATE_KEY
        kwargs['server_url'] = settings.PRODUCTION_SERVER
        kwargs['display_captcha'] = captcha.display_captcha(settings.PRODUCTION_PUBLIC_KEY)
        return kwargs


class LibraryDevView(CaptchaView):
    template_name = 'library_form.html'
    form_class = DevForm

    def get_context_data(self, **kwargs):
        kwargs['is_dev'] = True
        kwargs['heading'] = u'С библиотекой через девелоперский сервер'
        kwargs['public_key'] = settings.DEV_PUBLIC_KEY
        kwargs['private_key'] = settings.DEV_PRIVATE_KEY
        kwargs['server_url'] = settings.DEV_SERVER
        kwargs['display_captcha'] = captcha.display_captcha(settings.DEV_PUBLIC_KEY, api_server=settings.DEV_SERVER)
        return kwargs


class DjangoProductionView(CaptchaView):
    template_name = 'django_form.html'
    form_class = ProductionForm

    def get_context_data(self, **kwargs):
        kwargs['heading'] = u'С библиотекой через боевой сервер'
        kwargs['public_key'] = settings.PRODUCTION_PUBLIC_KEY
        kwargs['private_key'] = settings.PRODUCTION_PRIVATE_KEY
        kwargs['server_url'] = settings.PRODUCTION_SERVER
        kwargs['display_captcha'] = captcha.display_captcha(settings.PRODUCTION_PUBLIC_KEY)
        return kwargs


class DjangoDevView(CaptchaView):
    template_name = 'django_form.html'
    form_class = DevForm

    def get_context_data(self, **kwargs):
        kwargs['is_dev'] = True
        kwargs['heading'] = u'С библиотекой через девелоперский сервер'
        kwargs['public_key'] = settings.DEV_PUBLIC_KEY
        kwargs['private_key'] = settings.DEV_PRIVATE_KEY
        kwargs['server_url'] = settings.DEV_SERVER
        kwargs['display_captcha'] = captcha.display_captcha(settings.DEV_PUBLIC_KEY, is_dev=True)
        return kwargs
