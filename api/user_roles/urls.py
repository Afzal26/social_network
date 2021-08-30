from django.urls import path

from .views.administrator import AdministratorView
from .views.moderator import ModeratorView, ModeratorDetail

urlpatterns = [

    # Administrators
    path('administrators', AdministratorView.as_view()),

    # Moderators
    path('moderators', ModeratorView.as_view()),
    path('moderators/<moderator_id>', ModeratorDetail.as_view()),

]
