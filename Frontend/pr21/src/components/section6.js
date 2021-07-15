import React, { Component } from 'react';
import $ from 'jquery';

class Section6 extends Component {
    handleModelResult = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('section6');
        $(theFormItself).hide();

        var theFormItself2 = document.getElementById('section5');
        $(theFormItself2).show();
        this.props.handler(event.target.value);

        

    }
    render() {
        const items = []
        for (let i = 0; i < this.props.modelnum; i += 3) {
            let item = []
            for (let j = i; j < i + 3 && j < this.props.modelnum; j++) {
                item.push(
                    <div className="card sec6card">

                        <div className="card-body">
                            <h1 className="card-title">Model {j + 1}</h1>
                            <p className="card-text cardp">
                                Accuracy :

                            </p>
                            <button value={j + 1} onClick={this.handleModelResult} className="btn sec6btn">See Details</button>
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
        if (this.props.isauto === false) {
            return (
                <div className="section6" id="section6">

                    
                    <div className=" sec6heading">
                        <h2>Project Name: {this.props.projectname}</h2>
                    </div>
                    <div className=" sec6heading">
                        <h2>Your Models</h2>
                    </div>
                    {items}

                </div>
            );
        }
        else {
            return (
                <div className="section6 " id="section6">

                    {/* <div className=" sec6heading">
                        <h1>Results</h1>
                    </div> */}
                    <div className=" sec6heading">
                        <h1>Project Name: {this.props.projectname}</h1>
                    </div>
                    {/* <div className=" sec6heading">
                        <h2>The Best Model</h2>
                    </div> */}

                    <div className="card sec6autocard">

                        <div className="card-body">
                            <h2 className="card-title">Top Model</h2>
                            <h4 className="card-text cardp">See Details For:
                                <li>Metrics</li>
                                <li>Plots</li>
                                <li>Clean Data</li>
                                <li>Pickle File</li>
                                <li>Inferencing New Data</li>
                            </h4>
                            <button value={1} onClick={this.handleModelResult} className="btn sec6btn btn-primary">See Details</button>
                        </div>
                    </div>

                </div>
            );
        }
    }
}

export default Section6;