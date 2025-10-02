import os
import sys

# Add the current workspace directory to the Python path
sys.path.insert(0, os.path.abspath('.'))

# Set KOLIBRI_HOME to ensure Kolibri finds its configuration
os.environ.setdefault("KOLIBRI_HOME", os.path.join(os.path.expanduser("~"), ".kolibri"))

# Set KOLIBRI_DEVELOPER_MODE to True
os.environ.setdefault("KOLIBRI_DEVELOPER_MODE", "True")

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kolibri.deployment.default.settings.base")

import django
django.setup()

# Import and enable the plugin
from kolibri.plugins.utils import enable_plugin

plugin_name = "kolibri.plugins.chat_room"
print(f"Attempting to enable plugin: {plugin_name}")
success = enable_plugin(plugin_name, initialize_hooks=True)

if success:
    print(f"Plugin '{plugin_name}' enabled successfully.")
else:
    print(f"Failed to enable plugin '{plugin_name}'.")