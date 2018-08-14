from django import template
from django.core.files.storage import default_storage

register = template.Library()

@register.filter(name='file_exists')
def file_exists(filepath):
    if default_storage.exists(filepath):
        return filepath
    else:
        index = filepath.rfind('/')
        new_filepath = filepath[:index] + '/image.png'
        return new_filepath
