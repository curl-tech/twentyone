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
        for (let i = 0; i < this.props.modelnum; i+=3) 
        {
            let item=[]
            for (let j=i; j < i+3 && j<this.props.modelnum; j++) {
                item.push(
                    <div className="card sec6card">

                        <div className="card-body">
                            <h5 className="card-title">Model {j+1}</h5>
                            <p className="card-text">
                                Accuracy Train:
                           <br />
                           Accuracy Test:
                         </p>
                            <button value={j+1} onClick={this.handleModelResult} className="btn sec6btn">See Details</button>
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
            <div className="section6" id="section6">

                <div className=" sec6heading">
                    <h1>Results</h1>
                </div>
                <div className=" sec6heading">
                    <h2>Project Name: {this.props.projectname}</h2>
                </div>
                <div className=" sec6heading">
                    <h2>Your Top Models</h2>
                </div>
                {items}
                {/* <div className="card-group  text-center">

                    {items}

                </div> */}

            </div>
        );
    }
}

export default Section6;