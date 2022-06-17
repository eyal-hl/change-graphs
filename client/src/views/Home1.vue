<template>
  <div>
    <v-file-input accept="image/*" @change="uploadImage" id="file-input" label="הכנס תמונה"/>
    <img v-if="previewImage" :src="previewImage" />
    <br />
    <div class="row">
      <v-btn rounded color="primary" dark @click="changeImage">לחץ כאן</v-btn>
      <v-spacer />
      <div class="text-container">
        <v-text-field label="עובי הקו" :rules="rules" v-model="height" placeholder="עובי הקו"></v-text-field>
      </div>
      <div class="text-container">
        <v-text-field label="עובי הצל" :rules="rules" v-model="shadowSize" placeholder="עובי הצל"></v-text-field>
      </div>
      <div class="text-container">
        <!-- <v-file-input @change="updateLevel" accept="text/plain, .csv, .prn, application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" label="קושי"/> -->
        <textarea v-model="levelText" placeholder="add multiple lines"></textarea>
      </div>
    </div>
      <thead>
        <tr>
          <th class="text-right">מיקום</th>
          <th class="text-right">צבע</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(key, value) in level" :key="value">
          <td>{{ value }}</td>
          <td >{{ key }}</td>
        </tr>
      </tbody>
 
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
import {mapState} from "vuex"

export default {
  name: "Home",
  data() {
    return {
      previewImage: null,
      originalImage: null,
      
      height:35,
      shadowSize: 4,
      levelText:"",
      exampleLevel:{
       0	: 'לבן',
0.3	: 'כחול',
0.44	: 'כחול',
0.6	: 'לבן',
1.04	: 'לבן',
1.56	: 'לבן',
2.05	: 'לבן',
2.95	: 'לבן',
3.25	: 'לבן',
4.4	: 'לבן',
6.25	: 'כחול',
6.85	: 'כחול',
7.94	: 'לבן',
8.85	: 'ירוק',
9.16	: 'ירוק',
9.34	: 'לבן',
9.67	: 'לבן',
10.22	: 'ירוק',
11.26	: 'כחול',
11.35	: 'ירוק',
12.2	: null

      },
      rules: [
        value => !!value || "Required.",
        value => {
          const pattern = /^[\d|.]+$/;
          return pattern.test(value) || "Invalid number.";
        }
      ]
    };
  },
  computed: {
    ...mapState(['colors']),
    colorsFormatted(){
      let newColors = {};
      let level = {...this.level}
      level[Math.max.apply(null,Object.keys(level))] = 'צל'
      Object.keys(level).forEach(key => newColors[key] = this.colors[level[key]])
      return newColors
    },
    validInputs(){
      let errorMessage = ""
      if (!this.originalImage){
        errorMessage += "בעיה בתמונה\n"
      }
      if (!this.level){
        errorMessage += "בעיה בקובץ הקושי\n"
      }
      if (Object.values(this.colorsFormatted).includes(undefined)){
        errorMessage += "יש צבע בטבלת הקושי שלא קיים בטבלת הצבעים"
      }
      return errorMessage
    },
    level(){
      let newLevel = {};
      this.levelText.split('\n').forEach((line)=> {
        if (line){
          newLevel[line.split(/[ |\t]/)[0].includes('.')?line.split(/[ |\t]/)[0]:line.split(/[ |\t]/)[0]+'.0'] = line.split(/[ |\t]/)[1]||'צל';  
        }
        
        })
      return newLevel
    }
  },
  methods: {
    uploadImage() {
      const image = event.target.files[0];
      const reader = new FileReader();
      reader.readAsDataURL(image);
      reader.onload = e => {
        this.previewImage = e.target.result;
        this.originalImage = e.target.result;
      };
    },
    updateLevel(){
      console.log(event.target.files[0])
      
    },
    changeImage() {
      if (this.validInputs){
        alert(this.validInputs)
      }
      else{

      
      axios
        .post(`/api/image`, {
          body: {
            width: +this.height,
            shadowSize: +this.shadowSize,
            colors: this.colorsFormatted,
            image: this.originalImage,
          }
        })
        .then(({ data }) => (this.previewImage = data));}
    }
  }
};
</script>

<style scoped>
.text-container{
  width: 10vw;
  margin-left: 3vw;
}
</style>