import React, { Component } from 'react';
import aivideo from "../assets/videos/AI.mp4";
import $ from 'jquery';
import axios from 'axios'
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
        let projectname = this.state.projectname
        let train = this.state.train
        let mtype = this.state.mtype
        let data = { projectname, train, mtype }
        console.log(data)
        axios({
            url: `https://localhost:8800/create`,
            method: "POST",
            headers:
            {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: this.state
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
        $(theFormItself2).fadeIn(3000);
    }
    handleManual() {
        this.setState({
            auto: false
        })
        var theFormItself = document.getElementById('form2');
        $(theFormItself).fadeOut(1000);
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).fadeIn(3000);
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
        let isauto = this.state.auto
        let target = this.state.target
        let modelnumber = this.state.modelnum
        let nulltype = this.state.nulltype
        let data = { isauto, target, modelnumber, nulltype }
        console.log(data)
        axios({
            url: `https://localhost:8800/create`,
            method: "POST",
            headers:
            {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: this.state
        }).then((res) => {
            res.json().then((result) => {
                console.log("result", result)
            })
        })
    }

    render() {
        return (
            <div>
                {/* Section1 */}
                <div className="section1">
                    <div className="container typing-text">
                        <p>Curl Brings <span className="typed-text"></span><span className="cursor">&nbsp;</span></p>
                        <p>Together under one Umbrella</p>
                        <div className="section1text1">The Easy to go auto-ml engine for all your data, it creates end to end experiencce of machine and deep elarning without a single line of code</div>
                        <a href='#section2'> <button className=" col-30 section1button">Start Expereince &dArr;</button></a>
                        <a href='#section3'> <button className="col-30 section1button ">View Demo &dArr;</button></a>

                    </div>
                    {/* <Link to="#section2"><button className="section1button">Start Experience &dArr;</button></Link> */}
                </div>

                <div className="section2" id="section2">
                    <div className="createpagebox">
                        <h1>Start With Your Project</h1>
                        <p>" Just fill relevant feeds and select few choices and you are good to go"</p>
                    </div>
                    {/* Section2  */}
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
                    <div className="container" id="loader">
                        <div className="centered createform">
                            <div class="spinner-border text-primary" role="status">
                                <span class="sr-only">Loading...</span>
                            </div>
                        </div>
                    </div>

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
                {/* Section 4 */}
                <div className="section4" id="section4">
                    <div className="col-50 section4col1">
                        <h1>Curl AutoMl Engine lets you make excellent machine and deep learning models for all your needs with few clicks</h1>
                    </div>
                    <div className="col-50 section4col2">
                        <h3>"The best Part is its Open Source"</h3>
                        <a href='https://github.com/nikzagarwal/Project_21' > <button className=" section4button">Github Repo</button></a>
                    </div>
                </div>

            </div>
        );
    }
}

export default Home;