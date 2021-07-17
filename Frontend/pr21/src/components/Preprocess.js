import React from 'react';
import $ from 'jquery';
// import axios from 'axios';




class Preprocess extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            preprocessForm: ""
        };
    }
    static getDerivedStateFromProps(nextProps, prevState) {
        if (prevState.preprocessForm === "") {
            return { preprocessForm: Object.values(nextProps)[1] };
        }

        return null;
    }
    handlePreProcess = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('form4');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form5');
        $(theFormItself2).show();
    }
    handleTargetChange = event => {
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "target_column_name": event.target.value
            }
        }
        ))
    }
    handleOutlierChange = event => {
        if (event.target.value === "true")
            var x = true;
        else
            x = false;
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "Remove_outlier": x
            }
        }
        ))
    }
    handleImbalanceChange = event => {
        if (event.target.value === "true")
            var x = true;
        else
            x = false;
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "data_imbalance": x
            }
        }
        ))
    }
    handleFeatureChange = event => {
        if (event.target.value === "true")
            var x = true;
        else
            x = false;
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "feature_selection": x
            }
        }
        ))
    }
    handleDropChange = event => {
        var checkBox = document.getElementById(event.target.value + "drop");
        if (checkBox.checked === true) {
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "drop_column_name": this.state.preprocessForm.drop_column_name.concat([event.target.value])
                }
            }
            ))
        }
        else {
            const id = this.state.preprocessForm.drop_column_name.indexOf(event.target.value);
            console.log(id)
            console.log(this.state.preprocessForm.drop_column_name)
            let x = this.state.preprocessForm.drop_column_name.splice(id + 1)
            let y = this.state.preprocessForm.drop_column_name.splice(0, id)
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "drop_column_name": y.concat(x)
                }
            }
            ))
        }
    }
    handleEncodingChange = event => {
        var checkBox = document.getElementById(event.target.value + "encode");
       
        if (checkBox.checked === true) {
            this.setState(prevState => ({
                preprocessForm: {
                    ...prevState.preprocessForm,
                    "encode_column_name": this.state.preprocessForm.encode_column_name.concat([event.target.value])
                }
            }
            ))
        }
        else{
           const id = this.state.preprocessForm.encode_column_name.indexOf(event.target.value);
            console.log(id)
            console.log(this.state.preprocessForm.encode_column_name)
            let x = this.state.preprocessForm.encode_column_name.splice(id + 1)
            let y = this.state.preprocessForm.encode_column_name.splice(0, id)
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "encode_column_name": y.concat(x)
                }
            }
            ))
        }
    }
    handleScalingChange = event => {
        var checkBox = document.getElementById(event.target.value + "scale");
        if (checkBox.checked === true) {
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "scaling_column_name": this.state.preprocessForm.scaling_column_name.concat([event.target.value])
                }
            }
            ))
        }
        else {
            const id = this.state.preprocessForm.scaling_column_name.indexOf(event.target.value);
            console.log(id)
            console.log(this.state.preprocessForm.scaling_column_name)
            let x = this.state.preprocessForm.scaling_column_name.splice(id + 1)
            let y = this.state.preprocessForm.scaling_column_name.splice(0, id)
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "scaling_column_name": y.concat(x)
                }
            }
            ))
        }
    }
    handleImputationChange = event => {
        var checkBox = document.getElementById(event.target.value + "impute");
        if (checkBox.checked === true) {
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "imputation_column_name": this.state.preprocessForm.imputation_column_name.concat([event.target.value])
                }
            }
            ))
        }
        else {
            const id = this.state.preprocessForm.imputation_column_name.indexOf(event.target.value);
            console.log(id)
            console.log(this.state.preprocessForm.imputation_column_name)
            let x = this.state.preprocessForm.imputation_column_name.splice(id + 1)
            let y = this.state.preprocessForm.imputation_column_name.splice(0, id)
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "imputation_column_name": y.concat(x)
                }
            }
            ))
        }
    }

    render() {
        const rawdata = Object.values(this.props.rawdata);
        // console.log(this.props)
        // console.log(this.props.proprocessForm)
        console.log(this.state.preprocessForm)
        return (
            <div>
                {rawdata.map((data, i) => (
                    i === 1 ? (
                        <div className="preprocesstable " id="preprocesstable">
                            <table>
                                <thead>
                                    <tr>
                                        {Object.keys(data).map((key, i) =>
                                            <th className="dropdown ">
                                                {key}<span className="fa fa-caret-down"></span>
                                                <div className="dropdown-content">
                                                    <div className="prepro">
                                                        <input type="checkbox" id={key + "drop"} name={i + "drop"} value={key} onChange={this.handleDropChange} />
                                                        <label htmlFor={i + "drop"}>Drop Column</label>
                                                    </div>

                                                    <div className="prepro ">
                                                        <input type="checkbox" id={key + "encode"} name={i + "encode"} value={key} onChange={this.handleEncodingChange} />
                                                        <label htmlFor={i + "encode"}>Encode Column <span className="fa fa-caret-right"> </span></label>
                                                        {/* <label>Encode Column  </label>   */}
                                                        <div className="dropdown-content2 " >
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "onehotencode"} name={i + "encode"} />
                                                                <label htmlFor={i + "encode"}>One Hot Encoding</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "label"} name={i + "encode"} />
                                                                <label htmlFor={i + "encode"}>Label Encoding</label>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className="prepro">
                                                        <input type="checkbox" id={key + "scale"} name={i + "scale"} value={key} onChange={this.handleScalingChange} />
                                                        <label htmlFor={i + "scale"}>Scale Column <span className="fa fa-caret-right"> </span></label>

                                                        {/* <label>Scale Column  <span className="fa fa-caret-right"> </span></label> */}
                                                        <div className="dropdown-content2">
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "scale"} name={i + "scale"} />
                                                                <label htmlFor={i + "scale"}>Standarization</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "scale"} name={i + "scale"} />
                                                                <label htmlFor={i + "scale"}>Normalization</label>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className="prepro">
                                                    <input type="checkbox" id={key + "impute"} name={i + "impute"} value={key} onChange={this.handleImputationChange} />
                                                        <label htmlFor={i + "impute"}>Imputation <span className="fa fa-caret-right"> </span></label>
                                                        
                                                        {/* <label>Imputation  <span className="fa fa-caret-right"> </span></label> */}
                                                        <div className="dropdown-content2">
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "imputation"} name={i + "imputation"} />
                                                                <label htmlFor={i + "imputation"}>Mean</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "imputation"} name={i + "imputation"} />
                                                                <label htmlFor={i + "imputation"}>Median</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "imputation"} name={i + "imputation"} />
                                                                <label htmlFor={i + "imputation"}>Most Frequent</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "imputation"} name={i + "imputation"} />
                                                                <label htmlFor={i + "imputation"}>KNN</label>
                                                            </div>

                                                        </div>
                                                    </div>

                                                </div>
                                            </th>

                                        )}
                                    </tr>
                                </thead>

                                {rawdata.map((data, i) => (
                                    i < 5 ? (

                                        <tbody>
                                            <tr>
                                                {Object.keys(data).map((key) =>
                                                    <td>
                                                        {data[key]}

                                                    </td>)}

                                            </tr>

                                        </tbody>) : null))}
                            </table>
                        </div>) : null))}

                <div className="row">
                    <div className="col-40">
                        <label htmlFor="target">Target Variable</label>
                    </div>
                    <div className="col-60">

                        <select name="target" id="target" onChange={this.handleTargetChange}>
                            {Object.keys(rawdata[0]).map((key, i) =>
                                <option value={key}>{key}</option>
                            )}
                        </select>
                    </div>
                </div>
                {/* <div className="row">
                    <div className="col-40">
                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                    </div>
                    <div className="col-60" >
                        <input type="text" id="nulltype" name="nulltype" onChange={this.handleNullTypeChange} placeholder="Is it NULL, NA , ? , 0 or other (specify)" required />
                    </div>
                </div> */}
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="imbalance">Want us to check for data imbalance?</label>
                    </div>
                    <div className="col-60 ">
                        <select name="imbalance" id="imbalance" onChange={this.handleImbalanceChange}>
                            <option value="false">No</option>
                            <option value="true">Yes</option>
                        </select>
                    </div>
                </div>
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="outlier">Check for Outliers?</label>
                    </div>
                    <div className="col-60 ">
                        <select name="outlier" id="outlier" onChange={this.handleOutlierChange}>
                            <option value="true">Yes</option>
                            <option value="false">No</option>
                        </select>
                    </div>
                </div>
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="featureeng">Want us to perform feature engineering?</label>
                    </div>
                    <div className="col-60 ">
                        <select name="featureeng" id="featureeng" onChange={this.handleFeatureChange}>
                            <option value="true">Yes</option>
                            <option value="false">No</option>
                        </select>
                    </div>
                </div>
                <button className="preprocessbtn btn btn-secondary" onClick={this.handlePreProcess} >Preprocess</button>
            </div>
        );
    }
}

export default Preprocess;