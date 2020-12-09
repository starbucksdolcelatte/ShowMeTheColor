import React from 'react';
import './season.css?ver=1.4';
import autumn from './season/autumn.png';

const Autumn = ( { history } ) => 
{
    return (
        <div className='season_class'>
            <img src = {autumn} width='1300' height='600' alt = "autumn"/>
            <div id="btn_back">
            <button id="back_btn" onClick={ () => {history.push("/")}}>back</button>
            </div>
        </div>
    );
}

export default Autumn;