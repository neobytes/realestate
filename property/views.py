from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext

from property.forms import LoginForm

import traceback

from property.models import Property

@login_required
def home(request):	
    print "=== home =="
    properties = Property.objects.all()
    c = {'properties': properties}
    return render_to_response('home.html', c)

def add_property(request):
    return render_to_response('add_property.html')

def buying(request):
    return render_to_response('buying.html')

def selling(request):
    return render_to_response('selling.html')

def mortages(request):
    return render_to_response('mortages.html')

def homeforsale(request):
    return render_to_response('homeforsale.html')

def fore(request):
    return render_to_response('fore.html')

def lotsandland(request):
    return render_to_response('lotsandland.html')

def freehomeplans(request):
    return render_to_response('freehomeplans.html')


def agents(request):
    return render_to_response('agents.html')

def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contacts.html')

def rental(request):
    return render_to_response('rental.html')

def moving(request):
    return render_to_response('moving.html')


@csrf_exempt
def save_property(request):
    """
    save property in db
	"""
    try:
        property = Property(title=request.POST['title'], slug=request.POST['title'], description=request.POST['descrip'], price=request.POST['price'], available=request.POST['avail'], baths=request.POST['bath'], parking=request.POST['parking'], rooms=request.POST['rooms'], area=request.POST['area'], owner=User.objects.get(username = request.user))
        property.save()
    except:
        traceback.print_exc()
        return HttpResponse(" Failed To Save Property !")
    return render_to_response('index.html')

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


@login_required
def main(request):
    """
    authenticate user for username and password
    """	

    return render_to_response('home.html')


################################################
#                                              #
#               LOGIN/LOGOUT                   #
#                                              #
################################################
def login_page(request):
    message = error = None
    username = password = ''
    form = LoginForm()

    # default next page is index page
    next_page = "/"

    # getting next page in get request
    if request.GET:
        next_page = request.GET.get('next')

    if request.POST:
        # a form bound to the post data
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"

                # redirect after post
                return HttpResponseRedirect(next_page)
            else:
                message = "Your account is not active, please contact the site admin."
                error = 1
        else:
            message = "Your username and/or password were incorrect."
            error = 1

    c = {'username': username, 'form': form, 'next': next_page}
    if message:
        c.update({"message": message})
    if error:
        c.update({"error": error})
    c.update(csrf(request))

    return render_to_response('login.html', c)


def logout_page(request):
    """ Log users out and re-direct them to the main page. """
    logout(request)
    return HttpResponseRedirect('/login/', {'request': request})
