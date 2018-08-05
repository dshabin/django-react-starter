from django.conf.urls import url, include
from .views import LoginView,SignupView

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^signup/$', SignupView.as_view()),
    ]
