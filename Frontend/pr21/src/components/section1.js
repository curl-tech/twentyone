import React, { Component } from 'react';

class Section1 extends Component {
    render() {
        return (
            <div className="section1">
                <div className="container typing-text">
                    <p>Curl Brings <span className="typed-text"></span><span className="cursor">&nbsp;</span></p>
                    <p>Together under one Umbrella</p>
                    <div className="section1text1">The Easy to go auto-ml engine for all your data, it creates end to end experience of machine and deep learning without a single line of code</div>
                    <div className="sec1btn-group">
                        <a href='#section2'> <button className="  btn  section1button section1button2">Start Expereince </button></a>
                        <a href='#section3'> <button className=" btn btn-primary section1button section1button2 ">View Demo </button></a>
                    </div>
                </div>
            </div>
        );
    }
}

export default Section1;