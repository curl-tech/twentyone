import React, { Component } from 'react';
import $ from 'jquery';
import Plots from './plots.js';
// import DownloadLink from "react-download-link";
// import { CSVLink } from "react-csv";
// import car from '../assets/testDataset/cardata.csv';
import Download from './download.js';
import Metrics from './metrics.js';
// import Papa from 'papaparse';
import axios from 'axios';
import Papa from 'papaparse';
class Section5 extends Component {



    constructor() {
        super();
        this.state = {
            // csvfile: undefined,
            data: "",
            inferencefile: undefined,
            plot: "",
            countplot: 0
        };
        this.updateData = this.updateData.bind(this);
    }
    // componentDidMount(){
    //     this.setState({data:""})
    // }
    handleGoBack = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('section5');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('section6');
        $(theFormItself2).show();
        var thebtnItself = document.getElementById('show');
        $(thebtnItself).show();
        this.setState({ data: "" });

    }
    handleRetrain = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('section5');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form2');
        $(theFormItself2).show();
        // var theFormItself3 = document.getElementById('section6');
        // $(theFormItself3).show();


    }

    // handleChange = event => {
    //     this.setState({
    //         csvfile: event.target.files[0]
    //     });
    // };
    updateData(result) {
        this.setState({
            data: result.data
        });
        // console.log(this.state.traindata);
    }
    handlemetric = event => {
        var thebtnItself = document.getElementById('show');
        $(thebtnItself).hide();
        this.setState({ data: "a" });
        const projectid = this.props.projectdetails["projectID"];
        const modelid = this.props.projectdetails["modelID"];
        const FileDownload = require('js-file-download');
        axios.get('http://localhost:8000/getMetrics/' + projectid + "/" + modelid)
            .then((response) => {
                console.log(response)
                console.log(response.data);
                Papa.parse(response.data, {
                    complete: this.updateData,
                    header: true
                });
                if (this.props.projectdetails.modelType === "clustering")
                {
                    FileDownload(response.data, 'metrics.csv');
                    alert("File is big so it is downloaded");
                }// this.setState({data: response.data});
                // FileDownload(response.data, 'metrics.csv');
                // this.setState({data: response.data});
                // console.log(this.state.data);
            });


    }
    handlePlot = event => {
        const FileDownload = require('js-file-download');
        const projectid = this.props.projectdetails["projectID"];
        if (this.state.countplot === 0) {
            axios.get('http://localhost:8000/getPlots/' + projectid)
                .then((response) => {
                    // console.log(response);
                    this.setState({ plot: response.data });
                    var answer = window.confirm("Plots are ready and displayed. Want to Download in a file?");
                    if (answer) {
                        FileDownload(response.data, 'plot.html');
                    }
                    else {
                        console.log("plots not downloaded")
                    }
                });
            this.setState({ countplot: 1 })
        }
    }

    // importCSV = () => {
    //     const { csvfile } = this.state;
    //     Papa.parse(csvfile, {
    //         complete: this.updateData,
    //         header: true
    //     });
    // };

    // updateData(result) {
    //     this.setState({
    //         data: result.data
    //     });
    //     var data = result.data;
    //     console.log(data);
    // }
    handleInferenceChange = event => {
        this.setState({
            inferencefile: event.target.files[0]
        })
        // console.log(event.target.files[0]);
    }
    handleGetPrediction = event => {
        event.preventDefault();
        const formdata = new FormData();
        formdata.append(
            "projectID",
            this.props.projectdetails["projectID"]

        );
        formdata.append(
            "modelID",
            this.props.projectdetails["modelID"]

        );
        formdata.append(
            "inferenceDataFile",
            this.state.inferencefile

        );
        const FileDownload = require('js-file-download');
        axios.post('http://localhost:8000/doInference', formdata, { headers: { 'Accept': 'multipart/form-data', 'Content-Type': 'multipart/form-data' } })
            .then((res) => {
                console.log("Successful", res)
                FileDownload(res.data, 'prediction.csv');
                alert("Prediction is Ready and Downloaded");
            },
                (error) => { console.log(error) });
    }

    render() {
        return (

            <div className="section5 " id="section5">
                <div className="goback">
                    <button className="backbtn btn btn-secondary" onClick={this.handleGoBack}  > Go Back to Models </button>

                </div>
                {this.props.showRetrain === false ? null :
                    <div className="goback">
                        <button className="backbtn btn btn-secondary" onClick={this.handleRetrain}  >Retrain</button>

                    </div>
                }

                <div className="sec5heading">
                    <h1>Results (Model Number:  {this.props.currentmodel})</h1>
                </div>


                <div className="container">
                    {/* <!-- Nav tabs --> */}
                    <ul className="nav nav-tabs" id="myTab" role="tablist">
                        <li className="nav-item" role="presentation">
                            <button className="nav-link tabbtn active" id="Metrics-tab" data-bs-toggle="tab" data-bs-target="#metrics" type="button" role="tab" aria-controls="metrics" aria-selected="true">
                            {this.props.projectdetails.modelType==="clustering"?"Alloted Clusters":"Metrics"}</button>
                        </li>
                        <li className="nav-item" role="presentation">
                            <button className="nav-link tabbtn " id="plot-tab" onClick={this.handlePlot} data-bs-toggle="tab" data-bs-target="#plot" type="button" role="tab" aria-controls="Plot" aria-selected="false">Plots</button>
                        </li>
                        <li className="nav-item" role="presentation">
                            <button className="nav-link tabbtn" id="download-tab" data-bs-toggle="tab" data-bs-target="#download" type="button" role="tab" aria-controls="Download" aria-selected="false">Download</button>
                        </li>
                        <li className="nav-item" role="presentation">
                            <button className="nav-link tabbtn" id="Inference-tab" data-bs-toggle="tab" data-bs-target="#inference" type="button" role="tab" aria-controls="Inference" aria-selected="false">Inference</button>
                        </li>
                    </ul>

                    {/* <!-- Tab panes --> */}
                    <div className="tab-content">
                        <div className="tab-pane active" id="metrics" role="tabpanel" aria-labelledby="metrics-tab">
                            {/* Metrics will be displayed here */}
                            {/* <input type="file" className="form-control" id="metric" onChange={this.handleChange} accept=".csv" name="metric"
                                placeholder="enter data in csv" required />
                            <button onClick={this.importCSV} className="sec5btn">Import</button> */}
                            <button onClick={this.handlemetric} className="sec5btn" id="show">Show</button>
                            <Metrics data={this.state.data} mtype={this.props.mtype}/>
                        </div>



                        <div className="tab-pane" id="plot" role="tabpanel" aria-labelledby="plot-tab">

                            <div className="container">
                                <div className="d-flex flex-row justify-content-center flex-wrap">
                                    <Plots plot={this.state.plot} />
                                    {/* <div className="d-flex flex-column plot" >
                                         <img src="3" className="img-fluid" alt=" Plot3 not for this model " />*/}

                                </div>
                            </div>
                        </div>
                        <div className="tab-pane" id="download" role="tabpanel" aria-labelledby="download-tab">

                            <section className=" cards2 card-group ">
                                <div className="card flip-card ">
                                    <div className="flip-card-inner ">
                                        <div className="flip-card-front2">
                                            <h1>Clean Data</h1>
                                        </div>
                                        <div className="flip-card-back2 ">
                                            <p>"Download clean Data"</p>
                                            <Download type="clean" projectdetails={this.props.projectdetails} />


                                        </div>
                                    </div>
                                </div>
                                <div className="card flip-card ">
                                    <div className="flip-card-inner">
                                        <div className="flip-card-front2">
                                            <h1>Pickle File</h1>
                                        </div>
                                        <div className="flip-card-back2 ">
                                            <p>"Download pickle file"</p>
                                            <Download type="pickle" projectdetails={this.props.projectdetails} />

                                        </div>
                                    </div>
                                </div>

                            </section>
                        </div>
                        <div className="tab-pane" id="inference" role="tabpanel" aria-labelledby="Inference-tab">
                            <div className="container " id="form1">
                                <form >
                                    <div className="createform">


                                        <div className="row">
                                            <div className="col-40">
                                                <label htmlFor="Inference">Enter data to get Prediction</label>
                                            </div>
                                            <div className="col-60">
                                                <input type="file" className="form-control" id="inference" onChange={this.handleInferenceChange} accept=".csv" name="inference"
                                                    placeholder="enter training data in csv format" required />
                                            </div>
                                        </div>


                                        <div>
                                            <button type="submit" className="formbutton btn btn-secondary" onClick={this.handleGetPrediction} id="getresults" >Get Results</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>

                    </div>
                </div >
            </div >

        );
    }
}

export default Section5;
