from events.models import Event
from establishments.models import Establishment
from places.models import Place

# this is provisional, to be changed later for a more robust approach with better pk's
def get_featured_instances():
    # get featured instances in each table
    featured_events = Event.objects.filter(is_featured=True)
    featured_establishments = Establishment.objects.filter(is_featured=True)
    featured_places = Place.objects.filter(is_featured=True)
    # make a list out of the queries  
    all_featured_instances = list(featured_events) + list(featured_establishments) + list(featured_places)

    return all_featured_instances

