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
        trans_id = body['trans_id']
        # address = body['address']
        new_data = Address(trans_id=trans_id)
        new_data.save()
        return HttpResponse('Done')
    
    return HttpResponse('Send Json Data Via This API Endpoint')