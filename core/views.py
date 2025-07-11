from django.shortcuts import render, redirect
from .forms import ContactForm
def home_view(request):
    form = ContactForm()

    return render(request, 'home.html', {'form': form})
def about_view(request):
    return render(request, 'about.html')



def contact_list(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # redirect to a thank you page
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def contact_success(request):
    return render(request, "success.html")
