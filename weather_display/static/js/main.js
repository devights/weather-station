import Vue from 'vue';
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue';
import VueRouter from 'vue-router';
import VuePluralize from 'vue-pluralize';
import VueMoment from 'vue-moment';
import moment from 'moment-timezone';

import App from "./App.vue";
import Admin from "./pages/admin.vue";
import store from './store';

// import the bootstrap / bootstrap-vue base css
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

const debugMode = $("body").data("django-debug");

Vue.use(VueRouter);
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VuePluralize);
Vue.use(VueMoment, {moment});

export const EventBus = new Vue();

var router = new VueRouter({
  mode: "history",
  routes: [
    { path: '/', component: Admin }
  ]
});


// vue app will be rendered inside of #main div found in index.html using webpack_loader
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#main");
