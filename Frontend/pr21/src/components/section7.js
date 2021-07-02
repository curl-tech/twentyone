import React, { Component } from 'react';
import ProjectsSection6 from './projectsSection6.js';
import ProjectsSection5 from './projectsSection5.js';
import $ from 'jquery';
import axios from 'axios';

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
                0:{
                    "projectID": 45547,
                    "projectName": "Test1",
                    "target": "y",
                    "modelType": "regression",
                    "listOfDataIDs": [13235, 65526],
                    "isAuto": true
                },
                1:{
                    "projectID": 17131,
                    "projectName": "Test2",
                    "target": "y2",
                    "modelType": "classification",
                    "listOfDataIDs": [18036, 52595, 54152],
                    "isAuto": true
                },
                2:{
                    "projectID": 3,
                    "projectName": "Test3",
                    "target": "y3",
                    "modelType": "regression",
                    "listOfDataIDs": [7],
                    "isAuto": false
                }

        },
        }
        this.changeChild=React.createRef()
    }

    componentDidMount(){
        axios.get('http://localhost:8000/getAllProjects?userID=101')
            .then((response) => {
                console.log(response.data)
                this.setState({projectList: response.data});
            });

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

        // this.handleModelDetails(event.target.value)
        
    }
    handleModelDetails= (event,modelnumber) =>{
        console.log(event," ",modelnumber)
        console.log(this.state.projectList[event])
        this.setState({
            currentProjectDetails: {
                "dataID": this.state.projectList[event].listOfDataIDs[modelnumber],
                "modelID": this.state.projectList[event].listOfDataIDs[modelnumber],
                "projectID": this.state.projectList[event].projectID
            }
        })
    }
    handleGoBack = event => {
        var theSectionItself = document.getElementById('modelDetails');
        $(theSectionItself).hide();
        var theSectionItself2 = document.getElementById('projectDetails');
        $(theSectionItself2).show();
        var theFormItself = document.getElementById('projectsection6');
        $(theFormItself).show();

        var theFormItself2 = document.getElementById('projectsection5');
        $(theFormItself2).hide();

        var thebtnItself = document.getElementById('show');
        $(thebtnItself).show();
        // this.child.method()
        this.changeChild.current.method()
        // this.setState({ reset: 1});
    }
    render() {
        const items = []
        let len = Object.keys(this.state.projectList).length;
        // let len=3
        console.log(len)

        for (let i = 0; i < len; i += 3) {
            let item = []
            for (let j = i; j < i + 3 && j < len; j++) {
                item.push(
                    <div className="card sec7card">

                        <div className="card-body">
                            <div className="sec7h2">
                            <h2 className="card-title sec7text">{this.state.projectList[j].projectName}</h2>
                            </div>
                            <div className="sec7h5">
                            <h5 className="card-text cardp sec7text">
                                Target Variable :{this.state.projectList[j].target}
                            </h5>
                            <h5 className="card-text cardp sec7text">
                                Model Type :{this.state.projectList[j].modelType}
                            </h5>
                            <h5 className="card-text cardp sec7text">
                                Creation type :{this.state.projectList[j].isAuto ? "Auto" : "Manual"}
                            </h5>
                            </div>
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
                        <h2>List of all your Projects</h2>
                    </div>

                    {items}
                </div>
                <div className="modelDetails" id="modelDetails">

                    <div className="goback">
                        <button className="backbtn" onClick={this.handleGoBack}  >&lArr; Go Back to Projects </button>

                    </div>
                    <div id="sec6">
                        < ProjectsSection6 handler={this.props.handler} handleModelDetails={this.handleModelDetails} modelnum={this.state.projectList[this.state.currentProject].listOfDataIDs.length} isauto={this.state.projectList[this.state.currentProject].isAuto} projectname={this.state.projectList[this.state.currentProject].projectName} currentproject={this.state.currentProject} />
                    </div>
                    <div id="sec5">
                        < ProjectsSection5 ref={this.changeChild} showRetrain={this.state.showRetrain} currentmodel={this.props.currentmodel} projectdetails={this.state.currentProjectDetails} />
                    </div>
                </div>
            </div>

        );
    }
}

export default Section7;