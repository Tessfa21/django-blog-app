from django.contrib import admin
from .models import New

# Register your models here.
class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'detail', 'published_date','image')

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nDetail: {self.detail}\nPublished Date: {self.published_date}"

admin.site.register(New, NewAdmin) 