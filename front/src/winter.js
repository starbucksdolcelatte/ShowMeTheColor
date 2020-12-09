import React from 'react';
import './season.css?ver=1.4';
import winter from './season/winter.png';

const Winter = ( { history } ) => 
{
    return (
        <div className='season_class'>
            <img src = {winter} alt = "winter"/>
            <div id="btn_back">
            <button id="back_btn" onClick={ () => {history.push("/")}}>back</button>
            </div>
        </div>
    );
}

export default Winter;