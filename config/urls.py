from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('src.main.urls')),

    path('cart/', include(('src.cart.urls', 'src.cart'), namespace='cart')),
    path('shop/', include(('src.shop.urls', 'src.shop'), namespace='shop')),
]

if settings.DEBUG:
    urlpatterns = [
                      path('__debug__/', include('debug_toolbar.urls')),
                  ] + urlpatterns
    # urlpatterns += static(settings.MEDIA_URL,
    #                       document_root=settings.MEDIA_ROOT)
