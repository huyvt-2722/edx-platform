"""
Learner Home URL routing configuration
"""

from django.urls import path
from django.urls import include, re_path

from lms.djangoapps.learner_home import views

app_name = "learner_home"

# Learner Dashboard Routing
urlpatterns = [
    re_path(r"^init/?", views.InitializeView.as_view(), name="initialize"),
    path("mock/", include("lms.djangoapps.learner_home.mock.urls")),
]
