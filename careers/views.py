from django.shortcuts import render

def careers_list(request):
    return render(request, "careers/careers.html")