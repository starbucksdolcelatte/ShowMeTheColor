import React from 'react';
import './season.css?ver=1.4';
import spring from './season/spring.jpg';

const Spring = ( { history } ) => 
{
    return (
        <div className='season_class'>
            <img src = {spring} width='1300' height='600' alt = "spring"/>
            <div id="btn_back">
            <button id="back_btn" onClick={ () => {history.push("/")}}>back</button>
            </div>
        </div>
    );
}

export default Spring;