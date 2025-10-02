const path = require('path');

module.exports = [
  {
    bundle_id: 'main',
    webpack_config: {
      entry: path.resolve(__dirname, 'assets/src/main.js'),
    },
  },
  {
    bundle_id: 'side_nav',
    webpack_config: {
      entry: path.resolve(__dirname, 'assets/src/views/ChatRoomSideNavEntry.js'),
    },
  },
];