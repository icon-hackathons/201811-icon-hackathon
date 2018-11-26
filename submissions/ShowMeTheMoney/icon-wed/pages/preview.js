import Link from 'next/link'
import Router from 'next/router'
import { withRouter } from 'next/router'
import { connect } from 'react-redux'
import { initStore } from '../redux/store';
import { PROVIDER, NID, MANAGER_SCORE } from '../score/const';
import ManagerScore from '../score/ManagerScore'
import { requestJsonRpc } from '../utils/connect';
import { getItem } from '../utils/storage';
import { getTransactionResult } from '../utils/sdk';
import Header from '../components/header'
import Footer from '../components/footer'
import paragraphSeparator1 from '../images/paragraph_separator_1.png'

class Preview extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            loading: true
        }
    }

    onPayClick = async () => {
        const managerScore = new ManagerScore(PROVIDER, NID, MANAGER_SCORE)
        console.log(this.props.mealTicketCount, this.props.encryptionKey)
        const params = {
            'information': this.props.weddingInformation,
            'meal_ticket_count': this.props.mealTicketCount,
            'public_key': this.props.encryptionKey
        }
        const userAddress = getItem('userAddress')
        console.log(userAddress)
        const transaction = managerScore.makeDepolyTransaction(params, userAddress, true)
        try {
            const response = await requestJsonRpc(transaction, 60000)
            const { result: txHash } = response
            setTimeout(()=>{
                this.props.initStore()
                const transactionResult = getTransactionResult(txHash)
                const { scoreAddress } = transactionResult
                Router.push(`/complete?scoreAddress=${scoreAddress}`)
            }, 2000)
        }
        catch (e) {
            console.error(e)
        }
    }

    render() {
        const {
            groom_name,
            groom_father_name,
            groom_mother_name,
            bride_name,
            bride_father_name,
            bride_mother_name,
            wedding_date_str,
            wedding_place_name,
            wedding_place_address,
            invitation_message,
            wedding_photo_url
        } = this.props.weddingInformation
        return (
            <div className="preview">
                <Header />
                <div className='title'>청첩장 미리보기</div>
                <div className="content">
                    <img className='separator' src={paragraphSeparator1}/>
                    <div className='groom-bride'>
                        <p>{groom_name} • {bride_name}</p>
                        <p>두 사람의 결혼식에 초대합니다.</p>
                    </div>
                    <ul className='father-mother'>
                        <li>신랑혼주</li>
                        <li>{groom_father_name}, {groom_mother_name}</li>
                    </ul>
                    <ul className='father-mother'>
                        <li>신부혼주</li>
                        <li>{bride_father_name}, {bride_mother_name}</li>
                    </ul>
                    <hr/>
                    <div className='invitation-message'>
                        <p>인사말</p>
                        <p>{invitation_message}</p>
                    </div>
                    <img src={wedding_photo_url} />
                    <hr/>
                    <div className='wedding-information'>
                        <p>예식 안내</p>
                        <table>
                            <tbody>
                                <tr>
                                    <td>일시</td>
                                    <td>{wedding_date_str}</td>
                                </tr>
                                <tr>
                                    <td>장소</td>
                                    <td>{wedding_place_name}</td>
                                </tr>
                                <tr>
                                    <td>주소</td>
                                    <td>{wedding_place_address}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <img className='separator last' src={paragraphSeparator1}/>
                    {/* TODO 약도 */}
                    <div className="button-holder">
                        <button className='short' onClick={() => { Router.back() }}>수정</button>
                        <button className='short' onClick={this.onPayClick}>등록</button>
                    </div>
                </div>
            </div>
        )
    }
}

function mapStateToProps(state) {
    const { weddingInformation, mealTicketCount, encryptionKey } = state
    return { weddingInformation, mealTicketCount, encryptionKey }
}

function mapDispatchToProps(dispatch) {
    return {
        initStore: payload => dispatch(initStore(payload))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Preview))