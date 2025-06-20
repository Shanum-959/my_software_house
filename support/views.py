from django.shortcuts import render

def support_list(request):
    return render(request, "portfolio/portfolio.html")