from django.contrib import admin

# Register your models here.

from .models import Meals , Category


class MealsAdmin(admin.ModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name' ,'preparation_time', 'people', 'price']
    search_fields = ['name', 'description' ]
    list_filter = ('category','people')

admin.site.register(Meals , MealsAdmin)
admin.site.register(Category)