import React, { Component } from 'react';
import axios from 'axios';

class Download extends Component {

  handleDownloadClean = event => {
    event.preventDefault();
    axios.get('http://localhost:8000/downloadClean/36550')
      .then((response) => {
        console.log(response.data);
        console.log(response.status);
        console.log(response.statusText);
        console.log(response.headers);
        console.log(response.config);
      });
  }
  handleDownloadPickle = event => {
    event.preventDefault();
    axios.get('http://localhost:8000/downloadPickle/36550')
      .then((response) => {
        console.log(response.data);
        console.log(response.status);
        console.log(response.statusText);
        console.log(response.headers);
        console.log(response.config);
      });
  }
  render() {
    if (this.props.type === "clean") {
      return (
        <button className="sec5btn" onClick={this.handleDownloadClean} >Download</button>
      );
    }
    else {
      return (
        <button className="sec5btn" onClick={this.handleDownloadPickle} >Download</button>
      );
    }
  }
}

export default Download;