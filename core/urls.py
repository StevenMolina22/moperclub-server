from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import views as home_views
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.index),
    path('users/', include("users.urls")),
    path('events/', include("events.urls")),
    path('products/', include("products.urls")),
    path('places/', include("places.urls")),
    path('establishments/', include("establishments.urls")),
    path('categories/', include("categories.urls")),
    path('blog/', include("blog.urls")),
    path('docs/', include_docs_urls(title = "Docs API")),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
