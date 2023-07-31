from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from . import otchet

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('oks/', views.oks, name='oks'),
    path('otchet/', otchet.docx, name='otchet'),
    # path('exportcsv', views.exportcsv, name='exprort'),
    path('update-data/<int:id>/', views.update_data, name='update_data'),
    path('get-max-values/', views.get_max_values, name='get-max-values'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)