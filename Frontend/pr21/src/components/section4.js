import React, { Component } from 'react';

class Section4 extends Component {
    render() {
        return (
            <div className="section4" id="section4">

                {/* <div className="col-50 section4col1"> */}

                {/* <Link to='/#section3' > <button className=" section4button">See Demo</button></Link> */}

                {/* </div> */}
                <div className="section4col2">
                    <h1>Curl brings to you TwentyOne that lets you make excellent machine learning models for all your business and needs with few simple clicks</h1>
                    <br />
                    <h3>"The best Part is its Open Source"</h3>
                    <a href='https://github.com/nikzagarwal/Project_21' target="_blank" rel="noopener noreferrer"> <button className="btn btn-primary section4button">Github Repo</button></a>
                </div>

            </div>
        );
    }
}

export default Section4;