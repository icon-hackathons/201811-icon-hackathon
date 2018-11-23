import { withRouter } from 'next/router'
import WeddingScore from '../score/WeddingScore'
import { PROVIDER, NID } from '../score/const';

class Footer extends React.Component {
    render() {
        return (
            <div className='footer'>
                <span>청첩장</span>
                <span>축하메세지</span>
                <span>축의금 장부</span>
                <span>답례품</span>
                <span>상대방 지갑 등록</span>
            </div>
        )
    }
}

export default withRouter(Footer)