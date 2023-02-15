

# Register your models here.
from django.contrib import admin 
	
# Register your models here. 

# from .models import Food 
# admin.site.register(Food) 

from .models import Blog
admin.site.register(Blog)

from .models import Vendor
admin.site.register(Vendor)

from .models import Appuser
admin.site.register(Appuser)
