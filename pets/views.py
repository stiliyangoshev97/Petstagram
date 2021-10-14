from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from pets.forms import PetForm, LikeForm, CommentForm
from pets.models import Pet, Like, Comment

# Create your views here.

@login_required
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('pets:pet_details', pet.id)
    else:
        form = PetForm()

    context = {'form': form}

    return render(request, 'pets/create_pet.html', context)

def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
    else:
        form = PetForm(instance=pet)

    context = {
        "pet": pet,
        "form": form,
    }

    return render(request, 'pets/edit_pet.html', context)


def remove_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    pet.delete()

    return redirect("pets:pets_list")


@login_required
def pets_list(request):
    pets = Pet.objects.all()

    # Owned pets
    owned_pets = Pet.objects.filter(user=request.user).count()

    context = {'pets': pets, "owned_pets": owned_pets,}

    return render(request, 'pets/pets_list.html', context)

@login_required
def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    user = request.user
    # Filter the likes. Make a list with all the likes where user is the current user and pet is the pet in details
    likes = Like.objects.filter(user=user).filter(pet=pet)

    # Owned comments
    owned_comments = Comment.objects.filter(user=request.user).count()

    # Total comments
    total_comments = Comment.objects.filter(pet=pet).count()



    # Check if its owner by seeing if the pet.user owner is the same as the request.user (the current user)
    is_owner = pet.user == user
    # Returning the number of likes that a pet has
    likes_count = Like.objects.filter(pet=pet).count()

    # Check if it's liked
    is_liked = False
    for like in likes:
        is_liked = like.user == user # If a user liked a pet, it will return true




    # Filter the comments for the pet
    comments_pet = Comment.objects.filter(pet=pet)

    # Create a CommentForm
    if request.method == "POST":
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.pet = pet
            comment.user = request.user
            comment.save()
            return redirect('pets:pet_details', pet.id)
    else:
        comment_form = CommentForm()

    # Create like form
    if request.method == "POST":
        like_form = LikeForm(request.POST)

        if like_form.is_valid():
            like = like_form.save(commit=False)
            like.user = request.user
            like.pet = pet
            like.save()
            return redirect('pets:pet_details', pet.id)
    else:
        like_form = LikeForm()

    # Create dislike form, maybe its better to create a different view

    context = {
        "pet": pet,
        "is_owner": is_owner,
        "likes_count": likes_count,
        "like_form": like_form,
        "comments_pet": comments_pet,
        "comment_form": comment_form,
        "is_liked": is_liked,
        "owned_comments": owned_comments,
        "total_comments": total_comments,

    }

    return render(request, 'pets/pet_details.html', context)


def dislike_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    user = request.user

    like = Like.objects.get(pet=pet, user=user)

    like.delete()

    return redirect("pets:pet_details", pet.id)




def like_pet(request, pk):
    pass


def comment_pet(request, pk):
    pass

