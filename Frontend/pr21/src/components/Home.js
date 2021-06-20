import React, { Component } from 'react';
import aivideo from "../assets/videos/AI.mp4";
import $ from 'jquery';
import axios from 'axios';
import { HashLink as Link } from 'react-router-hash-link';
import Result from './Result.js';
import Section1 from './section1.js';
import Section6 from './section6.js';

class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            projectname: '',
            train: null,
            mtype: 'classification',
            auto: true,
            target: '',
            modelnum: 3,
            nulltype: 'NA'
        }
    }
    handleProjectNameChange = event => {
        this.setState({
            projectname: event.target.value
        })
    }
    handleTrainChange = event => {
        this.setState({
            train: event.target.files[0]
        })
        console.log(event.target.files[0])

    }
    handleMtypeChange = event => {
        this.setState({
            mtype: event.target.value
        })
    }
    handleSubmit = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('form1');
        $(theFormItself).fadeOut(2000);
        var theFormItself2 = document.getElementById('form2');
        $(theFormItself2).fadeIn(5000);
        const formData = new FormData();
        formData.append(
            "projectName",
            this.state.projectname

        );
        formData.append(
            "mtype",
            this.state.mtype

        );
        formData.append(
            "train",
            this.state.train
        );

        // let projectname = this.state.projectname
        // let train = this.state.train
        // let mtype = this.state.mtype
        // let data = { projectname, train, mtype }
        console.log(formData)
        axios({
            url: `http://localhost:8000/create`,
            method: "POST",
            headers:
            {
                // 'Accept': 'application/json',
                'Content-Type': 'multipart/form-data'
            },
            body: formData
        }).then((res) => {
            res.json().then((result) => {
                console.log("result", result)
            })
        })
    }
    handleAuto() {
        var theFormItself = document.getElementById('form2');
        $(theFormItself).fadeOut(1000);
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).fadeIn(1000);
    }
    handleManual() {
        this.setState({
            auto: false
        })
        var theFormItself = document.getElementById('form2');
        $(theFormItself).fadeOut(1000);
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).fadeIn(1000);
    }
    handleTargetChange = event => {
        this.setState({
            target: event.target.value
        })
    }
    handleModelNumChange = event => {
        this.setState({
            modelnum: event.target.value
        })
    }
    handleNullTypeChange = event => {
        this.setState({
            nulltype: event.target.value
        })
    }
    handleSubmit2 = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('form3');
        $(theFormItself).fadeOut(2000);
        var theFormItself2 = document.getElementById('loader');
        $(theFormItself2).fadeIn(2000);
        let isauto = this.state.auto
        let target = this.state.target
        let modelnumber = this.state.modelnum
        let nulltype = this.state.nulltype
        let data = { isauto, target, modelnumber, nulltype }
        console.log(JSON.stringify(data))
        axios({
            url: `http://localhost:8000/auto`,
            method: "POST",
            headers:
            {
                // 'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        }).then((res) => {
                console.log("Successfull")
            })
    }
    handleModelResult = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('section6');
        $(theFormItself).fadeOut(300);
        var theFormItself2 = document.getElementById('section5');
        $(theFormItself2).fadeIn(300);
    }
    handleGoBack = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('section5');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('section6');
        $(theFormItself2).show();
    }
    render() {
        return (
            <div>
                {/* ************************************************************************************************************************ */}

                {/* Section1 */}
                <Section1 />

                {/* ************************************************************************************************************************ */}
                {/* Section2  */}
                <div className="section2" id="section2">
                    <div className="createpagebox ">
                        <h1>Start With Your Project</h1>
                        <p>" Just fill relevant feeds and select few choices and you are good to go"</p>
                    </div>

                    {/* form1 */}
                    <div className="container " id="form1">
                        <form onSubmit={this.handleSubmit}>
                            <div className="createform">
                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="projectname">Name of your project?</label>
                                    </div>
                                    <div className="col-70">

                                        <input type="text" id="projectname" name="projectname" placeholder="Name your project..." value={this.state.projectname} onChange={this.handleProjectNameChange} required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="train">Enter training data</label>
                                    </div>
                                    <div className="col-70">
                                        <input type="file" className="form-control" id="train" onChange={this.handleTrainChange} accept=".csv" name="train"
                                            placeholder="enter training data in csv format" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="type">Which type of data is it?</label>
                                    </div>
                                    <div className="col-70 ">
                                        <select name="mtype" id="modeltype" value={this.state.mtype} onChange={this.handleMtypeChange}>
                                            <option value="classification">Classification</option>
                                            <option value="regression">Regression</option>
                                        </select>

                                    </div>
                                </div>

                                <div>
                                    <button type="submit" className="formbutton" id="startengine" >Begin Engine </button>
                                </div>
                            </div>
                        </form>
                    </div>
                    {/* form2 */}
                    <div className="container" id="form2">
                        <div className="centered ">

                            <section className="createform cards ">
                                <div className="flip-card col-50">
                                    <div className="flip-card-inner">
                                        <div className="flip-card-front">
                                            <h1>Auto</h1>
                                        </div>
                                        <div className="flip-card-back">
                                            <p>"Leave everything on us and see the beauty of artificial Intelligence"</p>
                                            <button className="btn2" onClick={this.handleAuto} id="form2autobutton">Select</button>
                                        </div>
                                    </div>
                                </div>
                                <div className="flip-card col-50">
                                    <div className="flip-card-inner">
                                        <div className="flip-card-front">
                                            <h1>Manual</h1>
                                        </div>
                                        <div className="flip-card-back">
                                            <p>"We believe you are always the boss and you can choose to make models as you wish"</p>
                                            <button className="btn2" onClick={this.handleManual}>Select</button>
                                        </div>
                                    </div>
                                </div>

                            </section>
                        </div>
                    </div>
                    {/* form3 */}
                    <div className="container" id="form3">
                        <form onSubmit={this.handleSubmit2}>
                            <div className="createform">

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="target">Target Variable</label>
                                    </div>
                                    <div className="col-70">

                                        <input type="text" id="target" name="target" onChange={this.handleTargetChange} placeholder="Enter target variable" required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="modelno">How many top models you want?</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="number" id="modelno" name="modelno" onChange={this.handleModelNumChange} placeholder="Enter number of models" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="text" id="nulltype" name="nulltype" onChange={this.handleNullTypeChange} placeholder="Is it NULL, NA , ? , 0 or other (specify)" required />
                                    </div>
                                </div>

                                <div>
                                    <button type="submit" className="formbutton" id="trainnow" >Train Now</button>
                                </div>
                            </div>
                        </form>
                    </div>
                    {/* loader */}
                    <Result />
                    {/* </div> */}
                    {/* ************************************************************************************************************************ */}
                </div>
                {/* Section3  */}
                <div className="section3" id="section3">
                    <div className="section3box">
                        <h1>Yes, Its that Easy</h1>
                        <video className="section3video" width="640" height="360" controls>
                            <source src={aivideo} type="video/mp4" />
                            <p>Your browser does not support the video tag.</p>
                        </video>
                        <a href='#section2' > <button className=" col-30 section3button">Start Expereince Now &uArr;</button></a>
                    </div>
                </div>
                {/* ************************************************************************************************************************ */}
                {/* Section 4 */}
                <div className="section4" id="section4">
                    <div className="col-50 section4col1">
                        <h1>Curl AutoMl Engine lets you make excellent machine and deep learning models for all your needs with few clicks</h1>
                        <Link to='/#section3' > <button className=" section4button">See Demo</button></Link>
                    </div>
                    <div className="col-50 section4col2">
                        <h3>"The best Part is its Open Source"</h3>
                        <a href='https://github.com/nikzagarwal/Project_21' > <button className=" section4button">Github Repo</button></a>
                    </div>
                </div>
                {/* ************************************************************************************************************************ */}
                {/* Section 5 */}
                <div className="section5 " id="section5">
                    <div className="goback">
                        <button className="sec5btn" onClick={this.handleGoBack}  >&lArr; Go Back to Models </button>

                    </div>
                    <div className="sec5heading">
                        <h1>Results</h1>
                    </div>
                    <div className="container">
                        {/* <!-- Nav tabs --> */}
                        <ul className="nav nav-tabs" id="myTab" role="tablist">
                            <li className="nav-item" role="presentation">
                                <button className="nav-link tabbtn active" id="Metrics-tab" data-bs-toggle="tab" data-bs-target="#metrics" type="button" role="tab" aria-controls="metrics" aria-selected="true">Metrics</button>
                            </li>
                            <li className="nav-item" role="presentation">
                                <button className="nav-link tabbtn " id="plot-tab" data-bs-toggle="tab" data-bs-target="#plot" type="button" role="tab" aria-controls="Plot" aria-selected="false">Plots</button>
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
                            <div className="tab-pane active" id="metrics" role="tabpanel" aria-labelledby="metrics-tab">Metrics will be displayed here</div>
                            <div className="tab-pane" id="plot" role="tabpanel" aria-labelledby="plot-tab">
                                Plots will be displayed here
                                <div className="container">
                                    <div className="d-flex flex-row justify-content-center flex-wrap">
                                        <div className="d-flex flex-column plot" >
                                            <img src="1" className="img-fluid" alt=" Plot1 not for this model " />
                                            <img src="2" className="img-fluid" alt=" Plot2 not for this model " />
                                            <img src="3" className="img-fluid" alt=" Plot3 not for this model " />

                                        </div>
                                        <div className="d-flex flex-column plot" >
                                            <img src="4" className="img-fluid" alt=" Plot4 not for this model " />
                                            <img src="5" className="img-fluid" alt=" Plot5 not for this model " />
                                            <img src="6" className="img-fluid" alt=" Plot6 not for this model " />
                                        </div>

                                    </div>
                                </div>
                            </div>
                            <div className="tab-pane" id="download" role="tabpanel" aria-labelledby="download-tab">

                                <section className=" cards2 ">
                                    <div className="flip-card col-50">
                                        <div className="flip-card-inner ">
                                            <div className="flip-card-front2">
                                                <h1>Clean Data</h1>
                                            </div>
                                            <div className="flip-card-back2 ">
                                                <p>"Download clean Data"</p>
                                                <button className="btn2" id="form2autobutton">Download</button>
                                            </div>
                                        </div>
                                    </div>
                                    <div className="flip-card col-50">
                                        <div className="flip-card-inner">
                                            <div className="flip-card-front2">
                                                <h1>Pickle File</h1>
                                            </div>
                                            <div className="flip-card-back2 ">
                                                <p>"Download pickle file"</p>
                                                <button className="btn2" >Download</button>
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
                                                <div className="col-30">
                                                    <label htmlFor="Inference">Enter data to get Prediction</label>
                                                </div>
                                                <div className="col-70">
                                                    <input type="file" className="form-control" id="inference" onChange={this.handleInferenceChange} accept=".csv" name="inference"
                                                        placeholder="enter training data in csv format" required />
                                                </div>
                                            </div>


                                            <div>
                                                <button type="submit" className="formbutton" id="getresults" >Get Results</button>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>

                        </div>
                    </div >
                </div >
                {/* ************************************************************************************************************************ */}
                {/* Section 6 */}
                <Section6 />

            </div >
        );
    }
}

export default Home;