import Router from 'next/router'
import { withRouter } from 'next/router'
import { getBalance } from "../utils/sdk";
import { getItem } from '../utils/storage';
import Header from '../components/header'
import Footer from '../components/footer'
import weddingDish from '../images/wedding_dish.png'
import weddingInvitation from '../images/wedding_invitation.png'
import { PROVIDER, NID } from '../score/const';
import GuestTransfer from '../score/GuestTransfer';
import { requestJsonRpc } from '../utils/connect';
import WeddingScore from '../score/WeddingScore';

class Main extends React.Component {
    constructor(props) {
        super(props)
        this.guestAddress = '',
        this.scoreAddress = '',
        this.guestTransfer = {}
        this.weddingScore = {}
        this.state = {
            count: 0,
            complete: false
        }
    }

    componentDidMount() {
        const guestAddress = getItem('guestAddress')
        const { scoreAddress } = this.props.router.query
        this.guestAddress = guestAddress
        this.scoreAddress = scoreAddress
        this.weddingScore = new WeddingScore(PROVIDER, NID, this.scoreAddress)
        this.guestTransfer = new GuestTransfer(PROVIDER, NID)
        const count = this.weddingScore.getMealTicketCount(this.guestAddress)
        console.log(count)
        this.setState({ count })
    }

    onClick = async () => {
        if (this.state.complete) return
        const transaction = this.guestTransfer.makeRefundMealTicket(this.scoreAddress, this.guestAddress)
        try {
            const response = await requestJsonRpc(transaction, 60000)
            const { result: txHash } = response
            console.log(txHash)
            this.setState({complete: true})
        }
        catch (e) {
            console.error(e)
        }  
    }

    render() {
        const { complete } = this.state
        return (
            <div className='main eat'>
                <Header />
                <div className='title'>{complete ? 'Have a nice day!' : 'Succeed!'}</div>
                {complete ?
                    <p>식권이 사용되었습니다.</p>
                    :
                    <p>축하메시지 및 축의금이 블록체인에<br/>성공적으로 전송되었습니다.</p>
                }
                
                <img src={weddingDish} />                
                <div className="count">{complete ? '사용 완료' : `식권 ${this.state.count} 장`}</div>                
                <div className='button-holder'>
                    <button className={`long${complete ? ' disabled': ''}`} onClick={this.onClick}>식권 사용하기</button>
                </div>
            </div>
        )
    }
}

export default withRouter(Main)