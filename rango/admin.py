from django.contrib import admin
from rango.models import Category, Page
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js
# Register your models here.

class PageAdmin(admin.ModelAdmin) :
    list_display = ('category','title','url')

#Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}

# update the registration to include this customized interface.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)