import React, { Component } from 'react';
import aivideo from "../assets/videos/AI.mp4";
class Section3 extends Component {
    render() {
        return (
            <div className="section3" id="section3">
            <div className="section3box">
                <h1>Yes, Its that Easy</h1>
                <video className="section3video" width="640" height="360" controls>
                    <source src={aivideo} type="video/mp4" />
                    <p>Your browser does not support the video tag.</p>
                </video>

            </div>
            <a href='#section2' > <button className=" col-40 section3button">Start Expereince Now &uArr;</button></a>

        </div>  
        );
    }
}

export default Section3;