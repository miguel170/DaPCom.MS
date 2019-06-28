from django.contrib import admin
from .models import ActivityType
from .models import Activity
from .models import Classification
from .models import Basis
from .models import Data
from .models import Office


# Register your models here.

admin.site.register(ActivityType)

admin.site.register(Office)

admin.site.register(Activity)

admin.site.register(Classification)

admin.site.register(Basis)

admin.site.register(Data)