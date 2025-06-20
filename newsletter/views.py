from django.shortcuts import render

def newsletter_list(request):
    return render(request, "newsletter/newsletter.html")