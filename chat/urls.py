from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='home'),
    path('accounts/', include('accounts.urls'))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
