from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Review
# Create your views here.

@login_required
def add_review(request):
    if request.method == "POST":
        Review.objects.create(
            user=request.user,
            imdb_id=request.POST.get("imdb_id"),
            rating=request.POST.get("rating"),
            comment=request.POST.get("comment"),
        )
    return redirect("detail", imdb_id=request.POST.get("imdb_id"))
