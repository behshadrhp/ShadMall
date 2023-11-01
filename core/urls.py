import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import debug_toolbar
from dotenv import load_dotenv

# Loading environment variable's
load_dotenv()

if settings.DEBUG:
    ADMIN_DIRECTORY = os.environ.setdefault('ADMIN_DIRECTORY', 'admin')
else:
    ADMIN_DIRECTORY = os.environ.get('ADMIN_DIRECTORY')

urlpatterns = [
    path(f'{ADMIN_DIRECTORY}/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#  Media static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Debug toolbar
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
