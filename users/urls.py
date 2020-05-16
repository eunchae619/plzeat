from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path(
        "verify/<str:key>/", views.complete_verification, name="complete_verification"
    ),
]
