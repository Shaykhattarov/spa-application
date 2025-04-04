import './Header.css';

import logotype from '../../assets/logotype.svg';
import burger from '../../assets/burger-icon.svg';
import avatar from '../../assets/avatar-icon.svg';

function Header() {
    return (
        <>
            <div className="header-wrapper">
                <div className="header-elements">
                    <div className="header-logotype">
                        <img src={logotype}/>
                    </div>
                    <div className="header-navigation">
                        <div className="header-burger-menu">
                            <img src={burger}/>
                        </div>
                        <div className="header-profile">
                            <img src={avatar} />
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Header