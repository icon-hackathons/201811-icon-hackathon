import Router from 'next/router'
import Link from 'next/link'
import { withRouter } from 'next/router'
import { connect } from 'react-redux'
import { setWeddingInformation, setMealTicketCount, setEncryptionKey } from '../redux/store';
import Header from '../components/header'
import Footer from '../components/footer'
import { getEncryptionKey, getDecryptionKey, encrypt } from '../utils/encrypt';
import paragraphSeparator1 from '../images/paragraph_separator_1.png'
import { requestAddress, requestJsonRpc } from '../utils/connect';
import { PROVIDER, NID } from '../score/const';
import GuestTransfer from '../score/GuestTransfer';
import WeddingScore from '../score/WeddingScore';
import { setItem } from '../utils/storage';

class Congratulate extends React.Component {

    constructor(props) {
        super(props)
        this.scoreAddress = '',
        this.weddingInformation = {}
        this.encryptionKey = ''
        this.guestTransfer = {}
        this.weddingScore = {}
        this.state = {
            address: '',
            amount: 0,
            guest: '',
            secret: true,
            gloom: true,
            message: '',
            attend: true,
            meal: 0,
        }
    }

    componentDidMount() {
        const { scoreAddress } = this.props.router.query
        this.scoreAddress = scoreAddress
        this.weddingScore = new WeddingScore(PROVIDER, NID, this.scoreAddress)
        this.guestTransfer = new GuestTransfer(PROVIDER, NID)
        this.weddingInformation = this.weddingScore.information()
        this.encryptionKey = this.weddingScore.getPublicKey()
        console.log(this.encryptionKey)
    }

    handleChange = e => {
        const { name, value } = e.target
        this.setState({ [name]: value })

    }

    onAddressClick = async () => {
        const address = await requestAddress(10000)
        this.setState({ address })
    }

    onShowClick = () => {
        if (this.state.secret) {
            this.setState({ secret: false })
        }
    }

    onHideClick = () => {
        if (!this.state.secret) {
            this.setState({ secret: true })
        }
    }

    onGloomClick = () => {
        if (!this.state.gloom) {
            this.setState({ gloom: true })
        }
    }

    onBrideClick = () => {
        if (this.state.gloom) {
            this.setState({ gloom: false })
        }
    }

    onYesClick = () => {
        if (!this.state.attend) {
            this.setState({ attend: true })
        }
    }

    onNoClick = () => {
        if (this.state.attend) {
            this.setState({ attend: false })
        }
    }

    onConfirmClick = async () => {
        const {
            address,
            amount,
            guest,
            secret,
            gloom,
            message,
            attend,
            meal,
        } = this.state

        console.log(secret, guest, this.encryptionKey, encrypt(guest, this.encryptionKey))

        const data = {
            name: secret ? encrypt(guest, this.encryptionKey) : guest,
            message,
            attend,
            secret,
            host: gloom ? 0 : 1,
            ticket_amount: meal
        }

        const transaction = this.guestTransfer.makeTransfer(data, this.scoreAddress, amount, address)
        
        try {
            const response = await requestJsonRpc(transaction, 60000)
            const { result: txHash } = response
            setItem('guestAddress', address)
            setTimeout(()=>{
                console.log(txHash)
                Router.push(`/eat?scoreAddress=${this.scoreAddress}`)
            }, 2000)
        }
        catch (e) {
            console.error(e)
        }    
    }

    render() {
        const {
            address,
            amount,
            guest,
            secret,
            gloom,
            message,
            attend,
            meal,
        } = this.state

        return (
            <div className="register">
                <Header />
                <div className='title'>결혼을 축하합니다.</div>
                <div className="content congratulate">
                    <p>축의금</p>
                    <table>
                        <tbody>
                            <tr className="add-margin-bottom">
                                <td className="height">결제 지갑</td>
                                <td><button onClick={this.onAddressClick} className='slim address'>지갑 선택</button> <span>{address}</span></td>
                            </tr>
                            <tr>
                                <td>축의금 금액</td>
                                <td><input name='amount' value={amount} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <hr />
                    <p>축하메세지</p>
                    <table className="no-margin-bottom">
                        <tbody>
                            <tr>
                                <td>보내는 사람</td>
                                <td><input name='guest' value={guest} onChange={this.handleChange} /></td>
                            </tr>

                        </tbody>
                    </table>
                    <div className="no-margin-bottom">
                        <div className='attend'>이름 공개</div>
                        <table className='selector attend'>
                            <tbody>
                                <tr>
                                    <td onClick={this.onShowClick}><span className={secret ? 'off' : 'on'}></span> 공개</td>
                                    <td onClick={this.onHideClick}><span className={secret ? 'on' : 'off'}></span> 비공개</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div className="no-margin-bottom">
                        <div className='attend'>참석 관계</div>
                        <table className='selector attend'>
                            <tbody>
                                <tr>
                                    <td onClick={this.onGloomClick}><span className={gloom ? 'on' : 'off'}></span> 신랑</td>
                                    <td onClick={this.onBrideClick}><span className={gloom ? 'off' : 'on'}></span> 신부</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div>
                        <div>축하 메세지</div>
                        <textarea name='message' value={message} onChange={this.handleChange}></textarea>
                    </div>

                    <hr />
                    <p>설문 조사</p>
                    <div>
                        <div className='attend'>참석 여부</div>
                        <table className='selector attend'>
                            <tbody>
                                <tr>
                                    <td onClick={this.onYesClick}><span className={attend ? 'on' : 'off'}></span> 참석</td>
                                    <td onClick={this.onNoClick}><span className={attend ? 'off' : 'on'}></span> 불참석</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <table className="last">
                        <tbody>
                            <tr>
                                <td>식권 신청</td>
                                <td><input name='meal' value={meal} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <div className="button-holder">
                        <button className='long' onClick={this.onConfirmClick}>확인</button>
                    </div>
               </div>
            </div>
        )
    }
}

export default withRouter(Congratulate)