from django.http import Http404
from django.http import HttpResponse
from .models import Activity

# alternative* from django.template import loader
from django.shortcuts import render, get_object_or_404


# Create your views here.

def index(request):
    all_activities = Activity.objects.all()
    
    # template = loader.get_template('PDI/index.html')
    context = { 'activities' : all_activities }
    
    # return HttpResponse(template.render(context, request))
    
    return render(request, 'PDI/index.html', context)

def update(request, activity_id):
    #try:
    #    context = {
    #     'activity' : Activity.objects.get(pk=activity_id),
    #     }
    #     
    # except Activity.DoesNotExist:
    #         raise Http404("Activity is not available")
    activity = get_object_or_404(Activity, pk = activity_id)
    return render(request, 'PDI/update.html', {'activity': activity})