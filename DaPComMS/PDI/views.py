from django.shortcuts import render

from django.http import HttpResponse
from .models import Activity

# Create your views here.

def index(request):
    all_activities = Activity.objects.all()
    html = ''
    
    for activity in all_activities:
        url = '/pdi/' + str(activity.id) + '/'
        
        html += '<a href = "' + url +'">' + activity.name + '</a><br>'
        
    return HttpResponse(html)

def update(request, activity_id):
    return HttpResponse("<h2> Activity ID: " + str(activity_id)
                       + "</h2>")
