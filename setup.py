try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='nocaptcha-client',
    version='1.0.0',
    url="http://nocaptcha.mail.ru",
    author="Sergey Trofimov",
    author_email="s.trofimov@corp.mail.ru",
    description="A client library for nocaptcha.mail.ru",
    long_description="""\
Provides a captcha for Python using the nocaptcha.mail.ru service. Does not require
any imaging libraries because the nocaptcha is served directly from mail.ru.

It is licensed under an MIT/X11 license.
""",
    license="MIT/X11",
    classifiers=[
        "Topic :: Security",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
    ],
    packages=find_packages(),
    namespace_packages=['nocaptcha'],
    zip_safe=False,
)
