import React, { Component } from 'react';
import Section6 from './section6.js';
import Section5 from './section5.js';
import $ from 'jquery';
class Section7 extends Component {
    constructor(props) {
        super(props)
        this.state = {
            currentProject: 0,
            showRetrain: false,
            // reset:0,
            currentProjectDetails: {
                "dataID": 0,
                "modelID": 0,
                "projectID": 0,
            },
            projectList: {
                0: {
                    "projectID": 63479,
                    "projectName": "Nik",
                    "target": "y",
                    "modelType": "regression",
                    "listOFDataIDs":{0:65025, 2:51356, 3:32541},
                    "isAuto": true
                },
                1: {
                    "projectID": 66655,
                    "projectName": "Nik2",
                    "target": "y2",
                    "modelType": "classification",
                    "listOFDataIDs": {0:90662, 5:45452, 6:54152},
                    "isAuto": true
                },
                2: {
                    "projectID": 3,
                    "projectName": "Nik3",
                    "target": "y3",
                    "modelType": "regression",
                    "listOFDataIDs": [7, 8, 9],
                    "isAuto": false
                }

            }
        }

    }
    handleProjectResult = event => {
        this.setState(
            {
                currentProject: event.target.value,
            })
        var theSectionItself = document.getElementById('modelDetails');
        $(theSectionItself).show();
        var theSectionItself2 = document.getElementById('projectDetails');
        $(theSectionItself2).hide();
        
        
        this.setState({
            currentProjectDetails:{
                "dataID":this.state.projectList[event.target.value].listOFDataIDs[0][0],
                "modelID":this.state.projectList[event.target.value].listOFDataIDs[0][0],
                "projectID":this.state.projectList[event.target.value].projectID
            }
        })
    }
    handleGoBack =event=> {
        var theSectionItself = document.getElementById('modelDetails');
        $(theSectionItself).hide();
        var theSectionItself2 = document.getElementById('projectDetails');
        $(theSectionItself2).show();
        var theFormItself = document.getElementById('section6');
        $(theFormItself).show();

        var theFormItself2 = document.getElementById('section5');
        $(theFormItself2).hide();

        var thebtnItself = document.getElementById('show');
        $(thebtnItself).show();
        // this.setState({ reset: 1});
    }
    render() {
        const items = []
        let len = Object.keys(this.state.projectList).length;
        // console.log(len)
        for (let i = 0; i < len; i += 3) {
            let item = []
            for (let j = i; j < i + 3 && j < len; j++) {
                item.push(
                    <div className="card sec7card">

                        <div className="card-body">
                            <h2 className="card-title sec7text">{this.state.projectList[j].projectName}</h2>
                            <h5 className="card-text cardp sec7text">
                                Target Variable :{this.state.projectList[j].target}
                            </h5>
                            <h5 className="card-text cardp sec7text">
                                Model Type :{this.state.projectList[j].modelType}
                            </h5>
                            <h5 className="card-text cardp sec7text">
                                Creation type :{this.state.projectList[j].isAuto ? "Auto" : "Manual"}
                            </h5>
                            <button value={j} onClick={this.handleProjectResult} className="btn sec7btn">See Details</button>
                        </div>
                    </div>

                )
            }
            items.push(
                <div className="card-group  text-center">
                    {item}
                </div>
            )

        }
        return (
            <div className="section7" id="section7">
                <div className="projectDetails" id="projectDetails">
                    <div className=" sec7heading">
                        <h2>List of all the Projects you have trained</h2>
                    </div>

                    {items}
                </div>
                <div className="modelDetails" id="modelDetails">

                    <div className="goback">
                        <button className="backbtn" onClick={this.handleGoBack}  >&lArr; Go Back to Projects </button>

                    </div>
                    <div id="sec6">
                    < Section6  handler={this.props.handler} isauto={this.state.projectList[this.state.currentProject].isAuto} projectname={this.state.projectList[this.state.currentProject].projectName} />
                   </div>
                   <div id="sec5">
                    < Section5 showRetrain={this.state.showRetrain} currentmodel={this.props.currentmodel} projectdetails={this.state.currentProjectDetails} />
                    </div>
                </div>
            </div>

        );
    }
}

export default Section7;