import Link from 'next/link'
import Router from 'next/router'
import { withRouter } from 'next/router'
import { connect } from 'react-redux'
import { initStore } from '../redux/store';
import { PROVIDER, NID, MANAGER_SCORE } from '../score/const';
import WeddingScore from '../score/WeddingScore'
import { requestJsonRpc } from '../utils/connect';
import { getItem } from '../utils/storage';
import { getTransactionResult } from '../utils/sdk';
import Header from '../components/header'
import Footer from '../components/footer'
import paragraphSeparator1 from '../images/paragraph_separator_1.png'

class Invite extends React.Component {

    constructor(props) {
        super(props)
        this.weddingScore = {}
        this.state = {
            loading: true,
            weddingInformation: {},
        }
    }

    componentDidMount() {
        const { scoreAddress } = this.props.router.query
        this.scoreAddress = scoreAddress
        console.log(scoreAddress)
        this.weddingScore = new WeddingScore(PROVIDER, NID, scoreAddress)
        const weddingInformation = this.weddingScore.information()
        this.setState({ weddingInformation })
        console.log(weddingInformation)
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
        } = this.state.weddingInformation
        return (
            <div className="preview">
                <Header />
                <div className="content invite">
                    <img className='separator' src={paragraphSeparator1} />
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
                    <hr />
                    <div className='invitation-message'>
                        <p>인사말</p>
                        <p>{invitation_message}</p>
                    </div>
                    <img src={wedding_photo_url} />
                    <hr />
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
                    <img className='separator last' src={paragraphSeparator1} />
                    {/* TODO 약도 */}
                    <Link href={`/congratulate?scoreAddress=${this.scoreAddress}`}>
                        <div className="button-holder">
                            <button className="long">축하하러 가기</button>
                        </div>
                    </Link>
                </div>
            </div>
        )
    }
}

export default withRouter(Invite)