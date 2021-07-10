const state = {
  stations: []
};

// getters
const getters = {
  stations: state => {
    return state.stations;
  }
};

// actions
const actions = {
  get_stations ({ commit }) {
    this.$axios.get(`/api/stations/`)
      .then(response => response.data)
      .then(items => {
        commit('set_stations', items);
      });
  },
  add_station ({ commit }, station) {
    commit('add_station', station);
  }
};

// mutations
const mutations = {
  set_stations (state, stations) {
    state.stations = stations.results;
  },
  add_station(state, station) {
    state.stations.push(station)
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
