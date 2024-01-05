from django.shortcuts import render
from .models import Topbg
from .models import Latest_news
from .models import Events_details
from .models import Trending

# Create your views here.

def index(request):

    Topbgimg = Topbg.objects.all()
    Latestnews = Latest_news.objects.all()
    Eventsdetails = Events_details.objects.all()
    Trend = Trending.objects.all()

    return render(request, "index.html", {'Topbg':Topbgimg, 'Latestnews':Latestnews, 'Eventsdetails':Eventsdetails, 'Trend':Trend})