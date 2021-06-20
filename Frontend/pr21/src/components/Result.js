import React, { Component } from 'react';
import Section6 from './section6.js';
 
class Result extends Component {
    constructor(props) {

        super(props);

        this.state = {
            items: [],
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

    }
  render() {
    const { isLoaded, items } = this.state;

    if (!isLoaded)
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
          <Section6 items={items}/>
      </div>  
    );
  }
}
 
export default Result;