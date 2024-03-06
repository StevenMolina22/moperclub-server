# views.py
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site  # Import get_current_site
from .utils import get_featured_instances

def get_featured_data(request):  
    featured_instances = get_featured_instances()

    # serialize each instance into a dictionary
    serialized_instances = []
    for instance in featured_instances:
      seriealized_instance = {
          'id': instance.id,
          'name': instance.name,
          'description': instance.description,
          'address': instance.address,
          'image': f"http://127.0.0.1:8000{instance.image.url}"  if instance.image else "",  # Get the URL of the image file
      }
      serialized_instances.append(seriealized_instance)

    return JsonResponse({'featured_instances': serialized_instances})