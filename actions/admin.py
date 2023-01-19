from django.contrib import admin

from .models import Action

# Register your models here.

@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    '''Admin View for Action'''

    list_display = ('user','verb', 'target', 'created')
    list_filter = ('created',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    search_fields = ('verb',)
    # date_hierarchy = ''
    # ordering = ('',)