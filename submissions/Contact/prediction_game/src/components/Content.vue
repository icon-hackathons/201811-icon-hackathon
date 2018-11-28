<template>
<v-app>
  <v-layout>
    <v-flex>
      <v-card>
        <v-card-actions>
          <v-spacer></v-spacer>
        </v-card-actions>
        <v-container v-bind="{ [`grid-list-${size}`]: true }" fluid>
          <v-layout row wrap>
            <v-flex
              v-for="(item, index) in dataArr"
              :key="item.id"
            >
              <v-card flat tile>

                <div class="Card-Style">
                  <div class="QABQAB-A">
                    주제 : {{item.subject}}(주제 번호 : {{parseInt(item.prediction_num, 16)}})(16진수 : {{item.prediction_num}})
                  </div>
                  <div class="Bat-div">
                    배팅금액 1 ICX
                  </div>

                  <div>
                    <span class="Duration">마감 블록 : {{ parseInt(item.expire_date.slice(2), 16) }}</span>
                    <span class="Cumulative">누적금액 {{ parseInt(item.deposited_icx.slice(2),16)/1000000000000000000 }}ICX</span>
                  </div>
                  <br />

                  <div class="Join-Btn">
                    <button @click="predict($event, index)"><span>참가하기</span></button>
                  </div>
                </div>

              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
      </v-card>
    </v-flex>
  </v-layout>
</v-app>
</template>

<script>
import api from '../api'
import Predict from './modal/Predict.vue'

import axios from 'axios'
import _ from 'lodash'
import signer from '../lib/signer'
let callFormat = _.cloneDeep(signer.callFormat)

export default {
  name: 'Content',
  data: () => ({
    size: 'xl'
  }),
  created () {
    callFormat["params"]['data']['method'] = 'getPredictions'
    callFormat["params"]['data']['params'] = {}
    axios.post(signer.biconUrl, callFormat, {headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}).then((result) => {
      this.$store.state.questions.questions = result.data.result.reverse()
      }).catch((reaseon)=>{console.log(reason)})
  },
  computed: {
    dataArr () {
      return this.$store.state.questions.questions
    }
  },
  methods: {
    predict (event, index) {
      this.$modal.show(Predict, {
        data: this.$store.state.questions.questions[index],
        text: this.$store.state.questions.questions[index]["subject"],
        expire_date: this.$store.state.questions.questions[index]["expire_date"],
        deposited_icx: this.$store.state.questions.questions[index]["deposited_icx"],
        state: this.$store.state.questions.questions[index]["state"]
        },
        {
          height: 'auto'
        }
        ,{
          draggable: true
          }
          )
    }
  }
}
</script>

<style>
  .Card-Style {
    width: 257px;
    height: 222px;
    background-color: #ffffff;

    border: 1px solid #979797;
    padding: 12px;
  }

  .QABQAB-A {
    width: 233px;
    height: 53%;
    font-family: AppleSDGothicNeo;
    font-size: 20px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #333333;

    text-align: left;
  }

  .Bat-div {
    width: 100%;
    height: 19px;
    font-family: AppleSDGothicNeo;
    font-size: 16px;
    font-weight: 800;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #404040;
    
    text-align: right;

    margin-bottom: 8px;
  }

  .Duration {
    width: 57px;
    height: 17px;
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: normal;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #404040;
    float: left;
  }

  .Cumulative {
    width: 153px;
    height: 17px;
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: normal;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #404040;
    float: right;
  }

  .Join-Btn {
    width: 100%;
    height: 40px;
    border-radius: 4px;
    background-color: #818181;
  }

  .Join-Btn Span {
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    letter-spacing: normal;
    color: #ffffff;

    /*참가하기 글을 맞추기 위하여, Join-Btn과 동일한 height 정보를 줘야함*/
    line-height: 40px;
    vertical-align: middle;
  }

</style>
