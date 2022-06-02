<script>
export default {
  data() {
    return {
      datarow: {},
      radiochecked:'-1',
      timuhao:1,
      defen:0,
    };
  },
  methods: {
    getini() {
      this.axios
        .get("http://192.168.108.155:8000/",
          {
            params: {
              timuhao: this.timuhao,
            }
          })
        .then((response) => {
          console.log(response.data);
          this.datarow = response.data;
          this.getmixxuanxiang(this.datarow.xuanxiang1, this.datarow.xuanxiang2, this.datarow.xuanxiang3, this.datarow.xuanxiang4, this.datarow.xuanxiang5,this.datarow.xuanxiang6,this.datarow.xuanxiang7,this.datarow.daan);
          this.radiochecked=-1;
        })
        .catch((error) => {
          console.log(error);
        });

        if((this.datarow.daan!==this.radiochecked)&&(this.datarow.daan!==undefined))
          {
            if(this.datarow.daan=='A')
            {
              var key=this.datarow.xuanxiang1
            }
            else if(this.datarow.daan=='B')
            {
             var key=this.datarow.xuanxiang2
            }
            else if(this.datarow.daan=='C')
            {
             var key=this.datarow.xuanxiang3
            }
            else if(this.datarow.daan=='D')
            {
             var key=this.datarow.xuanxiang4
            }
            else if(this.datarow.daan=='E')
            {
              var key=this.datarow.xuanxiang5
            }
            else if(this.datarow.daan=='F')
            {
             var key=this.datarow.xuanxiang6
            }
            else if(this.datarow.daan=='G')
            {
             var key=this.datarow.xuanxiang7
            }
            else
            {
             var key=this.datarow.daan
            }
             alert("答案是:  "+key);
          }
         
        if(this.datarow.daan===this.radiochecked)
          this.defen=this.defen+1;
        if(this.timuhao>100)
          alert("您的得分是"+this.defen);
        this.timuhao++;
    },

    getmixxuanxiang(xuanxiang1,xuanxiang2,xuanxiang3,xuanxiang4,xuanxiang5,xuanxiang6,xuanxiang7,daan)
    {
      if(daan==='A')
      {
        daan=xuanxiang1;
      }
      if(daan==='B')
      {
        daan=xuanxiang2;
      }
      if(daan==='C')
      {
        daan=xuanxiang3;
      }
      if(daan==='D')
      {
        daan=xuanxiang4;
      }
      if(daan==='E')
      {
        daan=xuanxiang5;
      }
      if(daan==='F')
      {
        daan=xuanxiang6;
      }
      if(daan==='G')
      {
        daan=xuanxiang7;
      }
      var mixarray=[xuanxiang1,xuanxiang2,xuanxiang3,xuanxiang4,xuanxiang5,xuanxiang6,xuanxiang7];
      var mixarraynew=mixarray.sort(function(){
        return Math.random()-0.5;
      });
      if(daan===mixarraynew[0])
      {
        daan='A';
      }
      if(daan===mixarraynew[1])
      {
        daan='B';
      }
      if(daan===mixarraynew[2])
      {
        daan='C';
      }
      if(daan===mixarraynew[3])
      {
        daan='D';
      }
      if(daan===mixarraynew[4])
      {
        daan='E';
      }
      if(daan===mixarraynew[5])
      {
        daan='F';
      }
      if(daan===mixarraynew[6])
      {
        daan='G';
      }
      this.datarow.xuanxiang1=mixarraynew[0];
      this.datarow.xuanxiang2=mixarraynew[1];
      this.datarow.xuanxiang3=mixarraynew[2];
      this.datarow.xuanxiang4=mixarraynew[3];
      this.datarow.xuanxiang5=mixarraynew[4];
      this.datarow.xuanxiang6=mixarraynew[5];
      this.datarow.xuanxiang7=mixarraynew[6];
      this.datarow.daan=daan;
    },
    
  },
  mounted() {
    console.log("created");
    this.getini();
  },
};
</script>
<template>

<div class="container">
<div class="row" >
  
  <div class="col">
  <h3 class="float-end">第{{this.timuhao-1}}题</h3>
  </div>
  <h3>{{ this.datarow.tigan }}</h3>
</div>

<div class="form-check" id='A' v-if="(this.datarow.xuanxiang1==null)&&(this.datarow.xuanxiang2==null)&&(this.datarow.xuanxiang3==null)&&(this.datarow.xuanxiang4==null)&&(this.datarow.xuanxiang5==null)&&(this.datarow.xuanxiang6==null)&&(this.datarow.xuanxiang7==null)"><h3><label class="form-check-label"><input  class="form-check-input" name="xuanxinang" v-model="radiochecked" type="radio" value="对" />正确 </label></h3> </div>
<div class="form-check" id='B' v-if="this.datarow.xuanxiang1!==null"><h3><label  class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="A"  class="form-check-input"/>{{this.datarow.xuanxiang1}} </label> </h3></div>
<div class="form-check" id='C' v-if="(this.datarow.xuanxiang1==null)&&(this.datarow.xuanxiang2==null)&&(this.datarow.xuanxiang3==null)&&(this.datarow.xuanxiang4==null)&&(this.datarow.xuanxiang5==null)&&(this.datarow.xuanxiang6==null)&&(this.datarow.xuanxiang7==null)"><h3><label class="form-check-label"><input  class="form-check-input" name="xuanxinang" v-model="radiochecked" type="radio" value="错" />错误 </label></h3> </div>
<div class="form-check" id='D' v-if="this.datarow.xuanxiang2!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="B"  class="form-check-input"/>{{this.datarow.xuanxiang2}} </label></h3> </div>
<div class="form-check" id='E' v-if="this.datarow.xuanxiang3!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="C" class="form-check-input"/>{{this.datarow.xuanxiang3}} </label> </h3></div>
<div class="form-check" id='F' v-if="this.datarow.xuanxiang4!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="D" class="form-check-input"/>{{this.datarow.xuanxiang4}} </label> </h3></div>
<div class="form-check" id='G' v-if="this.datarow.xuanxiang5!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="E" class="form-check-input"/>{{this.datarow.xuanxiang5}} </label> </h3></div>
<div class="form-check" id='H' v-if="this.datarow.xuanxiang6!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="F" class="form-check-input"/>{{this.datarow.xuanxiang6}} </label> </h3></div>
<div class="form-check" id='I' v-if="this.datarow.xuanxiang7!==null"><h3><label class="form-check-label"><input name="xuanxinang" v-model="radiochecked" type="radio"  value="G" class="form-check-input" />{{this.datarow.xuanxiang7}} </label> </h3></div>

<div class="row">
 
<center><button  type="button" class="btn btn-primary btn-group-justfied   row" @click="getini">下一题</button></center> 

</div>
</div>

</template>
