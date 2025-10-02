from django.views.generic import TemplateView

class ChatRoomView(TemplateView):
    template_name = "chat_room/chat_room.html"