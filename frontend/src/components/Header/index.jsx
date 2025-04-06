import './index.css';

import logotype from '../../assets/logotype.svg';
import burger from '../../assets/burger-icon.svg';
import avatar from '../../assets/avatar-icon.svg';

import { Link } from 'react-router-dom';



function Header() {



    return (
        <>
            <div className="header-wrapper">
                <div className="header-elements">
                    <Link to="/" className="header-logotype">
                        <img src={logotype}/>
                    </Link>
                    <div className="header-navigation">
                        <button className="header-burger-menu">
                            <img src={burger}/>
                        </button>
                        <Link to="login" className="header-profile">
                            <img src={avatar} />
                        </Link>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Header;