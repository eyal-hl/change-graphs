<template>
  <div>
    <div class="text-container">
      <v-file-input
        @change="newColors"
        accept="text/plain, .csv, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        label="צבעים חדשים"
      />
      <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-right">שם</th>
          <th class="text-right">ערך</th>
          <th class="text-right">צבע</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(key, value) in colors" :key="key">
          <td>{{ value }}</td>
          <td >{{ key }}</td>
          <td :style="{backgroundColor: '#'+key}"/>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
    </div>
    <div class="row">
    <textarea v-model="colorsText" placeholder="add multiple lines"></textarea>
    <v-btn rounded color="primary" dark @click="changeColors">שנה צבעים</v-btn>
    <v-btn rounded color="primary" dark @click="resetColors">אפס צבעים</v-btn>
    </div>
    </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'

export default {
  name: "Settings",
  data() {
      return {
          colorsText :'',
      }
  },
  mounted(){
    let newColorsText = '';
    Object.keys(this.colors).forEach((color)=>{
      newColorsText += (color + '\t' + this.colors[color] + '\n')
    })
    this.colorsText = newColorsText;
  },
  methods:{
      ...mapActions(['updateColors']),
      resetColors(){
        this.colorsText = `לבן	BFBFBF
ירוק	00B050
כחול	007AC0
שחור	000000
אדום	FF0000
צל	7030A0
צל-בהיר	F2F2F2
סגול	7030A0
`
      },
      newColors(){
          console.log(event.target.files[0])
      },
      changeColors(){
      let newColors = {};
      this.colorsText.split('\n').forEach((line)=> {
        if (line){
          newColors[line.split(/[ |\t]/)[0]] = line.split(/[ |\t]/)[1]||'צל';  
        }
        
        })
      this.updateColors(newColors);
    }

  },
  computed:{
      ...mapState(['colors'])
  }
};
</script>

<style>

</style>