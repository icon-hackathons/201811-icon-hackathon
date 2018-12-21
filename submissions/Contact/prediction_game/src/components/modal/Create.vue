<template>
    <div class="modal-layout">

        <div class="modal-Question">
            <p>주제 등록 하기</p>
        </div>
        
            <div class="Choice-Div in">
                <input v-model="subject" placeholder="주제">
                <input v-model="items" placeholder="항목(쉼표로 구분)">
                <input v-model="description" placeholder="설명">
            </div>

            <div class="btn-div in">
                <button class="A-Btn" @click="createPrediction">등록</button>
            </div>
    </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import signer from '../../lib/signer'
let sendCallFormat = _.cloneDeep(signer.transactionFormat)

    export default {
      name: 'Predict',
      props: ['text', 'status'],
      methods: {
        createPrediction () {
          sendCallFormat['params']['data']['method'] = "submit_prediction"
          sendCallFormat['params']['data']['params'] = {"subject": this.subject, "items": this.items, "description": this.description}
          signer.putsig(sendCallFormat, "b8a8d198a65335be9c599e9b0f8837872cc744960ba7b24801c01825ddcadfde")
          axios.post(signer.biconUrl, sendCallFormat, {headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}).then((result) => {
            console.log(result.data)
            }).catch((reaseon)=>{
              console.log(reason)})
            }
      },
      data : function() {
          return {
              subject: document.getElementById('subject'),
              items: document.getElementById('items'),
              description: document.getElementById('description')
          }
      }
    }
</script>

<style>
    .modal-layout {
        text-align: center;
    }

    .modal-Question {
      height: 66px;
      font-family: AppleSDGothicNeo;
      font-size: 28px;
      font-weight: bold;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      text-align: center;
      color: #333333;

      margin-top: 30px;
    }

    .Bat-Div {
      width: 235px;
      height: 58px;
      border-radius: 4px;
      background-color: #d8d8d8;

      display: inline-block;
      margin-bottom: 24px;
    }

    .Bat-Div span {
      width: 138px;
      height: 24px;
      font-family: AppleSDGothicNeo;
      font-size: 20px;
      font-weight: 800;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      color: #404040;

      line-height: 58px;
      vertical-align: middle;

    }

    .Choice-Div {
      height: 33px;

      margin-bottom: 1%;

      font-family: AppleSDGothicNeo;
      font-size: 28px;
      font-weight: bold;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      color: #333333;
    }

    .inofmration-div {
      width: 100%;
      font-family: AppleSDGothicNeo;
      font-size: 20px;
      font-weight: normal;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      color: #404040;

      margin-top: 30px;
      margin-bottom: 15px;
    }

    .A-Btn {
      width: 100px;
      height: 56px;
      border-radius: 4px;
      background-color: #818181;
    }

    .B-Btn {
      width: 100px;
      height: 56px;
      border-radius: 4px;
      background-color: #484848;
    }

    .btn-div button{
      font-family: AppleSDGothicNeo;
      font-size: 14px;
      font-weight: bold;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      text-align: center;
      color: #ffffff;

      margin-left: 10px;
      margin-right: 10px;
    }

    .confirm-box {
      width: 390px;
      height: 53px;
    
      display: inline-block;
      
      border-radius: 4px;
      background-color: #d8d8d8;
    }

    .confirm-box span{
      font-family: AppleSDGothicNeo;
      font-size: 20px;
      font-weight: normal;
      font-style: normal;
      font-stretch: normal;
      line-height: normal;
      letter-spacing: normal;
      color: #404040;

      line-height: 53px;
      vertical-align: center;
    }

    .in {
        display: inline-block;
        width: 100%;
    }
</style>