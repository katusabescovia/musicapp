from django import template

register = template.Library()

@register.filter
def milliseconds_to_time(ms):
    if ms is None:
        return "00:00"
    seconds = ms // 1000
    minutes, seconds = divmod(seconds, 60)
    return f"{minutes}:{seconds:02d}"
