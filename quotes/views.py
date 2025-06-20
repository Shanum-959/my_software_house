from django.shortcuts import render

def qoutes_list(request):
    return render(request, "qoutes/qoutes.html")