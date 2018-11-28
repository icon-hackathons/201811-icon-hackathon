<template>
    <div class="modal-layout">

        <div class="modal-Question">
            <p>{{ text }}</p>
        </div>

        <div class="Bat-Div">
            <span>배팅금액 1 ICX</span>
        </div>
        
        <div v-if="state === 'on_voting'">
        <!-- if 처리 필요 -->
            <div class="Choice-Div in">
                <span>{{data.items.split(",")[0]}}, </span>
                <span>{{data.items.split(",")[1]}}</span>
            </div>
            
            <div class="inofmration-div in">
                <span>마감 블록 : {{parseInt(data.expire_date.slice(2), 16)}}</span>
                <span>누적 금액 : {{parseInt(data.deposited_icx.slice(2), 16)/(1000000000000000000)}} ICX</span>
            </div>

            <div class="btn-div in">
                <button class="A-Btn" @click='vote(data.items.split(",")[0])'>{{data.items.split(",")[0]}}</button>
                <button class="B-Btn" @click='vote(data.items.split(",")[1])'>{{data.items.split(",")[1]}}</button>
            </div>
        <!-- end if -->
        </div>
        <div v-else-if="state === 'on_counting'">
            <div v-if="data.voter_list.split(',').includes('hx8f4ef11d2df14b66de3a6e5be4be987959287c75')">
               <div class="inofmration-div in">
 
                   <span>누적 금액: {{parseInt(data.deposited_icx.slice(2), 16)/(1000000000000000000)}} ICX</span>
               </div>
               <div class="btn-div in">
                   <button class="A-Btn" @click='count(data.items.split(",")[0])'>{{data.items.split(",")[0]}}(개표)</button>
                   <button class="A-Btn" @click='count(data.items.split(",")[1])'>{{data.items.split(",")[1]}}(개표)</button>
               </div>
            </div>
            <div v-else>
                {{data}}
              <span>누적 금액: {{parseInt(data.deposited_icx.slice(2), 16)/(1000000000000000000)}} ICX</span>
              투표에 참여하시지 않았습니다.
            </div>
        </div>
        <div v-else-if="state === 'ended'">
            <div class="confirm-box">
                <span>를 선택한 사람에게 {{2}} ICX 지급!</span>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import signer from '../../lib/signer'
const sha3_256 = require('js-sha3').sha3_256;
let sendCallFormat = _.cloneDeep(signer.transactionFormat)
    export default {
      name: 'Predict',
      props: ['text', 'state', 'expire_date', 'deposited_icx', 'data' ],
      methods: {
          vote (opt) {
              const one = (1000000000000000000).toString(16)
              sendCallFormat['params']['value'] = `0x${one}`
              sendCallFormat['params']['data']['method'] = "vote_prediction"
              const hashed_data = `${signer.scoreAddress}${signer.eoa}${opt}0`
              const msgHash = sha3_256.update(hashed_data).hex();
              sendCallFormat['params']['data']['params'] = {"prediction_num": this.data.prediction_num, "hashed_vote": msgHash}
              signer.putsig(sendCallFormat, "b8a8d198a65335be9c599e9b0f8837872cc744960ba7b24801c01825ddcadfde")
              axios.post(signer.biconUrl, sendCallFormat, {headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}).then((result) => {
                  console.log(result.data)
                  }).
                  catch((reaseon)=>{console.log(reason)})
              },
          count (opt) {
              sendCallFormat['params']['value'] = '0x0'
              sendCallFormat['params']['data']['method'] = "validate_vote"
              sendCallFormat['params']['data']['params'] = {"prediction_num": this.data.prediction_num, "item": opt, "nonce": "0x0"}
              console.log("ddddd")
              console.log(sendCallFormat)
              signer.putsig(sendCallFormat, "b8a8d198a65335be9c599e9b0f8837872cc744960ba7b24801c01825ddcadfde")
              axios.post(signer.biconUrl, sendCallFormat, {headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}).then((result) => {
                  console.log(result.data)
                  }).
                  catch((reaseon)=>{console.log(reason)})
          }
          },
          
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