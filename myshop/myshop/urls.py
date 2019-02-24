from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from login import views as login_views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),

    url(r'^captcha', include('captcha.urls')) ,
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^log/login',login_views.login),
    url(r'^log/register',login_views.register),
    url(r'^log/logout',login_views.logout),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
