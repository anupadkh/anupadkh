from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


# @register.inclusion_tag('form/sidebar.html', takes_context=True)
# def sidebar(context):
#     return {
#         'link':
#     }