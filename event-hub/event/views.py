from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from models import Events,User

# def index(request):
#     return HttpResponse("Hello, i am event manager.")

def event_insert(request):
    variables = {}  
    print "hello event"
    if request.POST:
		event=Events()
		event.eve_name=request.POST.get('event_name')
		event.eve_location=request.POST.get('event_location')
		event.eve_date=request.POST.get('event_date')
		event.eve_entry_fee=request.POST.get('event_entryfee')
		event.eve_discription=request.POST.get('event_discription')	
		event.eve_isused = 0	
		event.save()  
    return render(request,'clients/new_event.html',variables)

def event_dashboard(request):
    variables = {}  
    print "hello event"
    events = Events.objects.filter(eve_isused = 0)  
    variables['events']=events  
    return render(request,'clients/event_dashboard.html',variables)

def user_insert(request):
    variables = {}  
    print "hello user"
    if request.POST:
        user=User()
        user.use_name=request.POST.get('use_name')
        user.use_email=request.POST.get('use_email')
        user.use_mobile=request.POST.get('use_mobile')
        user.use_Address=request.POST.get('use_Address')
        user.set_password(request.POST.get('use_password'))
        user.use_login_id=request.POST.get('use_login_id')        
        user.use_isused = 0    
        user.save()  
    return render(request,'clients/add_new_user.html',variables)














