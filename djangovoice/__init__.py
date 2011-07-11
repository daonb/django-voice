from django.template import add_to_builtins

add_to_builtins('django.templatetags.i18n')

VERSION = (0, 2)

def get_version():
    return '.'.join(map(str, VERSION))
