from django import template

register = template.Library()

@register.filter
def get_weekday_labels(queryset):
    return [day.choice_label for day in queryset]
