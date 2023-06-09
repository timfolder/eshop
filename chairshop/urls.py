from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="first_screen.html"), name = "home"),
    path('gallery/', include('chairitems.urls')),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
