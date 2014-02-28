# encoding: utf-8
from django import forms
from django.conf import settings

from nocaptcha.client import captcha


class BaseForm(forms.Form):
    name = forms.CharField(label=u'Имя')
    email = forms.EmailField(label=u'Электронная почта')

    # def __init__(self, *args, **kwargs):
    #     self.private_key = kwargs.get('private_key')
    #     super(BaseForm, self).__init__(*args, **kwargs)

    def clean(self):
        try:
            captcha.check_captcha(
                self.private_key,
                self.data.get('nocaptcha_id'),
                self.data.get('nocaptcha_value'),
                self.is_dev,
            )
        except captcha.CaptchaError as e:
            raise forms.ValidationError(e)

        return super(BaseForm, self).clean()


class DevForm(BaseForm):
    private_key = settings.DEV_PRIVATE_KEY
    is_dev = True


class ProductionForm(BaseForm):
    private_key = settings.PRODUCTION_PRIVATE_KEY
    is_dev = False