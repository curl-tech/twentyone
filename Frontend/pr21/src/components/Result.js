import React, { Component } from 'react';
import Section6 from './section6.js';

class Result extends Component {
    constructor(props) {

        super(props);

        this.state = {
            metricData: undefined,
            isLoaded: false
        }

    }
    
    componentDidMount() {

        // fetch('https://localhost:8800/auto')
        //     .then(res => res.json())
        //     .then(json => {
        //         this.setState({
        //             items: json,
        //             isLoaded: true, 
        //         })
        //     }).catch((err) => {
        //         console.log(err);
        //     });
        const ws = new WebSocket('ws://localhost:8000/ws')
        ws.onopen = () => {
            // on connecting, do nothing but log it to the console
            console.log('connected')
            ws.send("Connected to React");
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
    render() {

        if (!this.state.isLoaded)
            return (
                <div className="container loader" id="loader">
                    <p>" Your models are been created... Can we take a quick Tea Break ?? "</p>
                    <div className="centered spinner-location">
                        <div className="spinner-border text-dark spinner-border-lg" role="status">
                            <span className="sr-only">Loading...</span>
                        </div>
                    </div>

                </div>
            );
        return (
            <div>
                <Section6 metricData={this.state.metricData} modelnum={this.props.modelnum} handler={this.props.handler} projectname={this.props.projectname} isauto={this.props.isauto} />
            </div>
        );
    }
}

export default Result;