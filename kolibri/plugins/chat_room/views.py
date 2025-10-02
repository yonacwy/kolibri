from kolibri.core.webpack.utils import webpack_asset
from kolibri.plugins.base import KolibriPluginBase
from django.views.generic.base import TemplateView


class ChatRoomView(TemplateView):
    template_name = "chat_room/chat_room.html"

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context["webpack_url"] = webpack_asset("chat_room_module", "app")
        return context