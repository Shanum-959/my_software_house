from django.shortcuts import render

def localization_list(request):
    return render(request, "localization/localization.html")