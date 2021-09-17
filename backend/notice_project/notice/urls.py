from django.urls import path
<<<<<<< HEAD
from .views import install, sidebar, CreateNewNotices, NoticeAPI, UpdateNoticeAPIView, DeleteNotice, search
=======
from .views import install,sidebar, create_room, CreateNewNotices, search, get_room
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
>>>>>>> 1a859a53a498550d1f4a5b9b770414dea004d3d1



schema_view = get_schema_view(
   openapi.Info(
      title="Noticeboard API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   
   path('sidebar', sidebar, name="sidebar"),

   path('install',install, name='install'),

<<<<<<< HEAD
    path('install', install, name='install'),
=======
   path('create-notice-room', create_room),
>>>>>>> 1a859a53a498550d1f4a5b9b770414dea004d3d1

   path('create-notice', CreateNewNotices.as_view()),

   path('search', search.as_view()),

   path('get-room', get_room),

   path('docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
