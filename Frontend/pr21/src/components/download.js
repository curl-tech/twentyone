import React, { Component } from 'react';
import axios from 'axios';

class Download extends Component {

  handleDownloadClean = event => {
    event.preventDefault();
    const FileDownload = require('js-file-download');
    const dataid=this.props.projectdetails["dataID"];
    axios.get('http://localhost:8000/downloadClean/'+dataid)
      .then((response) => {
        console.log(response)
        FileDownload(response.data, 'cleandata.csv');
      });
  }
  handleDownloadPickle = event => {
    event.preventDefault();
    const FileDownload = require('js-file-download');
    const modelid=this.props.projectdetails["modelID"];
    axios.get('http://localhost:8000/downloadPickle/'+modelid)
      .then((response) => {
        FileDownload(response.data, 'pickledmodel.pkl');
      });
  }
  render() {
    if (this.props.type === "clean") {
      return (
        <button className="sec5btn btn btn-primary" onClick={this.handleDownloadClean} >Download</button>
      );
    }
    else {
      return (
        <button className="sec5btn btn btn-primary" onClick={this.handleDownloadPickle} >Download</button>
      );
    }
  }
}

export default Download;