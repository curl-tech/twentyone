import React, { Component } from 'react';
import Section6 from './section6.js';
import Section5 from './section5.js';

class Result extends Component {
   
    render() {

        if (this.props.projectdetail["Successful"] === "False")
            return (
                <div className="container loader" id="loader">
                    <p>" Your models are been created... Can we take a quick Tea Break ?? "</p>
                    <div className="centered spinner-location">
                        <div className="spinner-border text-dark spinner-border-lg" role="status">
                            <span className="loadertext">Loading...</span>
                        </div>
                    </div>

                </div>
            );
        else {
            return (
                <div>
                    <Section6 modelnum={this.props.modelnum} handler={this.props.handler}  projectname={this.props.projectname} isauto={this.props.isauto} />
                    <Section5 currentmodel={this.props.currentmodel}  projectdetails={this.props.projectdetail} />
                </div>
            );
        }
    }
}

export default Result;