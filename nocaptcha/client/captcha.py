# encoding: utf-8
import json
import urllib
import logging


API_SERVER = 'https://api-nocaptcha.mail.ru'


class CaptchaError(Exception):
    pass


def check_captcha(private_key, captcha_id, captcha_value, **kwargs):
    """
    Returns True if captcha is valid
    Or raise CaptchaError exception with description
    """
    result, error = None, None
    params = urllib.urlencode({
        'private_key': private_key,
        'captcha_id': captcha_id,
        'captcha_value': isinstance(captcha_value, unicode) and captcha_value.encode('utf-8') or captcha_value,
    })

    try:
        url = '{api_server}/check?{params}'.format(
            api_server=kwargs.get('api_server', API_SERVER),
            params=params
        )
        logging.debug(url)

        result = urllib.urlopen(url)
        result = result.read()
        logging.debug(result)

        result = json.loads(result)

        if result['status'] != 'ok':
            error = result.get('desc', 'Bad response')
        elif not result['is_correct']:
            error = 'Bad captcha'
    except IOError:
        error = 'Server unavailable'
    except ValueError:
        error = 'Bad response'

    if error:
        raise CaptchaError(error)

    return True


def source_captcha(public_key, **kwargs):
    """
    Return url of source script to display captcha
    public_key - The public api key
    """
    return '{api_server}/captcha?public_key={public_key}'.format(
        api_server=kwargs.get('api_server', API_SERVER),
        public_key=public_key,
    )


def display_captcha(public_key, **kwargs):
    """
    Return HTML code to display captcha
    public_key - The public api key
    """

    return '<script async src="{url}" type="text/javascript"></script>'.format(
        url=source_captcha(public_key, **kwargs),
    )
