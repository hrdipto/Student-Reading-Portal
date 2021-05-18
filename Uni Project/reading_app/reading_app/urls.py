from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('classrooms/', include('classrooms.urls'), name="home"),
    # path('about/', views.about),
    path('', include('accounts.urls')),

    path('api/v1/classrooms/', include('restclassrooms.urls')),
    path('api/v1/accounts/', include('restaccounts.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)