import { createStore, applyMiddleware } from 'redux'
import { composeWithDevTools } from 'redux-devtools-extension'
import thunkMiddleware from 'redux-thunk'

const initialState = {
  weddingInformation: {
    groom_name: '송화중',
    groom_father_name: '송병현',
    groom_mother_name: '정영옥',
    bride_name: '성지영',
    bride_father_name: '성용호',
    bride_mother_name: '신학심',
    wedding_date: '1542787020385000',
    wedding_date_str: '2017년 8월 16일 오후 2시',
    wedding_place_name: '헤레이스',
    wedding_place_address: '서울 영등포구 당산동3가 81',
    invitation_message: '서로가 마주보며 다져온 사랑을\n이제 함께 한 곳을 바라보며\n걸어갈 수 있는 큰 사랑으로\n키우고자 합니다.\n저희 두 사람이 사랑의 이름으로\n지켜나갈 수 있게\n앞 날을 축복해주시면\n감사하겠습니다.',
    wedding_photo_url: 'https://pds.joins.com//news/component/htmlphoto_mmdata/201711/02/a7e52ac4-168e-4c9a-a31d-a0b206b53a6d.jpg',
  },
  mealTicketCount: 100,
  encryptionKey: '',
}

export const actionTypes = {
  initStore: 'initStore',
  setWeddingInformation: 'setWeddingInformation',
  setMealTicketCount: 'setMealTicketCount',
  setEncryptionKey: 'setEncryptionKey'
}

export const reducer = (state = initialState, action) => {
  switch (action.type) {
    case actionTypes.initStore:
      return initialState
    case actionTypes.setWeddingInformation:
      const weddingInformation = { ...initialState.weddingInformation }
      Object.keys(weddingInformation).forEach(key => {
        weddingInformation[key] = action.weddingInformation[key]
      })
      return Object.assign({}, state, {
        weddingInformation,
      })
    case actionTypes.setMealTicketCount:
      return Object.assign({}, state, {
        mealTicketCount: action.mealTicketCount,
      })
    case actionTypes.setEncryptionKey:
      return Object.assign({}, state, {
        encryptionKey: action.encryptionKey,
      })
    default:
      return state
  }
}

export const initStore = () => dispatch => {
  return dispatch({ type: actionTypes.initStore })
}

export const setWeddingInformation = weddingInformation => dispatch => {
  return dispatch({ type: actionTypes.setWeddingInformation, weddingInformation })
}

export const setMealTicketCount = mealTicketCount => dispatch => {
  return dispatch({ type: actionTypes.setMealTicketCount, mealTicketCount })
}

export const setEncryptionKey = encryptionKey => dispatch => {
  return dispatch({ type: actionTypes.setEncryptionKey, encryptionKey })
}

export function initializeStore(initialState = initialState) {
  return createStore(reducer, initialState, composeWithDevTools(applyMiddleware(thunkMiddleware)))
}
