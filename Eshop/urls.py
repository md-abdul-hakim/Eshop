from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
    path('account/', include('account.urls')),
    path('order/', include('order.urls')),
    path('other/', include('other.urls')),
    path('payment/', include('payment.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('notification/', include('notification.urls')),
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)