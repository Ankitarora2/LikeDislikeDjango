from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import LikeDislike


def update_count(request):
    # Get the like or dislike type from the request
    like_type = request.GET.get('type')

    # Get the current like and dislike counts from the database
    like_dislike = LikeDislike.objects.first()
    like_count = like_dislike.like_count
    dislike_count = like_dislike.dislike_count

    # Update the like or dislike count
    if like_type == 'like':
        like_count += 1
    elif like_type == 'dislike':
        dislike_count += 1

    # Save the updated counts to the database
    like_dislike.like_count = like_count
    like_dislike.dislike_count = dislike_count
    like_dislike.total_count = like_count + dislike_count
    like_dislike.save()

    # Return the updated counts as a JSON response
    return JsonResponse({'like_count': like_count, 'dislike_count': dislike_count})
