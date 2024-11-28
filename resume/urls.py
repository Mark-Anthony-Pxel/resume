from django.urls import path, include
from django.conf import settings
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('app.urls')),
]