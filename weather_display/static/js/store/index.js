import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import VueAxios from 'vue-axios';
import qs from 'qs';
import stations from "./api/stations";

Vue.use(Vuex);
Vue.use(VueAxios, axios);
const store = new Vuex.Store({
  modules: {
    stations
  },
});
const $axios = axios.create();
store.$axios = $axios;
const $qs = qs;
store.$qs = $qs;
export default store;
