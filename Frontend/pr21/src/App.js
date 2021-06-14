import './App.css';
import Home from './components/Home.js';
import Create from './components/create.js';
import React, { Component } from 'react';

import { BrowserRouter as Router, Route, } from "react-router-dom";
class App extends Component {
  render() {

    return (
      <Router basename="/Auto_ml_curl" >
        <PageWrapper>
          <Route
            exact={true}
            path="/"
            component={Home}
          />
          <Route
            path="/Home"
            component={Home}
          />

          <Route
            path="/Newproject"
            component={Create}
          />
          <Route
            path="/MyProjects"
            component={projects}
          />
        </PageWrapper>
      </Router>
    );
  }
}

export default App;
