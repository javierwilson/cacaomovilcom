from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Document)
admin.site.register(News)
admin.site.register(Webinar)
admin.site.register(Field)
admin.site.register(Catalog)
admin.site.register(CatalogFile)
