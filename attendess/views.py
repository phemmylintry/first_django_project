from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Attendee

def current_time(request):
    attendees = Attendee.objects.all()

    return render(request, "attendess/index.html", {"attendees": attendees})

