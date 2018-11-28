<template>
<header class="Rectangle-header">
  <div class="inner-div">
    
    <div class="inline" style="margin-left: 4%" >
      <span class="Oval">
        <span class="Man"></span>
      </span>

      <span class="Address">Address : hx1234567890abcdef1234567890abcdef12345678
      </span>
      
      <span class="Balance">Balance: {{parseInt(balance, 16)/1000000000000000000}} ICX</span>
      <span class="Balance">lastBlock: {{lastBlock}} ICX</span>
    </div>

    <div class="inline" style="float: right; margin-right: 4%; width: 270px;">
      <div class="inline_block" style="margin-right: 4%">
        <select class="Selector" @change="changeFilter(select)" v-model="select">
          <option value="all">전체</option>
          <option value="voted">투자한방 리스트</option>
          <option value="own">내가 개설한 방</option>
          <option value="ended">종료</option>
        </select>
      </div>

      <div @click="createModal($event)" class="login-btn inline_block">
        <span>주제 등록하기</span>
      </div>
    
    </div>
  </div>

</header>
</template>

<script>
import Create from './modal/Create.vue'
import axios from 'axios'
import signer from '../lib/signer'

import _ from 'lodash'

let callFormat = _.cloneDeep(signer.callFormat)

export default{
  name: 'Header',
  methods: {
    submitPrediction () {
      sendCallFormat['params']['data']['method'] = method
      sendCallFormat['params']['data']['params'] = params
    },
    createModal (event) {
      this.$modal.show(Create, {
        text: "dd",
        status: "init"
        }, {
          draggable: true
          }
        )
    },
    changeFilter (option) {
      console.log(option)
      const address = "hx8f4ef11d2df14b66de3a6e5be4be987959287c75"
      callFormat['params']['data']['params'] = {"address": address}
      if(this.select=="voted"){
        callFormat['params']['data']['method'] = "getPredictionsByVoter"
      }else if(this.select=="own"){
        callFormat['params']['data']['method'] = "getPredictionsByOwner"
      }else if(this.select=="ended"){
        callFormat['params']['data']['method'] = "getPredictionsByState"
        callFormat['params']['data']['params'] = {"state": "ended"}
      }else{
        callFormat['params']['data']['method'] = "getPredictions"
        callFormat['params']['data']['params'] = {}
      }
      axios.post(signer.biconUrl, callFormat, {headers: { 'Content-Type': 'application/x-www-form-urlencoded'}})
      .then((result)=>{
        this.$store.state.questions.questions = result.data.result.reverse()
        }).catch((reason)=>{console.log(reason)})
    }
  },
  created () {
    let reqArr = []
    reqArr.push(axios.post(signer.biconUrl, signer.getBalance,{headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}))
    reqArr.push(axios.post(signer.biconUrl, signer.getLastBlock,{headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}))
    
    axios.all(reqArr).then(axios.spread((balanceRes, blockRes) => { 
      this.$store.state.questions.lastBlock = blockRes.data.result.height
      this.$store.state.account.balance = balanceRes.data.result
      console.log(balanceRes.data.result)
    })).catch((error) => {
        console.error(error)
    })
  },
  computed: {
    lastBlock () {
      return this.$store.state.questions.lastBlock
    },
    balance () {
      return this.$store.state.account.balance
    }
  },
  data : function() {
    return {
      select: this.$store.state.questions.status
    }
    }
    }
</script>

<style>
  .Rectangle-header {
    width: 100%;
    height: 56px;
    background-color: #1e1e1e;
    padding-top: 13px;
    text-align: left;
  }

  .Oval {
    width: 30px;
    height: 30px;
    background-color: #ffffff;

    margin-left: 54px;
  }

  .Man {
    width: 26px;
    height: 26px;
  }

  .Address {
    width: 160px;
    height: 17px;
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #ffffff;

    margin-right: 28px;
  }

  .Balance {
    width: 148px;
    height: 17px;
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #ffffff;
  }

  .user-123 {
    width: 58px;
    height: 17px;
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #ffffff;
  }

  .login-btn {
    width: 96px;
    height: 26px;
    border-radius: 4px;
    background-color: #878787;

    text-align: center;
  }

  .Selector {
    width: 140px;
    height: 26px;
    border-radius: 4px;
    background-color: #ffffff;
  }

  .login-btn span{
    font-family: AppleSDGothicNeo;
    font-size: 14px;
    font-weight: bold;
    font-style: normal;
    font-stretch: normal;
    line-height: normal;
    letter-spacing: normal;
    color: #ffffff;

    line-height: 26px;
    vertical-align: middle;
  }

  .inline_block {
    display: inline-block;
  }

  .inline {
    display: inline;
  }
</style>
