import Router from 'next/router'
import { requestAddress } from '../utils/connect';
import { getItem, setItem } from '../utils/storage';
import ManagerScore from '../score/ManagerScore'
import { PROVIDER, NID, MANAGER_SCORE } from '../score/const';
import Header from '../components/header'
import { BeatLoader } from 'react-spinners';
import { css } from 'react-emotion';
import IconWithULogo from '../images/icon_with_u_logo.png'

class Index extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            loading: false
        }
    }

    componentDidMount() {
        const userAddress = getItem('userAddress')
        if (userAddress) {
            const managerScore = new ManagerScore(PROVIDER, NID, MANAGER_SCORE)
            const scoreAddress = managerScore.getWeddingScoreAddress(userAddress)
            if (scoreAddress !== 'cx') {
                Router.push(`/complete?scoreAddress=${scoreAddress}`)
            }
            else {
                Router.push(`/main`)
            }
        }
        else {
            this.setState({ loading: false })
        }
    }

    onLoginClick = async () => {
        const userAddress = await requestAddress(10000)
        setItem('userAddress', userAddress)
        Router.push(`/main`)
    }

    render() {
        return (
            <div className='index'>
                <p>너와 나, 우리들의 아이콘</p>
                <img src={IconWithULogo} />
                <div className='button-holder'>
                    {this.state.loading ?
                        <BeatLoader
                            color={'#0aafb3'}
                            className={css`
                                text-align: center;
                                height: 60px;
                                line-height: 70px;
                    `   }
                        />
                        :
                        <button className='long' onClick={this.onLoginClick}>ICONex로 간편 로그인</button>
                    }
                </div>
            </div>
        )
    }
}

export default Index