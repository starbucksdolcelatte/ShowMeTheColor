import React, { Component } from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Home from './Home';
import Test from './test';
import Test2 from './test2';
import Test3 from './test3';
import Spring from './spring';
import Summer from './summer';
import Autumn from './autumn';
import Winter from './winter';


class App extends Component {
  render() {
    return(
      <div>
        <BrowserRouter>
          <Route path="/" exact component={Home} />
          <Route path="/test" exact component={Test} />
          <Route path="/test2" exact component={Test2} />    
          <Route path="/test3" exact component={Test3} />
          <Route path="/spring" exact component={Spring} />
          <Route path="/summer" exact component={Summer} />
          <Route path="/autumn" exact component={Autumn} />
          <Route path="/winter" exact component={Winter} />
        </BrowserRouter>
      </div>
    )
  }
}

export default App;