from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include("apps.bookmodule.urls")), # تضمين مسارات bookmodule
    path('users/', include("apps.usermodule.urls"))  # تضمين مسارات usermodule
]