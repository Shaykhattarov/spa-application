import './index.css';

import truck from '../../assets/truck-icon.svg';
import map from '../../assets/map-icon.svg';
import shop from '../../assets/shop-icon.svg';


function Home() {
    
    return (
        <>
            <div className='home-wrapper'>
                <div className='home-elements'>
                    <div className="home-huge-text">
                        Учет приема товаров
                    </div>
                    <div className='home-normal-text'>
                        в продуктовом магазине
                    </div>
                    <div className='home-icons-wrapper'>
                        <div className='home-icon'>
                            <img src={truck}/>
                        </div>
                        <div className='home-icon'>
                            <img src={map} />
                        </div>
                        <div className='home-icon'>
                            <img src={shop} />
                        </div>
                    </div>
                </div>
            </div>
        </>
    ); 
}

export default Home;