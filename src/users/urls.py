from django.urls import path

urlpatterns = [
path("login/", LoginView.as_view(), name="login"),
path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
path("logout/", LogoutView.as_view(), name="logout"),
]
