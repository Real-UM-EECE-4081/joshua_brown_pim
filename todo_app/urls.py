from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/",views.ItemListView.as_view(), name="list"),
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    path("list/<int:pk>/delete/", views.ListDelete.as_view(), name="list-delete"),
    path("list/<int:list_id>/item/add/",views.ItemCreate.as_view(), name="item-add"),
    path("list/<int:list_id>/item/<int:pk>/",views.ItemUpdate.as_view(),name="item-update"),
    path("list/<int:list_id>/item/<int:pk>/delete/",views.ItemDelete.as_view(),name="item-delete"),
    #path('upload/', views.image_upload_view)
    #path('admin/', admin.site.urls),
]

static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)