import Link from 'next/link'
import { withRouter } from 'next/router'
import { connect } from 'react-redux'
import { setWeddingInformation, setMealTicketCount, setEncryptionKey } from '../redux/store';
import Header from '../components/header'
import Footer from '../components/footer'
import { getEncryptionKey, getDecryptionKey } from '../utils/encrypt';
import paragraphSeparator1 from '../images/paragraph_separator_1.png'

class Register extends React.Component {

    constructor(props) {
        super(props)
        const { weddingInformation, mealTicketCount } = this.props
        this.state = {
            ...weddingInformation,
            mealTicketCount,
            password: '',
            passwordCheck: '',
        }
    }

    handleChange = e => {
        const { name, value } = e.target
        this.setState({ [name]: value })
    }

    onNextClick = () => {
        const { mealTicketCount, password } = this.state
        const encryptionKey = getEncryptionKey(password)
        this.props.setWeddingInformation(this.state)
        this.props.setMealTicketCount(mealTicketCount)
        this.props.setEncryptionKey(encryptionKey)
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
            wedding_photo_url,
            mealTicketCount,
            password,
            passwordCheck,
        } = this.state

        return (
            <div className="register">
                <Header />
                <div className='title'>청첩장 등록하기</div>
                <div className="content">
                    <p>1. 기본 정보</p>
                    <table>
                        <tbody>
                            <tr>
                                <td>신랑</td>
                                <td><input name='groom_name' value={groom_name} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>신랑 父</td>
                                <td><input name='groom_father_name' value={groom_father_name} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>신랑 母</td>
                                <td><input name='groom_mother_name' value={groom_mother_name} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <table>
                        <tbody>
                            <tr>
                                <td>신부</td>
                                <td><input name='bride_name' value={bride_name} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>신부 父</td>
                                <td><input name='bride_father_name' value={bride_father_name} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>신부 母</td>
                                <td><input name='bride_mother_name' value={bride_mother_name} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <hr/>

                    <p>2. 예식 정보</p>
                    <table className="no-margin-bottom">
                        <tbody>
                            <tr>
                                <td>예식 날짜</td>
                                <td><input name='wedding_date_str' value={wedding_date_str} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>예식장</td>
                                <td><input name='wedding_place_name' value={wedding_place_name} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>주소</td>
                                <td><input name='wedding_place_address' value={wedding_place_address} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>웨딩 사진</td>
                                <td><input name='wedding_photo_url' value={wedding_photo_url} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <div>
                        <div>인사말</div>
                        <textarea name='invitation_message' value={invitation_message} onChange={this.handleChange}></textarea>
                    </div>

                    <hr/>

                    <p>3. 축의금 장부 비밀번호</p>
                    <table>
                        <tbody>
                            <tr>
                                <td>입력</td>
                                <td><input type='password' name='password' value={password} onChange={this.handleChange} /></td>
                            </tr>
                            <tr>
                                <td>확인</td>
                                <td><input type='password' name='passwordCheck' value={passwordCheck} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>

                    <hr/>

                    <p>4. 식권 관리</p>
                    <table className='last'>
                        <tbody>
                            <tr>
                                <td>수량 입력</td>
                                <td><input name='mealTicketCount' value={mealTicketCount} onChange={this.handleChange} /></td>
                            </tr>
                        </tbody>
                    </table>        

                    <p className="caution">* 청첩장 등록시에 약 12 ICX의 수수료가 발생할 수 있습니다.</p>

                    <Link href='/preview'>
                        <div className="button-holder">
                            <button className='long' onClick={this.onNextClick}>다음</button>
                        </div>
                    </Link>                    
                </div>
            </div>
        )
    }
}

function mapStateToProps(state) {
    const { weddingInformation, mealTicketCount } = state
    return { weddingInformation, mealTicketCount }
}

function mapDispatchToProps(dispatch) {
    return {
        setWeddingInformation: payload => dispatch(setWeddingInformation(payload)),
        setMealTicketCount: payload => dispatch(setMealTicketCount(payload)),
        setEncryptionKey: payload => dispatch(setEncryptionKey(payload))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(withRouter(Register))