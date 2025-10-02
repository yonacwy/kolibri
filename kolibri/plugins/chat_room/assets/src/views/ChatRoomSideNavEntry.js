import Kolibri from 'kolibri';
import KolibriModule from 'kolibri_module';
import { ChatRoomNavItem } from '../../kolibri_plugin';

class ChatRoomSideNavEntry extends KolibriModule {
  ready() {
    Kolibri.registerModule(ChatRoomNavItem);
  }
}

export default new ChatRoomSideNavEntry();