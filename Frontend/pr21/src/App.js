import './App.css';
import React, { Component } from 'react';
import Home from './components/Home.js';
import Create from './components/create.js';
import projects from './components/projects.js';
import PageWrapper from './components/Pagewrapper.js';

// import React, { useState, useEffect } from 'react';
import {
  BrowserRouter as Router,
  Route
} from "react-router-dom";

class App extends Component {
  render() {
    
    return (
      <Router basename="/AutoMLCurl" >
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
            path="/newproject"
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
