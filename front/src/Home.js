import React from 'react';
import './Home.css?v=1.0';
import './snow.css';


const Snowflake = ({ style }) => {
    return (
      <p className="snow-flake" style={style}>
        {"\u2745"}
      </p>
    );
  };
  
  const makeSnowFlakes = () => {
    let animationDelay = "0.1s"; 
    let fontSize = "14px"; 
    const arr = Array.from("Merry Christmas"); 
  
   
    return arr.map((el, i) => {
      animationDelay = `${(Math.random() * 80).toFixed(100)}s`; 
      fontSize = `${Math.floor(Math.random() * 10) + 25}px`; 
      const style = {
        animationDelay,
        fontSize,
      };
    return <Snowflake key={i} style={style} />;  });
  };
  



const Home = ( { history } ) => 
{
   
    return (
        <>
            <div>
                <div className="snow-container">
                {makeSnowFlakes()}
                </div>
                <head>
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.7.2/animate.min.css"></link>
                </head>
                <div className='home_display'>
                <center id='home'>
                    <div className='animated fadeInDown'>findyourcolor</div>
                </center>
                    <div id="btn_group">
                    <button id="soo_btn2" onClick={ () => {history.push("/test")}}>test</button>
                    </div>
                </div>
            </div>
        </>
    );
}

export default Home;