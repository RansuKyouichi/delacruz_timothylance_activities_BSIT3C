from django import template

register = template.Library()

@register.filter
def format_number(value):
    try:
        return f"${int(value):,}"
    except ValueError:
        return value
