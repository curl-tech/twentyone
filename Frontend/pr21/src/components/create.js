import React, { Component } from 'react';
class Create extends Component {
    render() {
        return (
            <div className="createbody">
                <div>
                    <div className="createpagebox">
                        <h1>Project Creation</h1>
                        <p>" In this section you can create a new project by giving your own data to us"</p>
                    </div>

                    <div className="container">
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
                                        <input type="file" id="train" accept=".csv" name="train"
                                            placeholder="enter training data in csv format" required />
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-30">
                                        <label for="test">Enter test data (if available)</label>
                                    </div>
                                    <div className="col-70" >
                                        <input type="file" id="test" accept=".csv" name="test"
                                            placeholder="enter test data in csv htmlFormat " />
                                    </div>
                                </div>


                                <div className="">
                                    <input type="submit" value="Begin Engine"/>
                                </div>
                            </div>
                        </form>

                    </div>
                </div>
            </div>
        );

    }
}
export default Create;