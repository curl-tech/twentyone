import React, { Component } from 'react';
import aivideo from "../assets/videos/AI.mp4";
class Home extends Component {
    render() {
        return (
            <div>
                {/* Section1 */}
                <div className="section1">
                    <div className="container typing-text">
                        <p>Curl Brings <span className="typed-text"></span><span className="cursor">&nbsp;</span></p>
                        <p>Together under one Umbrella</p>
                        <div className="section1text1">The Easy to go auto-ml engine for all your data, it creates end to end experiencce of machine and deep elarning without a single line of code</div>
                        <a href='#section2'> <button className=" col-30 section1button">Start Expereince &dArr;</button></a>
                        <a href='#section3'> <button className="col-30 section1button ">View Demo &dArr;</button></a>

                    </div>
                    {/* <Link to="#section2"><button className="section1button">Start Experience &dArr;</button></Link> */}
                </div>

                <div className="section2" id="section2">
                    <div className="createpagebox">
                        <h1>Start With Your Project</h1>
                        <p>" Just fill relevant feeds and select few choices and you are good to go"</p>
                    </div>
                    {/* Section2  */}
                    <div className="container " id="form1">
                        <form>
                            <div className="createform">
                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="name">Name of your project?</label>
                                    </div>
                                    <div className="col-70">

                                        <input type="text" id="name" name="name" placeholder="Name your project..." required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="train">Enter training data</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="file" className="form-control" id="train" accept=".csv" name="train"
                                            placeholder="enter training data in csv format" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-30">
                                        <label for="type">Which type of data is it?</label>
                                    </div>
                                    <div className="col-70 ">
                                        <select name="mtype" id="modeltype" onchange="myFunction(this)">
                                            <option value="classification">Classification</option>
                                            <option value="regression">Regression</option>
                                        </select>

                                    </div>
                                </div>

                                <div>
                                    <input type="submit" id="startengine" value="Begin Engine" />
                                </div>
                            </div>
                        </form>
                    </div>
                    <br></br>
                    <div className="container" id="form2">
                        <div className="centered ">

                            <section className="createform cards ">
                                <div className="flip-card col-50">
                                    <div className="flip-card-inner">
                                        <div className="flip-card-front">
                                            <h1>Auto</h1>
                                        </div>
                                        <div className="flip-card-back">
                                            <p>"Leave everything on us and see the beauty of artificial Intelligence"</p>
                                            <button className="btn2" id="form2button">Select</button>
                                        </div>
                                    </div>
                                </div>
                                <div className="flip-card col-50">
                                    <div className="flip-card-inner">
                                        <div className="flip-card-front">
                                            <h1>Manual</h1>
                                        </div>
                                        <div className="flip-card-back">
                                            <p>"We believe you are always the boss and choose to make models as you wish"</p>
                                            <button className="btn2">Select</button>
                                        </div>
                                    </div>
                                </div>

                            </section>
                        </div>
                    </div>
                    <br></br>
                    <div className="container" id="form3">
                        <form>
                            <div className="createform">

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="target">Target Variable</label>
                                    </div>
                                    <div className="col-70">

                                        <input type="text" id="target" name="target" placeholder="Enter target variable" required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="modelno">How many top models you want?</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="number" id="modelno" name="modelno" placeholder="Enter number of models" required />
                                    </div>
                                </div>
                                <div className="row">
                                    <div className="col-30">
                                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="text" id="nulltype" name="nulltype" placeholder="Is it NULL, NA , ? , 0 or other (specify)" required />
                                    </div>
                                </div>

                                <div>
                                    <input type="submit" id="startengine" value="Train Now" />
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                {/* Section2  */}
                <div className="section3" id="section3">
                    <div className="section3box">
                        <h1>Yes, Its that Easy</h1>
                        <video className="section3video" width="640" height="360" autoplay controls>
                            <source src={aivideo} type="video/mp4" />
                            <p>Your browser does not support the video tag.</p>
                        </video>
                        <a href='#section2' > <button className=" col-30 section3button">Start Expereince Now &uArr;</button></a>
                    </div>
                </div>
            </div>
        );
    }
}
export default Home;