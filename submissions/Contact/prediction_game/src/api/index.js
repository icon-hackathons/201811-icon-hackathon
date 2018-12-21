import axios from 'axios'
import _ from 'lodash'
import signer from '../lib/signer'
let callFormat = _.cloneDeep(signer.callFormat)
let sendCallFormat = _.cloneDeep(signer.sendCallFormat)

const questionUrl = 'http://127.0.0.1:3000/inProgress/'
const rpcUrl = "https://bicon.net.solidwallet.io/api/v3/"


export default {
  getQuestions (page) {
    return axios.create({
      baseURL: `${questionUrl}${page}`
    })
  },
  getBalance (address) {
    return axios.create({
      baseURL: `${rpcUrl}`
    })
  },
  getLastBlock () {
    return 
  }
}
