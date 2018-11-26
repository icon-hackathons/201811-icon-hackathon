import Link from 'next/link'
import { withRouter } from 'next/router'
import WeddingScore from '../score/WeddingScore'
import { PROVIDER, NID } from '../score/const';
import Header from '../components/header'
import Footer from '../components/footer'
import { getItem } from '../utils/storage';
import weddingDecoration from '../images/wedding_decoration.png'
import { requestJsonRpc } from '../utils/connect';

class Complete extends React.Component {
    constructor(props) {
        super(props)
        this.weddingScore = {}
        this.state = {
            userAddress: '',
            scoreAddress: '',
            weddingInformation: {},
        }
    }

    componentDidMount() {
        const userAddress = getItem('userAddress')
        const { scoreAddress } = this.props.router.query
        this.weddingScore = new WeddingScore(PROVIDER, NID, scoreAddress)
        const weddingInformation = this.weddingScore.information()
        this.setState({ userAddress, scoreAddress, weddingInformation })
    }

    onAddClick = async () => {
        const spouseAddress = window.prompt('배우자의 지갑 주소를 입력하세요.')
        const { userAddress, scoreAddress } = this.state
        const transaction = this.weddingScore.makeSetWeddingScoreAddress(scoreAddress, spouseAddress, userAddress)
        const response = await requestJsonRpc(transaction)
        console.log(response)
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
        const {
            userAddress,
            scoreAddress,
            weddingInformation
        } = this.state
        const {
            groom_name,
            bride_name,
            wedding_photo_url,
        } = weddingInformation
        return (
            <div className="complete">
                <Header />
                <div className='title'>{groom_name} • {bride_name}의 청첩장</div>
                <div className="content">
                    <img src={wedding_photo_url || 'https://pds.joins.com//news/component/htmlphoto_mmdata/201711/02/a7e52ac4-168e-4c9a-a31d-a0b206b53a6d.jpg'} />
                    <img src={weddingDecoration} />
                    <ul className='address'>
                        <li>청첩장 스코어</li>
                        <li>{scoreAddress}</li>
                    </ul>
                    <ul className='address'>
                        <li>로그인한 지갑</li>
                        <li>{userAddress}</li>
                    </ul>
                    <button onClick={this.onAddClick} className='slim'>배우자 지갑 추가</button>
                    <hr />
                    <div className='management'>
                        <p>청첩장 관리</p>
                        <table>
                            <tbody>
                                <tr>
                                    <td>청첩장 수정</td>
                                    <td>></td>
                                </tr>
                                <Link href={`/invite?scoreAddress=${scoreAddress}`}>
                                    <tr>
                                        <td>청첩장 발송</td>
                                        <td>></td>
                                    </tr>
                                </Link>
                                <tr>
                                    <td>청첩장 보관함</td>
                                    <td>></td>
                                </tr>
                                <tr>
                                    <td>웨딩 기프트 구매</td>
                                    <td>></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <hr className="short-margin-top" />
                    <div className='management'>
                        <p>장부 관리</p>
                        <table>
                            <tbody>
                                <Link href={`/check?scoreAddress=${scoreAddress}`}>
                                    <tr>
                                        <td>축의금 확인</td>
                                        <td>></td>
                                    </tr>
                                </Link>
                                <tr onClick={this.onWithdrawClick}>
                                    <td>축의금 인출</td>
                                    <td>></td>
                                </tr>
                                <tr>
                                    <td>장부 다운로드</td>
                                    <td>></td>
                                </tr>
                                <tr>
                                    <td>축하 메세지 보기</td>
                                    <td>></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        )
    }
}

export default withRouter(Complete)