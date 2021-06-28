import React, { Component } from 'react';
import $ from 'jquery';
import axios from 'axios';
// import { HashLink as Link } from 'react-router-hash-link';
import Result from './Result.js';
import Preprocess from './Preprocess.js';
import ManualModel from './manualmodel.js';
import Section1 from './section1.js';
import Section3 from './section3.js';
import Section4 from './section4.js';
import Section6 from './section6.js';
import Section5 from './section5.js';
import Papa from 'papaparse';

class Home extends Component {
    constructor(props) {
        super(props)
        this.state = {
            userID: 101,
            projectname: '',
            train: undefined,
            mtype: 'classification',
            auto: true,
            target: '',
            modelnum: 1,
            nulltype: 'NA',
            currentmodel: 1,
            data: "{0:0}",
            metricData: "{0:0}"

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
        // console.log(event.target.files[0]);
    }
    updateData(result) {
        this.setState({
            data: result.data
        });
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

        // console.log(formdata.getAll('train'))

        axios.post('http://localhost:8000/create', formdata, { headers: { 'Accept': 'multipart/form-data', 'Content-Type': 'multipart/form-data' } })
            .then((res) => { console.log("Successful", res) },
                (error) => { console.log(error) });
    }
    handleAuto() {
        var theFormItself = document.getElementById('form2');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form3');
        $(theFormItself2).show();
    }
    handleManual = event => {
        this.setState({
            auto: false
        })
        var theFormItself = document.getElementById('form2');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form4');
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
        // console.log(JSON.stringify(data))

        axios.post('http://localhost:8000/auto', JSON.stringify(data))
            .then(res => { console.log("Successful", res) },
                (error) => { console.log(error) });
        // axios.get('http://localhost:8000/auto')
        //     .then((response) => {
        //         console.log(response.data);
        //         console.log(response.status);
        //         console.log(response.statusText);
        //         console.log(response.headers);
        //         console.log(response.config);
        //     });
        const ws = new WebSocket('ws://localhost:8800/ws')
        ws.onopen = () => {
            // on connecting, do nothing but log it to the console
            console.log('connected')
            this.ws.send("Connected to React");
        }

        ws.onmessage = evt => {
            // listen to data sent from the websocket server
            console.log("getting message")
            const message = JSON.parse(evt.data)
            this.setState({ metricData: message })
            console.log(message)
        }

        ws.onclose = () => {
            console.log('disconnected')
            // automatically try to reconnect on connection loss

        }
    }
    handleCurrentModel = (val) => {
        this.setState({
            currentmodel: val
        })
    }
    handleAutoPreprocess() {
        var theFormItself = document.getElementById('preprocesstable');
        $(theFormItself).toggle();

    }
    handleAutoModelSelect() {
        var theFormItself = document.getElementById('modellist');
        $(theFormItself).toggle();

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
                                        <label htmlFor="projectname">Name of your project? <span className="ibtn">i <span id="idesc">Enter any relevant name for your project</span></span></label>
                                    </div>
                                    <div className="col-60">

                                        <input type="text" id="projectname" name="projectname" placeholder="Name your project..." value={this.state.projectname} onChange={this.handleProjectNameChange} required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="train">Enter training data <span className="ibtn">i <span id="idesc">Enter the data on which you want to train your model</span></span></label>
                                    </div>
                                    <div className="col-60">
                                        <input type="file" className="form-control" id="train" onChange={this.handleTrainChange} accept=".csv" name="train"
                                            placeholder="enter training data in csv format" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="type">Which type of data is it? <span className="ibtn">i <span id="idesc">Genrally if no. of classes less than 10 for target its Classification</span></span></label>
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
                                        <select name="target" id="target" onChange={this.handleTargetChange}>
                                            {Object.keys(this.state.data[0]).map((key, i) =>
                                                <option value={key}>{key}</option>
                                            )}
                                        </select>
                                        {/* <input type="text" id="target" name="target" onChange={this.handleTargetChange} placeholder="Enter target variable" required /> */}
                                    </div>
                                </div>

                                {/* <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="modelno">How many top models you want?</label>
                                    </div>
                                    <div className="col-60" >
                                        <input type="number" id="modelno" name="modelno" onChange={this.handleModelNumChange} placeholder="Enter number of models" required />
                                    </div>
                                </div> */}
                                {/* <div className="row">
                                    <div className="col-40">
                                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                                    </div>
                                    <div className="col-60" >
                                        <input type="text" id="nulltype" name="nulltype" onChange={this.handleNullTypeChange} placeholder="Is it NULL, NA , ? , 0 or other (specify)"  />
                                    </div>
                                </div> */}

                                <div>
                                    <button type="submit" className="formbutton" id="trainnow" >Train Now</button>
                                </div>
                            </div>
                        </form>
                    </div>
                    {/* loader */}
                    <Result modelnum={this.state.modelnum} handler={this.handleCurrentModel} projectname={this.state.projectname} isauto={this.state.isauto} />
                    {/* ************************************************************************************************************************ */}

                    {/* form 4 for manual preprocessing */}
                    <div className="container" id="form4">
                        <div className="PreprocessForm">
                            <div className="autocheckbox">
                                <input type="checkbox" id="autopreprocess" onClick={this.handleAutoPreprocess} name="autopreprocess" />
                                <label htmlFor="autopreprocess"> Auto Preprocess</label>
                            </div>
                            <h1>Preprocess</h1>
                            <p>Go to each column and decide how would you like to preprocess it</p>
                            <Preprocess rawdata={this.state.data} />
                        </div>
                    </div>
                    {/* form 5 for model and hypeparameters selection*/}
                    <div className="container" id="form5">
                        <div className="Modelselection">
                            <div className="autocheckbox">
                                <input type="checkbox" id="automodel" onClick={this.handleAutoModelSelect} name="automodel" />
                                <label htmlFor="automodel"> Auto Models</label>
                            </div>
                            <h1>Models</h1>
                            <p>Preprocessing is being done. Now, select models and their hyperparameters</p>
                            <ManualModel mtype={this.state.mtype} />
                        </div>
                    </div>

                    {/* ************************************************************************************************************************ */}
                </div>
                {/* Section3  */}
                {/* This section is for showing demo video */}
                <Section3 />
                {/* ************************************************************************************************************************ */}
                {/* Section 4 */}
                {/* This Section id for About */}
                <Section4 />
                {/* ************************************************************************************************************************ */}
                {/* Section 5 */}
                {/* This section is to show detail of every trained model */}
                <Section5 currentmodel={this.state.currentmodel} />
                {/* ************************************************************************************************************************ */}
                {/* Section 6 */}
                {/* This section is to show all models trained */}
                <Section6 modelnum={this.state.modelnum} handler={this.handleCurrentModel} projectname={this.state.projectname} isauto={this.state.isauto} />

            </div >
        );
    }
}

export default Home;