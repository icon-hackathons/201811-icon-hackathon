import { withRouter } from 'next/router'
import WeddingScore from '../score/WeddingScore'
import { PROVIDER, NID } from '../score/const';
import IconWithULogo from '../images/icon_with_u_logo.png'

class Header extends React.Component {
    render() {
        return (
            <div className='header'>
                <img src={IconWithULogo}/>
            </div>
        )
    }
}

export default withRouter(Header)