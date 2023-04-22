from django import template

register = template.Library()

@register.filter
def trans_to_persian(value):
    value = str(value)
    translation_table = str.maketrans('0123456789', '۰١٢٣٤٥٦٧٨٩')

    return value.translate(translation_table)
