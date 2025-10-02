from __future__ import absolute_import, print_function, unicode_literals

from kolibri.core.webpack import hooks as webpack_hooks
from kolibri.plugins.base import KolibriPluginBase


class ChatRoomAsset(webpack_hooks.WebpackBundleHook):
    unique_slug = "chat_room_module"
    src_file = "assets/src/app.js"


class ChatRoomPlugin(KolibriPluginBase):
    unqiue_slug = "chat_room"
    default_enabled = True

    class KolibriFrontend(KolibriPluginBase.KolibriFrontend):
        webpack_bundle_hooks = [ChatRoomAsset]