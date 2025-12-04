from django.urls import path
from .views import (
    notice_list,
    notice_detail,
    notice_create,
    notice_update,
    notice_delete,
)

urlpatterns = [
    # URL pattern for displaying a list of all notices
    path("", notice_list, name="notice_list"),

    # URL pattern for displaying details of a specific notice
    path("notice/<int:pk>/", notice_detail, name="notice_detail"),

    # URL pattern for creating a new notice
    path("notice/new/", notice_create, name="notice_create"),

    # URL pattern for updating an existing notice
    path("notice/<int:pk>/edit/", notice_update, name="notice_update"),

    # URL pattern for deleting an existing notice
    path("notice/<int:pk>/delete/", notice_delete, name="notice_delete"),
]
