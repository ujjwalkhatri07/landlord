
from Rooms import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

from django.urls import path, include

urlpatterns=[
    path('',views.show_room),
    path('new',views.show_new)
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)