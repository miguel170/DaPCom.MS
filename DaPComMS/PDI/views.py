from django.views import generic
from .models import Activity, Data
#from django.http import Http404
#from django.http import HttpResponse
##
    # alternative* from django.template import loader
from django.shortcuts import render, get_object_or_404


    # Create your views here.
def index(request):
  all_activities = Activity.objects.all()
  count =  Activity.objects.count()
#  template = loader.get_template('PDI/index.html')
 
  context = { 'activities' : all_activities,
              'total_act' : count,
              'web_title' : "Personal Data Inventory"}

  return render(request, 'PDI/index.html', context)
#       return HttpResponse(template.render(context, request))

def update(request, activity_id):
   # try:
   #     context = {
   #     'activity' : Activity.objects.get(pk=activity_id),
   #     }

   # except Activity.DoesNotExist:
   #     raise Http404("Activity is not available")

   act = get_object_or_404(Activity, pk = activity_id)
   elements =  Data.objects.filter(activity = activity_id).all()

   context = {
    'activity' : act,
    'elements': elements,
    'web_title' : "Personal Data Inventory - Update"
   }

   return render(request, 'PDI/update.html/', context)