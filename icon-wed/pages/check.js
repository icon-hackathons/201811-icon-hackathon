import { withRouter } from 'next/router'
import WeddingScore from '../score/WeddingScore'
import { PROVIDER, NID, WITHU_TOKEN_CONTRACT } from '../score/const';
import Header from '../components/header'
import { getItem } from '../utils/storage';
import weddingDecoration from '../images/wedding_decoration.png'
import { requestJsonRpc } from '../utils/connect';
import { convertLoopToIcx, getBalance } from '../utils/sdk';
import { getDecryptionKey, getEncryptionKey, encrypt, decrypt } from '../utils/encrypt';
import TokenScore from '../score/TokenScore';

class Check extends React.Component {
    constructor(props) {
        super(props)
        this.weddingScore = {},
        this.tokenScore = {},
        this.state = {
            guestsCount: 0,
            balance: 0,
            amountRaised: 0,
            tokenBalance: 0,
            giftycon: 0,
            userAddress: '',
            scoreAddress: '',
            weddingInformation: {},
            isGloom: true,
            isEncrypted: true,
            listData: []
        }
    }

    componentDidMount() {
        const userAddress = getItem('userAddress')
        const { scoreAddress } = this.props.router.query
        this.weddingScore = new WeddingScore(PROVIDER, NID, scoreAddress)
        const weddingInformation = this.weddingScore.information()
        const listData = this.weddingScore.getGroomGuests(0, 10)        
        // const guestsCount = this.weddingScore.getGuestsCount()
        const balance = getBalance(scoreAddress)
        // const amountRaised = this.weddingScore.getAmountRaised()
        this.tokenScore = new TokenScore(PROVIDER, NID, WITHU_TOKEN_CONTRACT)
        const tokenBalance = this.tokenScore.balanceOf(scoreAddress)
        this.setState({ balance, tokenBalance, userAddress, scoreAddress, weddingInformation, listData })
    }

    onGroomClick = () => {
        if (!this.state.isGloom) {
            const listData = this.weddingScore.getGroomGuests(0, 10)
            this.setState({ isGloom: true, listData })
        }
    }

    onBrideClick = () => {
        if (this.state.isGloom) {
            const listData = this.weddingScore.getBrideGuests(0, 10)
            this.setState({ isGloom: false, listData })
        }
    }

    onEncryptionClick = () => {
        this.setState({ isEncrypted: true })
    }

    onDecryptionClick = () => {
        this.setState({ isEncrypted: false })
        const decryptonKey = window.prompt('복호화 암호를 입력하세요.')
    }

    render() {
        const { weddingInformation, guestsCount, balance, amountRaised, tokenBalance, giftycon, isGloom, isEncrypted, listData } = this.state
        const { wedding_date_str } = weddingInformation
        return (
            <div className="check">
                <Header />
                <div className='title'>축의금 확인</div>
                <div className='content'>
                    <div className='dashboard'>
                        <p>Dashboard</p>
                        <p>D-day {wedding_date_str}</p>
                        <div className="count">
                            <span>{guestsCount}</span> 
                            <span>{balance}</span>
                            <span>{amountRaised}</span>
                            <span>{tokenBalance}</span>
                            <span>{giftycon}</span>
                        </div>
                        <div className="description">
                            <span>누적 하객수</span> 
                            <span>누적 축의금</span>
                            <span>잔여 식권</span>
                            <span>잔여 WTU</span>
                            <span>잔여 상품권</span>
                        </div>
                        <div className='buttons'>
                            <button className='slim'>인출하기</button>
                            <button className='slim'>충전하기</button>
                        </div>
                    </div>
                    <hr />
                    <div className='list'>
                        <p>축의금 리스트</p>
                        <table className='selector'>
                            <tbody>
                                <tr>
                                    <td onClick={this.onGroomClick}><span className={isGloom ? 'on' : 'off'}></span> 신랑측 축의금</td>
                                    <td onClick={this.onBrideClick}><span className={isGloom ? 'off' : 'on'}></span> 신부측 축의금</td>
                                </tr>
                                <tr>
                                    <td onClick={this.onEncryptionClick}><span className={isEncrypted ? 'on' : 'off'}></span> 암호화</td>
                                    <td onClick={this.onDecryptionClick}><span className={isEncrypted ? 'off' : 'on'}></span> 복호화</td>
                                </tr>
                            </tbody>
                        </table>
                        <table className='data'>
                            <thead>
                                <tr>
                                    <th>이름</th>
                                    <th>금액</th>
                                    <th>TxHash</th>
                                </tr>
                            </thead>
                            <tbody>
                                {listData.map((item, index) => {
                                    const name = item.secret === '0x1' ? '***' : item.name
                                    return (
                                        <tr key={index}>
                                            <td>{name}</td>
                                            <td>{convertLoopToIcx(item.amount)} ICX</td>
                                            <td>{item.hash}</td>
                                        </tr>
                                    )
                                })}
                            </tbody>
                        </table>                       
                    </div>
                    </div>
                </div>
                )
            }
        }
        
export default withRouter(Check)