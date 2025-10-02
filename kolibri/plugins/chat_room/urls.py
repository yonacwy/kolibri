from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.ChatRoomView.as_view(), name="chat_room"),
]