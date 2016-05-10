from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from property.models import Property

def home(request):	
    properties = Property.objects.all()
    c = {'properties': properties}
    #c.update(d)
    return render_to_response('index.html', c)



def add_property(request):
	print('add property')
	return render_to_response('add_property.html')

def buying(request):
	print('buying property')
	return render_to_response('buying.html')

def selling(request):
	print('selling property')
	return render_to_response('selling.html')


def mortages(request):
	print('mortages property')
	return render_to_response('mortages.html')

def homeforsale(request):
	print('home for sale property')
	return render_to_response('homeforsale.html')

def fore(request):
	print('fore closure')
	return render_to_response('fore.html')

def lotsandland(request):
	print('lots and land')
	return render_to_response('lotsandland.html')

def freehomeplans(request):
	print('freehomeplans')
	return render_to_response('freehomeplans.html')


def agents(request):
	print('agents')
	return render_to_response('agents.html')

def about(request):
	print('about')
	return render_to_response('about.html')

def contact(request):
	print('contact')
	return render_to_response('contacts.html')

def rental(request):
	print('rental')
	return render_to_response('rental.html')

def moving(request):
	print('moving')
	return render_to_response('moving.html')


@csrf_exempt
@login_required
def save_property(request):
    """
    save property in db
    """
    try:
        title       = request.POST['title']
        shortname   = request.POST["shortname"]
        description = request.POST["description"]

        property = Property(title=title, shortname=shortname, description=description, owner=request.user)
        property.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Property !")

    return HttpResponseRedirect('/', get_common_dict(request))

@login_required
def property(request, property_id):
    """
    get all tasks for given property
    """
    properties = Property.objects.get(id=property_id)
    c = get_common_dict(request)
    d = {'properties': properties}
    c.update(d)
    return render_to_response('tasks.html', c)

