from django import template
from django.template.context_processors import request

from pets.models import Pet, Comment

register = template.Library()
# Count total pets
@register.inclusion_tag("pets/inclusion_tags/total_pets.html")
def count_pets():
    pets_number = Pet.objects.all().count()

    context = {
        "pets_number": pets_number,
    }

    return context


# Count pets that are owned by the request.user
@register.inclusion_tag("pets/inclusion_tags/owned_pets.html")
def count_owned_pets(request):
    owned_pets = Pet.objects.filter(user=request.user).count()

    context = {
        "owned_pets": owned_pets,
    }

    return context



# Count total comments
@register.inclusion_tag("pets/inclusion_tags/total_comments.html")
def count_comments():
    total_comments = Comment.objects.all().count()

    context = {
        "total_comments": total_comments,
    }

    return context

# Count comment written by user
@register.inclusion_tag("pets/inclusion_tags/owned_comments.html")
def count_owned_comments():

    owned_comments = Comment.objects.filter(user=request.user).count()

    context = {
        "owned_comments": owned_comments,

    }

    return context
