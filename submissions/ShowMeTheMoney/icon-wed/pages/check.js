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
        this.ticketInfo = {},
        this.state = {
            guestsCount: 0,
            balance: 0,
            remaining: 0,
            amountRaised: 0,
            tokenBalance: 0,
            giftycon: 0,
            userAddress: '',
            scoreAddress: '',
            weddingInformation: {},
            isGloom: true,
            isEncrypted: true,
            listData: [],
            decryptedListData: [],
            password: '',
            hasPassword: false,
        }
    }

    componentDidMount() {
        const userAddress = getItem('userAddress')
        const { scoreAddress } = this.props.router.query
        this.weddingScore = new WeddingScore(PROVIDER, NID, scoreAddress)
        const weddingInformation = this.weddingScore.information()
        const listData = this.weddingScore.getGroomGuests(0, 100)        
        const guestsCount = this.weddingScore.getGuestsCount()
        const balance = getBalance(scoreAddress)
        const amountRaised = this.weddingScore.getAmountRaised()
        this.tokenScore = new TokenScore(PROVIDER, NID, WITHU_TOKEN_CONTRACT)
        const tokenBalance = this.tokenScore.balanceOf(scoreAddress)
        this.ticketInfo = this.weddingScore.getMealTicketInfo()
        const remaining = this.ticketInfo.remaining_amount
        console.log(this.ticketInfo, remaining, weddingInformation)
        this.setState({ guestsCount, remaining, amountRaised, balance, tokenBalance, userAddress, scoreAddress, weddingInformation, listData })
    }

    onGroomClick = () => {
        if (!this.state.isGloom) {
            const listData = this.weddingScore.getGroomGuests(0, 100)
            this.setState({ isGloom: true, listData })
        }
    }

    onBrideClick = () => {
        if (this.state.isGloom) {
            const listData = this.weddingScore.getBrideGuests(0, 100)
            this.setState({ isGloom: false, listData })
        }
    }

    onEncryptionClick = () => {
        this.setState({ isEncrypted: true, decryptedListData: [], hasPassword: false })
    }

    onDecryptionClick = () => {
        this.setState({ isEncrypted: false, hasPassword: false })
    }

    onConfirmClick = () => {
        try {
            const pk = getDecryptionKey(this.state.password)      
            console.log(pk)  
            const decryptedListData = []
            const listData = [...this.state.listData]
            console.log(listData)
            listData.forEach(item => {            
                const i = { ...item }
                if (item.secret === '0x1') {
                    i.name = decrypt(item.name, pk)
                }
                decryptedListData.push(i)
            })
            console.log(this.state.listData, decryptedListData)
            this.setState({decryptedListData, hasPassword: true, password: ''})
        }
        catch(e) {
            console.log(e)
        } 
    }

    onWithdrawClick = async () => {
        const userAddress = getItem('userAddress')
        const address = window.prompt('인출할 주소를 입력하세요.')
        if (!address) return
        const transaction = this.weddingScore.makeWithdraw(address, userAddress)
        try {
            const response = await requestJsonRpc(transaction, 60000)
            const { result: txHash } = response
            console.log(txHash)
            alert('인출에 성공하였습니다.')
        }
        catch (e) {
            console.error(e)
        }  
        
    }

    render() {
        const { hasPassword, weddingInformation, remaining, decryptedListData, guestsCount, amountRaised, tokenBalance, giftycon, isGloom, isEncrypted, listData } = this.state
        const { wedding_date_str } = weddingInformation
        const list = (!isEncrypted && hasPassword) ? decryptedListData : listData
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
                            <span>{amountRaised}</span>
                            <span>{remaining}</span>
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
                            <button onClick={this.onWithdrawClick} className='slim'>인출하기</button>
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
                        {!isEncrypted && !hasPassword && <input className="pw" type="password" value={this.state.password} onChange={(e)=>{this.setState({password: e.target.value})}}/>}
                        {!isEncrypted && !hasPassword && <button className="slim pw" onClick={this.onConfirmClick}>확인</button>}
                        <table className='data'>
                            <thead>
                                <tr>
                                    <th>이름</th>
                                    <th>금액</th>
                                    <th>TxHash</th>
                                </tr>
                            </thead>
                            <tbody>
                                {list.map((item, index) => {
                                    const name = item.secret === '0x1' && (isEncrypted || (!isEncrypted && !hasPassword)) ? '***' : item.name
                                    console.log(item, item.secret)
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