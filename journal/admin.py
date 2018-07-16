from django.contrib import admin

from .models import Journal


class JournalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Create about', {
            'fields':['name','date'],
            'classes':'wide'
        }),
        ('Journal Detail', {'fields':['journal']}),
        ('Week journal', {
            'fields':['wens','thurs','fri','satur','sun','mon','tues']
        }),
    ]
    list_display = ("name", "date", "journal")
    list_filter = ['date']
    search_fields = ['name']

admin.site.register(Journal, JournalAdmin)
# アプリをadmin上から編集できるようにする。
