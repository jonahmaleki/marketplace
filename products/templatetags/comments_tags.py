from django import template

register = template.library()

@register.filter
def only_active_comment(comment):
    return comment.filter(active=True)
