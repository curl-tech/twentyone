import React, { Component } from 'react';
import $ from 'jquery';

class ProjectsSection6 extends Component {
    handleModelResult = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('projectsection6');
        $(theFormItself).hide();

        var theFormItself2 = document.getElementById('projectsection5');
        $(theFormItself2).show();
        this.props.handler(event.target.value);
        this.props.handleModelDetails(this.props.currentproject,event.target.value-1);
    }
    render() {
        const items = []
        for (let i = 0; i < this.props.modelnum; i += 2) {
            let item = []
            for (let j = i; j < i + 2 && j < this.props.modelnum; j++) {
                item.push(
                    // <div className="card sec6card">
                    //     <div className="card-body">
                    //         <h1 className="card-title">Model {j + 1}</h1>
                    //         <p className="card-text cardp">
                    //             Accuracy :
                    //         </p>
                    //         <button value={j + 1} onClick={this.handleModelResult} className="btn sec6btn">See Details</button>
                    //     </div>
                    // </div>
                    <div key={j} className="card projectsec6autocard">

                        <div className="card-body">
                            <h2 className="card-title">{this.props.isauto === true ? <span>Top Model for run: <em>{j + 1} </em></span> : <span><em>Model: {j + 1}</em></span> }</h2>
                            {/* <h4 className="card-text cardp">See Details For:
                                <li>Metrics</li>
                                <li>Plots</li>
                                <li>Clean Data</li>
                                <li>Pickle File</li>
                                <li>Inferencing New Data</li>
                            </h4> */}
                            <button value={j + 1} onClick={this.handleModelResult} className="btn sec6btn btn-primary">See Details</button>
                        </div>
                    </div>
                )
            }
            items.push(
                <div className="card-group  ">
                    {item}
                </div>
            )

        }
        if (this.props.isauto === false) {
            return (
                <div className="section6" id="projectsection6">


                    <div className=" sec6heading">
                        <h1>Project Name:<em> {this.props.projectname}</em></h1>
                    </div>
                    <div className=" sec6heading">
                        <h1>Your Models</h1>
                    </div>
                    {items}

                </div>
            );
        }
        else {

            return (
                <div className="section6 " id="projectsection6">

                    {/* <div className=" sec6heading">
                        <h1>Results</h1>
                    </div> */}
                    <div className=" sec6heading">
                        <h1>Project Name: <em>{this.props.projectname}</em></h1>
                    </div>
                    {/* <div className=" sec6heading">
                        <h2>The Best Model</h2>
                    </div> */}
                    {items}
                    {/* <div className="card sec6autocard">

                        <div className="card-body">
                            <h2 className="card-title">Top Model</h2>
                            <h4 className="card-text cardp">See Details For:
                                <li>Metrics</li>
                                <li>Plots</li>
                                <li>Clean Data</li>
                                <li>Pickle File</li>
                                <li>Inferencing New Data</li>
                            </h4>
                            <button value={1} onClick={this.handleModelResult} className="btn sec6btn">See Details</button>
                        </div>
                    </div> */}

                </div>
            );
        }
    }
}

export default ProjectsSection6;