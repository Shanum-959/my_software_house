from django.shortcuts import render

def knowledge(request):
    return render(request, "knowledge_base/knowledge_base.html")