from django.contrib import admin
from .models import Topbg
from .models import Latest_news
from .models import Events_details
from .models import Trending

# Register your models here.

admin.site.register(Topbg)
admin.site.register(Latest_news)
admin.site.register(Events_details)
admin.site.register(Trending)