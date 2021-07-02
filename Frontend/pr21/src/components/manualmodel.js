import React, { Component } from 'react';
import HyperModal from './hypermodal.js';
class ManualModel extends Component {
    constructor(props) {
        super(props)
        this.state = {
            classimodellist: ['LogisticRegression', 'RandomForestClassifier', 'DecisionTree', 'XGBOOST', 'GaussianNB', 'K-NN'],
            regmodellist: ['LinearRegression', 'PolynomialRegression', 'RandomForest', 'DecisionTree', 'XGBOOST', 'K-NN'],
            modalShow: false,
            currentModel:""
        }
    }
    handlehyperselection= event=>{
        var checkbox = event.target;
        if(checkbox.checked){
            this.setState({modalShow: true })
            this.setState({currentModel: event.target.value }) 
        }
        else{
            this.setState({modalShow: false })
        }
    }
    render() {


        if (this.props.mtype === 'classification') {
            const Classificationitems = []
            const len = this.state.classimodellist.length
            for (let i = 0; i < len; i += 3) {
                let item = []
                for (let j = i; j < i + 3 && j < len; j++) {
                    item.push(
                        <div className="card sec6card manualcard">

                            <div className="card-body">
                                <h4 className="card-title">{this.state.classimodellist[j]}</h4>
                                <div className="manualmodelcard">
                                    <input type="checkbox" id="automodel" value={this.state.classimodellist[j]} onClick={this.handlehyperselection} name="automodel" />
                                    <label htmlFor="automodel" > Select</label>
                                    <HyperModal
                                        show={this.state.modalShow}
                                        onHide={() => this.setState({ modalShow: false })}
                                        modelName={this.state.currentModel}
                                        mtype={this.props.mtype}
                                    />
                                </div>
                            </div>
                        </div>


                    )
                }
                Classificationitems.push(
                    <div className="card-group text-center">
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
            const len = this.state.regmodellist.length
            for (let i = 0; i < len; i += 3) {
                let item = []
                for (let j = i; j < i + 3 && j < len; j++) {
                    item.push(
                        <div className="card sec6card manualcard">

                            <div className="card-body">
                                <h4 className="card-title heading">{this.state.regmodellist[j]}</h4>
                                <div className="manualmodelcard">
                                    <input type="checkbox" id="automodel" value={this.state.regmodellist[j]} onClick={this.handlehyperselection} name="automodel" />
                                    <label htmlFor="automodel"> Select</label>
                                    <HyperModal
                                        show={this.state.modalShow}
                                        onHide={() => this.setState({ modalShow: false })}
                                        modelName={this.state.currentModel}
                                        mtype={this.props.mtype}
                                    />
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
                    <button className="preprocessbtn" onClick={this.handleTrain}> Train Now</button>

                </div>

            );
        }


    }
}

export default ManualModel;