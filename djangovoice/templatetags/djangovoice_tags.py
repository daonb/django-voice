from django.template import Library

register = Library()

@register.simple_tag
def user_name(user):
    """if user has full name, get user's full name, else username.
    """
    full_name = user.get_full_name()
    if not full_name:
        return user.username

    return full_name
