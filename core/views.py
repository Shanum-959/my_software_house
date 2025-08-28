from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def home_view(request):
    form = ContactForm()

    return render(request, 'home.html', {'form': form})

@cache_page(60 * 15)
def about_view(request):
    return render(request, 'about.html')



def contact_list(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                send_mail(
                    subject=f"New Contact Form Submission from {form.cleaned_data['name']}",
                    message=f"Name: {form.cleaned_data['name']}\n"
                            f"Email: {form.cleaned_data['email']}\n"
                            f"Message: {form.cleaned_data['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,    # info@exionixtech.com
                    recipient_list=['info@exionixtech.com'],   # Mailbox
                    fail_silently=False,
                )
            except Exception as e:
                # Agar email fail ho jaye, error log karo
                print("Email send failed:", e)
            return redirect('contact_success')  # redirect to a thank you page
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def contact_success(request):
    return render(request, "success.html")
