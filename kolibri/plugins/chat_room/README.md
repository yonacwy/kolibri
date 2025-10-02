# Kolibri Chat Room Plugin

A basic plugin for adding a chat room feature to Kolibri.

## Installation

1. `pip install -e .` (from the plugin directory)
2. In Kolibri: `kolibri manage enableplugin chat_room`
3. `kolibri manage migrate`
4. Restart Kolibri.

## Development

- Run `kolibri devserver --plugin chat_room` to build/watch frontend.
- Access via a custom URL or hook it into Kolibri's navigation (extend `NavigationHook` in kolibri_plugin.py).

For more, see [Kolibri Plugin Architecture](https://kolibri-dev.readthedocs.io/en/develop/backend_architecture/plugins.html).