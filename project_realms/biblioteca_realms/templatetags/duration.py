from django import template

register = template.Library()


@register.filter
def duration(value):
    if value is None:
        return "00:00"

    horas = value // 3600
    minutos = (value % 3600) // 60
    segundos = value % 60

    if horas > 0:
        return f"{horas}:{minutos:02}:{segundos:02}"

    return f"{minutos}:{segundos:02}"