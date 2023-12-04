from django.shortcuts import render
from .forms import BookForm
from django.http import HttpResponseRedirect

# Create your views here.
def get_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
        
    else:
        form = BookForm()

    return render(request, "name.html", {"form": form})