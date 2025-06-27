from django.shortcuts import render, get_object_or_404
from .models import Project, Document, Message
from django.contrib.auth.decorators import login_required
from services.models import Service, OrderedService



def client_portal_home(request):
    return render(request, 'client_portal/basic.html')

@login_required
def dashboard_view(request):
    projects = Project.objects.filter(client=request.user)
    services = OrderedService.objects.filter(user=request.user)

    return render(request, 'client_portal/client_portal.html', {
        'projects': projects,
        'services': services,
    })


@login_required
def project_detail_view(request, pk):
    user = request.user
    has_services = OrderedService.objects.filter(user=user).exists()

    if not has_services:
        return render(request, 'client_portal/no_services.html')  # Show message

    project = get_object_or_404(Project, pk=pk, client=user)
    documents = Document.objects.filter(project=project)
    messages = Message.objects.filter(project=project)

    return render(request, 'client_portal/project_detail.html', {
        'project': project,
        'documents': documents,
        'messages': messages,
    })

