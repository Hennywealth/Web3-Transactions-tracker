from django.http import HttpResponse
from celery import  group
# from.tasks import  log_loop
import json
from .models import Address
from django.shortcuts import render

def test(request):
    # log_loop.delay("block_filter", 2)
    if request.method == "POST":
        body_unicode = request.body	
        body = json.loads(body_unicode.decode('utf-8')) 
        name = body['name']
        address = body['address']
        new_data = Address(name=name, address=address)
        new_data.save()
        return HttpResponse('Done')
    return None