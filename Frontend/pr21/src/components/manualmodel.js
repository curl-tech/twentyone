import React, { Component } from 'react';

class ManualModel extends Component {
    constructor(props) {
        super(props)
        this.state = {
            classimodelist: ['Logistic Classification', 'Random Forest', 'Decision Tree', 'Xgboost', 'Naive bayes', 'K-NN'],
            regmodelist: ['Linear Regression', 'Polynomial Regression', 'Random Forest', 'Decision Tree', 'Xgboost', 'K-NN']

        }
    }
    render() {


        if (this.props.mtype === 'classification') {
            const Classificationitems = []
            const len = this.state.classimodelist.length
            for (let i = 0; i < len; i += 3) {
                let item = []
                for (let j = i; j < i + 3 && j < len; j++) {
                    item.push(
                        <div className="card sec6card">

                            <div className="card-body">
                                <h4 className="card-title">{this.state.classimodelist[j]}</h4>
                                <div className="manualmodelcard">
                                    <input type="checkbox" id="automodel" onClick={this.handleAutoModelSelect} name="automodel" />
                                    <label for="automodel"> Select</label>
                                </div>
                            </div>
                        </div>

                    )
                }
                Classificationitems.push(
                    <div className="card-group  text-center">
                        {item}
                    </div>
                )

            }
            return (
                <div>
                    <div id="modellist">
                        {Classificationitems}
                    </div>
                    <button className="preprocessbtn" onClick={this.handleTraining} >Train Now</button>

                </div >
            );
        }
        else if (this.props.mtype === 'regression') {
            const Regressionitems = []
            const len = this.state.regmodelist.length
            for (let i = 0; i < len; i += 3) {
                let item = []
                for (let j = i; j < i + 3 && j < len; j++) {
                    item.push(
                        <div className="card sec6card ">

                            <div className="card-body">
                                <h4 className="card-title">{this.state.regmodelist[j]}</h4>
                                <div className="">
                                    <input type="checkbox" id="automodel" onClick={this.handleAutoModelSelect} name="automodel" />
                                    <label for="automodel"> Select</label>
                                </div>
                            </div>
                        </div>

                    )
                }
                Regressionitems.push(
                    <div className="card-group  text-center">
                        {item}
                    </div>
                )

            }
            return (
                <div>
                    <div id="modellist">
                        {Regressionitems}
                    </div>
                    <button className="preprocessbtn" onClick={this.handleTrain} Train Now></button>

                </div>

            );
        }


    }
}

export default ManualModel;