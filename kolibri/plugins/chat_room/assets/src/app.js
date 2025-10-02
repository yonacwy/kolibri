import Vue from 'vue';
import VueRouter from 'vue-router';
import routes from './routes';
import ChatRoomPage from './views/ChatRoomPage';

Vue.use(VueRouter);

const router = new VueRouter({
  routes,
});

new Vue({
  el: 'body',
  router,
  render: h => h(ChatRoomPage),
});