from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def home(request):	
    return render_to_response("index.html")

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
    property = Property.objects.get(id=property_id)
    c = get_common_dict(request)
    d = {'property': property, 'tasks': property.get_tasks()}
    c.update(d)
    return render_to_response('tasks.html', c)

