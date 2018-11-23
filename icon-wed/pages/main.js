import Router from 'next/router'
import { withRouter } from 'next/router'
import { getBalance } from "../utils/sdk";
import { getItem } from '../utils/storage';
import Header from '../components/header'
import Footer from '../components/footer'
import weddingInvitation from '../images/wedding_invitation.png'

class Main extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            balance: 0,
            userAddress: '',
            scoreAddress: ''
        }
    }

    componentDidMount() {
        const userAddress = getItem('userAddress')
        const { scoreAddress } = this.props.router.query
        if (userAddress) {
            const balance = getBalance(userAddress)
            this.setState({ userAddress, balance })
        }

        if (scoreAddress) {
            this.setState({ scoreAddress })
        }

        // TODO 
        // 오너가 다를 경우 추가 처리
    }

    onClick = () => {
        const { scoreAddress } = this.state
        if (scoreAddress) {
            Router.push(`/complete?scoreAddress=${scoreAddress}`)
        }
        else {
            Router.push(`/register`)
        }
    }

    render() {
        const { userAddress, scoreAddress, balance } = this.state
        return (
            <div className='main'>
                <Header />
                <p>[청첩장 제작 - 축의금 수령 - 장부 관리]<br/>블록체인 청첩장으로 한번에 해결하세요.</p>
                <img src={weddingInvitation} />
                <div className='button-holder'>
                    <button className='long' onClick={this.onClick}>블록체인 청첩장 만들기</button>
                </div>
            </div>
        )
    }
}

export default withRouter(Main)