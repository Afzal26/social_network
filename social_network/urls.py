from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('', include('api.accounts.urls')),
    path('', include('api.credits.urls')),
    path('', include('api.posts.urls')),
    path('', include('api.private_messages.urls')),
    path('', include('api.replies.urls')),
    path('', include('api.user_roles.urls')),
    path('', include('api.votes.urls')),

    # Core
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
