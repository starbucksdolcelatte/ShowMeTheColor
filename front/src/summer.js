import React from 'react';
import './season.css?ver=1.4';
import summer from './season/summer.jpg';

const Summer = ( { history } ) => 
{
    return (
        <div className='season_class'>
            <img src = {summer} width='1300' height='600' alt = "summer"/>
            <div id="btn_back">
            <button id="back_btn" onClick={ () => {history.push("/")}}>back</button>
            </div>
        </div>
    );
}

export default Summer;