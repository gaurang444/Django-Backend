from django.shortcuts import redirect, render
from django.conf import settings
import requests
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import *
import csv
from .filters import *
#api view to get all users and table view
def home_view(request):
    all_users=User.objects.all()
    user_filter = UserFilter(request.GET, queryset=all_users)
    res={}
    res['data']=user_filter
    res['filter']=user_filter
    return render(request,"index.html",res)

#end point for creating new user. check if user already exists on adhar_num search key
def add_user(request):
    username=request.POST['username']
    email=request.POST['email']
    phone=request.POST['phone']
    adhar_num=request.POST['adhar_num']
    address=request.POST['address']
    print(username,email,phone,adhar_num,address)
    res={}
    user_obj=User.objects.filter(adhar_num=adhar_num).first()
    if user_obj:
        print("user already exists")
        res['status']="Already Exists"
        return HttpResponse(json.dumps(res), content_type='application/json')
    new_user_obj=User(user_name=username,adhar_num=adhar_num,phone_num=phone,email=email,address=address,is_Active=True)
    new_user_obj.save()
    print("new user created")
    res["status"]="User Created"
    res["id"]=new_user_obj.id
    return HttpResponse(json.dumps(res), content_type='application/json')


#end point to update an user
def update_user(request):
    username=request.POST['username']
    email=request.POST['email']
    phone=request.POST['phone']
    db_id=int(request.POST['dbid'])
    address=request.POST['address']
    soft_delete=str(request.POST['soft-delete'])
    print(username,email,phone,db_id,address,soft_delete)
    
    user_obj=User.objects.filter(id=db_id).first()
    res={}
    if user_obj is None:
        res['status']="DNE"
        return HttpResponse(json.dumps(res), content_type='application/json')
    user_obj.user_name=username
    user_obj.email=email
    user_obj.phone_num=phone
    user_obj.address=address
    
    if soft_delete=="false":
        user_obj.is_Active=False
    if soft_delete=="true":
        user_obj.is_Active=True

    user_obj.save()
    res["status"]="Success"
    return HttpResponse(json.dumps(res), content_type='application/json')



#end point to delete an user
def delete_user(request):
    db_id=int(request.POST['dbid'])
    user_obj=User.objects.filter(id=db_id).first()
    res={}
    if user_obj is None:
        res['status']="DNE"
        return HttpResponse(json.dumps(res), content_type='application/json')
    user_obj.delete()
    print("deleted successfully")
    res["status"]="Success"
    return HttpResponse(json.dumps(res), content_type='application/json')

def send_email():
    return

def download_csv(request):
    db_all=User.objects.all()
    response = HttpResponse(content_type='text/csv')
    filename = u"KAFQA_DATA_EXPORT " + " " + str(timezone.now()) + ".csv"
    response['Content-Disposition'] = u'attachment; filename="{0}"'.format(filename)
    writer = csv.writer(response)
    writer.writerow(['Username','Adhar_number','Phone_number','Email','Address','Is_Active()','user_created_at','last_updated_at'])
    for obj in db_all:
        writer.writerow([obj.user_name,obj.adhar_num,obj.phone_num, obj.email, obj.address, obj.is_Active,obj.user_created_at,obj.last_updatedat])
    return response
    

     



