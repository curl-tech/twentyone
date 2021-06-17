import React, { Component } from 'react';
class Create extends Component {
    render() {
        return (
            <div className="section2" id="section2">
                <div className="createpagebox">
                    <h1>Project Creation</h1>
                    <p>" In this section you can create a new project by giving your own data to us"</p>
                </div>

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
                                <div className="col-70">
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
                                    <input type="text" id="nulltype" name="nulltype" placeholder="Is it NULL, NA , ? , 0 or other (specify)"  required />
                                </div>
                            </div>

                            <div>
                                <input type="submit" id="startengine" value="Train Now" />
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        );

    }
}
export default Create;