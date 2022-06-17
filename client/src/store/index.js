import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    colors: {
      'לבן': "BFBFBF",
      'ירוק': "00B050",
      'כחול': "007AC0",
      'שחור': "000000",
      'אדום': "FF0000",
      'צל': "7030A0",
      'צל-בהיר': "F2F2F2",
      'סגול': "7030A0"
    },
  },
  mutations: {
    updateColors(state, colors){
      state.colors = colors;
    }
  },
  actions: {
    updateColors({commit}, colors){
      commit('updateColors', colors);
      localStorage.colors = JSON.stringify(colors);
    },
    checkLocalColors({commit}){
      let colors = localStorage.colors;
      if (colors){
        commit('updateColors', JSON.parse(colors))
      }
    }
  },
  modules: {
  }
})
