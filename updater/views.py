import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from updater.models import Host, Update

def update(request):
    if request.method != 'POST':
        return HttpResponse('No data submitted')
    host = get_object_or_404(Host, name=request.POST['hostname'])
    if not host.access_key == request.POST['key']:
        return HttpResponse('Could not authorize')
    update = Update(host=host, 
                    from_ip=requst.META.REMOTE_ADDR,
                    message=request.POST['message'])
    update.save()
    return HttpResponse('1')
