import React, { Component } from 'react';
import { Modal } from 'react-bootstrap';
import { Button } from 'react-bootstrap';
class HyperModal extends Component {
    constructor(props) {
        super(props)
        this.state = {
            reghyper: {
                "LinearRegression": {
                    "1": { "name": "fit_intercept", "value": null, "ishype": false }
                },
                "PolynomialRegression": {
                    "1": { "name": "poly_degree", "value": null, "ishype": false }
                },
                "RandomForest": {
                    "1": { "name": "criterion", "value": null, "ishype": false },
                    "2": { "name": "n_estimators", "value": null, "ishype": false },
                    "3": { "name": "max_depth", "value": null, "ishype": false },
                    "4": { "name": "min_samples_split", "value": null, "ishype": false }
                },
                "DecisionTree": {
                    "1": { "name": "criterion", "value": null, "ishype": false },
                    "2": { "name": "max_deptht", "value": null, "ishype": false },
                    "3": { "name": "min_samples_split", "value": null, "ishype": false },
                },
                "XGBOOST": {
                    "1": { "name": "verbosity", "value": null, "ishype": false },
                    "2": { "name": "booster", "value": null, "ishype": false },
                    "3": { "name": "updater", "value": null, "ishype": false }
                },
                "K-NN": {
                    "1": { "name": "n_neighbors", "value": null, "ishype": false },
                    "2": { "name": "leaf_size", "value": null, "ishype": false },
                    "3": { "name": "algorithm", "value": null, "ishype": false }
                }
            },
            classimodellist: ['LogisticRegression', 'RandomForestClassifier', 'DecisionTree', 'XGBOOST', 'GaussianNB', 'K-NN'],
            classihyper: {
                "LogisticRegression": {
                    "1": { "name": "penalty", "value": null, "ishype": false },
                    "2": { "name": "fit_intercept", "value": null, "ishype": false },
                    "3": { "name": "solver", "value": null, "ishype": false },
                    "4": { "name": "multi_class", "value": null, "ishype": false }
                },
                "RandomForestClassifier": {
                    "1": { "name": "n_estimators", "value": null, "ishype": false },
                    "2": { "name": "max_depth", "value": null, "ishype": false },
                },
                "DecisionTree": {
                    "1": { "name": "max_depth", "value": null, "ishype": false },
                    "2": { "name": "min_samples_split", "value": null, "ishype": false },
                    "3": { "name": "criterion", "value": null, "ishype": false },
                    "4": { "name": "min_samples_leaf", "value": null, "ishype": false }
                },
                "XGBOOST": {
                    "1": { "name": "learning rate", "value": null, "ishype": false },
                    "2": { "name": "max_depth", "value": null, "ishype": false },
                    "3": { "name": "gamma", "value": null, "ishype": false }
                },

                "GaussianNB": {
                    "1": { "name": "var_smoothing", "value": null, "ishype": false },
                },
                "K-NN": {
                    "1": { "name": "n_neighbors", "value": null, "ishype": false },
                    "2": { "name": "leaf_size", "value": null, "ishype": false },
                    "3": { "name": "algorithm", "value": null, "ishype": false }
                }
            }
        }
    }
    render() {
        let model = ""
        const display = []
        if (this.props.show === true) {
            model = this.props.modelName
            const items = this.props.mtype==='classification'?this.state.classihyper[model] :this.state.reghyper[model]
            for (let i = 0; i < Object.keys(items).length; i++) {
                display.push(

                    <div className="row">
                        <div className="col-40">
                            <label htmlFor="outlier">{items[String(i + 1)]["name"]}</label>
                        </div>

                        <div className="col-60" >
                            <input type="text" id="name" name="name" onChange={this.handleNameChange} placeholder="Enter Value" required />
                        </div>
                    </div>


                )
            }

        }
        return (
            <div>
                <Modal
                    {...this.props}
                    size="lg"
                    aria-labelledby="contained-modal-title-vcenter"
                    centered

                >
                    <Modal.Header closeButton>
                        <Modal.Title id="contained-modal-title-vcenter">
                            {model}
                        </Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        <p>Give values to hyperparameters or leave blank for default </p>
                        {display}

                    </Modal.Body>
                    <Modal.Footer>
                        <Button onClick={this.props.onHide}>Done</Button>
                    </Modal.Footer>
                </Modal>

            </div>
        );
    }
}

export default HyperModal;