from kolibri.core.auth.constants.user_kinds import COACH
from kolibri.core.hooks import NavigationHook
from kolibri.core.webpack import KolibriPluginBase
from kolibri.plugins.hooks import register_hook
from kolibri.core.urls import reverse as url_reverse
from . import urls

class ChatRoom(KolibriPluginBase):
    bundle_id = "main"
    url_slug = "chat_room"
    translated_view_urls = "urls"
    navigation_url = "/chat_room/"

@register_hook
class ChatRoomNavItem(NavigationHook):
    bundle_id = "side_nav"
    roles = (COACH,)

    @property
    def menu_spec(self):
        return [
            {
                "url": url_reverse("kolibri.plugins.chat_room:chat_room"),
                "text": "Chat Room",
                "icon": "chat",
                "category": "coach",
            },
        ]