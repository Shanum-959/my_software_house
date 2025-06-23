from django.shortcuts import render, get_object_or_404
from .models import Project, Document, Message
from django.contrib.auth.decorators import login_required

def client_portal_home(request):
    return render(request, 'client_portal/basic.html')

@login_required
def dashboard_view(request):
    projects = Project.objects.filter(client=request.user)
    return render(request, 'client_portal/client_portal.html', {'projects': projects})

@login_required
def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk, client=request.user)
    documents = Document.objects.filter(project=project)
    messages = Message.objects.filter(project=project).order_by('-timestamp')
    return render(request, 'client_portal/project_detail.html', {
        'project': project,
        'documents': documents,
        'messages': messages
    })
