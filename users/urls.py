from django.conf.urls import url

from .views import UsersView

urlpatterns = [
    url(r'^$', UsersView.as_view())
]
