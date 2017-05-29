from .models import Event, Field, Product

def products(request):
   return {
        'events': Event.objects.all()[:5],
        'fields': Field.objects.all()[:5],
        'products': Product.objects.all()[:5],
   }
