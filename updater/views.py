import json

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from updater.models import Host, Update
from mydns.models import RessourceRecord

@csrf_exempt
def update(request):
    if request.method != 'POST':
        return HttpResponse('No data submitted')
    host = get_object_or_404(Host, name=request.POST['hostname'])
    if not host.access_key == request.POST['key']:
        return HttpResponse('Could not authorize')
    update = Update(host=host, 
                    from_ip=request.META['REMOTE_ADDR'],
                    message=request.POST['message'])
    update.save()
    rr = RessourceRecord.get_or_create(name=host.name) # zone gets set in mysql to "1" -- I'll change this later
    rr.data = request.META['REMOTE_ADDR']
    rr.save()
    return HttpResponse('1')
