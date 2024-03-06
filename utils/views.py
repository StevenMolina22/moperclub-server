# views.py
from django.http import JsonResponse
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
          'image': instance.image.url if instance.image else None,  # Get the URL of the image file
      }
      serialized_instances.append(seriealized_instance)

    return JsonResponse({'featured_instances': serialized_instances})