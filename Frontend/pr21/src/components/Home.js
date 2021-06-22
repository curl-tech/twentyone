import React, { Component } from 'react';
import aivideo from "../assets/videos/AI.mp4";
import $ from 'jquery';
import axios from 'axios';
// import { HashLink as Link } from 'react-router-hash-link';
import Result from './Result.js';
import Section1 from './section1.js';
import Section6 from './section6.js';
import Section5 from './section5.js';
import Papa from 'papaparse';

class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            userID:101,
            projectname: '',
            train: undefined,
            mtype: 'classification',
            auto: true,
            target: '',
            modelnum: 3,
            nulltype: 'NA',
            currentmodel: 1,
            inputdata: ""
        }
        this.updateData = this.updateData.bind(this);
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
        console.log(event.target.files[0]);
    }
    updateData(result) {
        this.setState({
            data: result.data
        });
        var data = result.data;
        // console.log(data);
    }
    handleMtypeChange = event => {
        this.setState({
            mtype: event.target.value
        })
    }
    handleSubmit = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('form1');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form2');
        $(theFormItself2).show();
        const { train } = this.state;
        Papa.parse(train, {
            complete: this.updateData,
            header: true
        });
        const formdata = new FormData();
        formdata.append(
            "userID",
            this.state.userID

        );
        formdata.append(
            "projectName",
            this.state.projectname

        );
        formdata.append(
            "mtype",
            this.state.mtype

        );
        formdata.append(
            "train",
            this.state.train
        );

        console.log(formdata.getAll('train'))

        axios.post('http://localhost:8000/create', formdata, { headers: { 'Accept': 'multipart/form-data', 'Content-Type': 'multipart/form-data' } })
            .then((res) => {console.log("Successful", res)},
                (error) => { console.log(error) });
    }
    handleAuto() {
        var theFormItself = document.getElementById('form2');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).show();
    }
    handleManual() {
        this.setState({
            auto: false
        })
        var theFormItself = document.getElementById('form2');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).show();
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
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('loader');
        $(theFormItself2).show();
        let userID = this.state.userID
        let isauto = this.state.auto
        let target = this.state.target
        let modelnumber = this.state.modelnum
        let nulltype = this.state.nulltype
        let data = { userID, isauto, target, modelnumber, nulltype }
        console.log(JSON.stringify(data))

        axios.post('http://localhost:8000/auto', JSON.stringify(data))
            .then(res => { console.log("Successful", res) },
                (error) => { console.log(error) });
    }
    handleCurrentModel = (val) => {
        this.setState({
            currentmodel: val
        })
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
                        {/* <p>" Just fill relevant feeds and select few choices and you are good to go"</p> */}
                    </div>

                    {/* form1 */}
                    <div className="container " id="form1">
                        <form onSubmit={this.handleSubmit}>
                            <div className="createform">
                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="projectname">Name of your project?</label>
                                    </div>
                                    <div className="col-60">

                                        <input type="text" id="projectname" name="projectname" placeholder="Name your project..." value={this.state.projectname} onChange={this.handleProjectNameChange} required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="train">Enter training data</label>
                                    </div>
                                    <div className="col-60">
                                        <input type="file" className="form-control" id="train" onChange={this.handleTrainChange} accept=".csv" name="train"
                                            placeholder="enter training data in csv format" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="type">Which type of data is it?</label>
                                    </div>
                                    <div className="col-60 ">
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

                            <section className="createform  ">
                                <div className="card-group">
                                    <div className="card flip-card ">
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
                                    <div className=" card flip-card ">
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
                                </div>

                            </section>
                        </div>
                    </div>
                    {/* form3 */}
                    <div className="container" id="form3">
                        <form onSubmit={this.handleSubmit2}>
                            <div className="createform">

                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="target">Target Variable</label>
                                    </div>
                                    <div className="col-60">

                                        <input type="text" id="target" name="target" onChange={this.handleTargetChange} placeholder="Enter target variable" required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="modelno">How many top models you want?</label>
                                    </div>
                                    <div className="col-60" >
                                        <input type="number" id="modelno" name="modelno" onChange={this.handleModelNumChange} placeholder="Enter number of models" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                                    </div>
                                    <div className="col-60" >
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

                    </div>
                    <a href='#section2' > <button className=" col-40 section3button">Start Expereince Now &uArr;</button></a>

                </div>
                {/* ************************************************************************************************************************ */}
                {/* Section 4 */}
                <div className="section4" id="section4">

                    <div className="col-50 section4col1">

                        {/* <Link to='/#section3' > <button className=" section4button">See Demo</button></Link> */}

                    </div>
                    <div className="col-50 section4col2">
                        <h1>Curl AutoMl Engine lets you make excellent machine and deep learning models for all your needs with few clicks</h1>

                        <h3>"The best Part is its Open Source"</h3>
                        <a href='https://github.com/nikzagarwal/Project_21' target="_blank" rel="noopener noreferrer"> <button className=" section4button">Github Repo</button></a>
                    </div>

                </div>
                {/* ************************************************************************************************************************ */}
                {/* Section 5 */}
                <Section5 currentmodel={this.state.currentmodel} />
                {/* ************************************************************************************************************************ */}
                {/* Section 6 */}
                <Section6 modelnum={this.state.modelnum} handler={this.handleCurrentModel} projectname={this.state.projectname} />

            </div >
        );
    }
}

export default Home;