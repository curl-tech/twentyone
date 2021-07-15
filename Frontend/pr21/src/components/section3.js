import React, { Component } from 'react';
import aivideo from "../assets/videos/curl21.mp4";
class Section3 extends Component {
    render() {
        return (
            <div className="section3 " id="section3">
               
                    <div className="  section3box">
                        <h1>Yes, Its that Easy</h1>
                        <br/>
                        <br/>
                        <video className="section3video" width="640" height="320" controls>
                            <source src={aivideo} type="video/mp4" />
                            <p>Your browser does not support the video tag.</p>
                        </video>
                    </div>
                    <div class="text-center btnDiv">
                    <a href='#section2' > <button className="btn btn-primary section3button">Start Experience</button></a>
                    </div>
            </div>
        );
    }
}

export default Section3;