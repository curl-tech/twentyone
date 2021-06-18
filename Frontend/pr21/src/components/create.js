import React, { Component } from 'react';
import $ from 'jquery';
import axios from 'axios'
class Create extends Component {
    
    constructor(props) {
        super(props)
        this.state = {
            projectname: '',
            train: null,
            mtype: 'classification',
            auto: true,

        }
    }
    handleProjectNameChange = event => {
        this.setState({
            projectname: event.target.value
        })
    }
    handleTrainChange = event => {
        this.setState({
            train:event.target.files[0]
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
        let projectname=this.state.projectname
        let train=this.state.train
        let mtype=this.state.mtype
        let data={projectname,train,mtype}
        console.log(data)
        axios({
            url:`https://localhost:8800/create`,
            method:"POST",
            headers: 
            {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body:this.state
            }).then((res)=>{
                res.json().then((result)=>{
                  console.log("result",result)
                })
        }) 
    }
    handleAuto = event => {
        var theFormItself = document.getElementById('form2');
        $( theFormItself ).fadeOut( 2000 );
        var theFormItself2 = document.getElementById('form3');
        $( theFormItself2).fadeIn( 5000 );
    } 
    handleManual = event => {
        var theFormItself = document.getElementById('form2');
        $( theFormItself ).fadeOut( 1000 );
        var theFormItself2 = document.getElementById('form3');
        $( theFormItself2).fadeIn( 3000 );
    } 


    render() {
        return (
            <div className="section2" id="section2">
                <div className="createpagebox">
                    <h1>Project Creation</h1>
                    <p>" In this section you can create a new project by giving your own data to us"</p>
                </div>

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
                                    <input type="file" className="form-control" id="train"  onChange={this.handleTrainChange} accept=".csv" name="train"
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
                                <button type="submit" className="form1button" id="startengine" >Begin Engine </button>
                            </div>
                        </div>
                    </form>
                </div>
                <br></br>
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
                <br></br>
                <div className="container" id="form3">
                    <form>
                        <div className="createform">

                            <div className="row">
                                <div className="col-30">
                                    <label htmlFor="target">Target Variable</label>
                                </div>
                                <div className="col-70">

                                    <input type="text" id="target" name="target" placeholder="Enter target variable" required />
                                </div>
                            </div>

                            <div className="row">
                                <div className="col-30">
                                    <label htmlFor="modelno">How many top models you want?</label>
                                </div>
                                <div className="col-70" >
                                    <input type="number" id="modelno" name="modelno" placeholder="Enter number of models" required />
                                </div>
                            </div>
                            <div className="row">
                                <div className="col-30">
                                    <label htmlFor="nulltype">How are null values specified in dataset?</label>
                                </div>
                                <div className="col-70" >
                                    <input type="text" id="nulltype" name="nulltype" placeholder="Is it NULL, NA , ? , 0 or other (specify)" required />
                                </div>
                            </div>

                            <div>
                                <input type="submit" id="startengine" value="Train Now" />
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        );

    }
}
export default Create;