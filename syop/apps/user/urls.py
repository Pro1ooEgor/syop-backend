from django.urls import path, re_path

from .views import AuthorRegisterView, LoginView, LogoutView, CheckUniqueEmail, CheckUniqueUsername, CheckToken

urlpatterns = [
    path('register/', AuthorRegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    re_path('logout/(?P<author_id>\d+)/$', LogoutView.as_view(), name="logout"),
    path('checkToken/', CheckToken.as_view(), name="check_token"),
    path('checkEmail/', CheckUniqueEmail.as_view(), name="check_unique_email"),
    path('checkUsername/', CheckUniqueUsername.as_view(), name="check_unique_username"),
]
