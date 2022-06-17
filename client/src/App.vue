<template>
  <v-app>
    <v-app-bar
      app
     
      dark
    >
      

      <v-spacer></v-spacer>

      <v-btn class="goto-btn" to="/">בית</v-btn>
      <v-btn class="goto-btn" to="/settings">הגדרות</v-btn>

      <v-spacer></v-spacer>

      
    </v-app-bar>

    <v-content class="container">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  components: {
    
  },

  data: () => ({
    
  }),
  mounted(){
    this.$store.dispatch('checkLocalColors')
  }
};
</script>

<style scoped>
.goto-btn + .goto-btn{
  margin-right: 2vw;
}
</style>
