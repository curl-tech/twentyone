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
                "modelType": "regression"
            },
            projectList: {
                0: {
                    "projectID": 45547,
                    "projectName": "Please Create your first project",
                    "target": "NONE",
                    "modelType": "NONE",
                    "listOfDataIDs": [13235, 65526],
                    "isAuto": true
                },
            },
            emptyProject: true
        }
        this.changeChild = React.createRef()
    }

    componentDidMount() {
        axios.get('http://localhost:8000/getAllProjects?userID=101')
            .then((response) => {
                console.log(response.data)
                if (response.data.length !== 0) {
                    this.setState({
                        projectList: response.data,
                        emptyProject: false
                    });

                }
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
    handleModelDetails = (event, modelnumber) => {
        console.log(event, " ", modelnumber)
        console.log(this.state.projectList[event])
        this.setState({
            currentProjectDetails: {
                "dataID": this.state.projectList[event].listOfDataIDs[modelnumber],
                "modelID": this.state.projectList[event].listOfDataIDs[modelnumber],
                "projectID": this.state.projectList[event].projectID,
                "modelType": this.state.projectList[event].modelType
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
        // console.log(len)

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
                                <table className="projecttable">
                                    <tbody>
                                        <tr>
                                            <td className="firstcol">Target</td>
                                            <td> <em>{this.state.projectList[j].target} </em></td>
                                        </tr>
                                        <tr>
                                            <td className="firstcol">Type</td>
                                            <td> <em>{this.state.projectList[j].modelType}</em></td>
                                        </tr>
                                        <tr>
                                            <td className="firstcol"> Mode</td>
                                            <td> <em>{this.state.projectList[j].isAuto ? "Auto" : "Manual"}</em></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <button value={j} onClick={this.handleProjectResult} className="btn sec7btn btn-primary">See Details</button>
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
        if (this.state.emptyProject === false) {
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
                            <button className="backbtn btn btn-primary" onClick={this.handleGoBack}  > &lArr; Projects </button>

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

        else {
            return (
                <div className="section7" id="section7">
                    <div className="projectDetails" id="projectDetails">
                        <div className=" sec7heading">
                            <h2>List of all your Projects</h2>
                        </div>
                        <div className="card sec7card">
                            <h4 className="emptyproject">Either server is not started or you don't have any previous project</h4>
                            <div class="text-center btnDiv">
                                <a href='#section2' > <button className="btn btn-primary">Create New Project</button></a>
                            </div>
                        </div>

                    </div>
                </div>
            );
        }
    }
}

export default Section7;