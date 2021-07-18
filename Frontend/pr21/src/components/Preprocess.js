import React from 'react';
import $ from 'jquery';
import axios from 'axios';




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
        if (this.props.automanualpreprocess === true) {
            this.setState(prevState => ({

                preprocessForm: {
                    ...prevState.preprocessForm,
                    "is_auto_preprocess": true
                }
            }
            ))
        }
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "projectID": this.props.projectdetail.projectID,
                "userID": this.props.projectdetail.userID,
                   
            }

        }
        ))

        console.log(JSON.stringify(this.state.preprocessForm))

        axios.post('http://localhost:8000/getHyperparams', JSON.stringify(this.state.preprocessForm))
            .then(res => {
                console.log("Successful2", res)
                this.props.handleModelForm(res.data)
            },
                (error) => { console.log(error) });




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
    handleSplitChange = event => {
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "split_ratio_test": event.target.value
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
    handleEncodingChange = (key) => event => {
        var checkBox = document.getElementById(key + "encode");
        const rbs = document.querySelectorAll('input[name=' + "\"" + key + 'encodetype"]');
        let selectedValue;
        if (key !== 0) {
            for (const rb of rbs) {
                if (rb.checked) {
                    selectedValue = rb.value;
                    break;
                }
            }
            if (checkBox.checked === false)
                checkBox.checked = true;
            if (checkBox.checked === true) {
                const id = this.state.preprocessForm.encode_column_name.indexOf(key);

                if (id !== -1) {
                    let x = this.state.preprocessForm.encoding_type.splice(id + 1)
                    let y = this.state.preprocessForm.encoding_type.splice(0, id)
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "encoding_type": y.concat([selectedValue]).concat(x)
                        }
                    }
                    ))
                }
                else {
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "encode_column_name": this.state.preprocessForm.encode_column_name.concat([key]),
                            "encoding_type": this.state.preprocessForm.encoding_type.concat([selectedValue])
                        }
                    }
                    ))

                }
            }
        }

    }


    handleEncodingRemove = event => {
        const id = this.state.preprocessForm.encode_column_name.indexOf(event.target.value);
        const rbs = document.querySelectorAll('input[name=' + "\"" + event.target.value + 'encodetype"]');
        for (const rb of rbs) {
            rb.checked = false;
        }
        let x = this.state.preprocessForm.encode_column_name.splice(id + 1)
        let y = this.state.preprocessForm.encode_column_name.splice(0, id)
        let x2 = this.state.preprocessForm.encoding_type.splice(id + 1)
        let y2 = this.state.preprocessForm.encoding_type.splice(0, id)
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "encode_column_name": y.concat(x),
                "encoding_type": y2.concat(x2)
            }
        }
        ))

    }
    handleScalingChange = (key) => event => {
        var checkBox = document.getElementById(key + "scale");
        const rbs = document.querySelectorAll('input[name=' + "\"" + key + 'scaletype"]');
        let selectedValue;
        if (key !== 0) {
            for (const rb of rbs) {
                if (rb.checked) {
                    selectedValue = rb.value;
                    break;
                }
            }
            if (checkBox.checked === false)
                checkBox.checked = true;
            if (checkBox.checked === true) {
                const id = this.state.preprocessForm.scaling_column_name.indexOf(key);

                if (id !== -1) {
                    let x = this.state.preprocessForm.scaling_type.splice(id + 1)
                    let y = this.state.preprocessForm.scaling_type.splice(0, id)
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "scaling_type": y.concat([selectedValue]).concat(x)
                        }
                    }
                    ))
                }
                else {
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "scaling_column_name": this.state.preprocessForm.scaling_column_name.concat([key]),
                            "scaling_type": this.state.preprocessForm.scaling_type.concat([selectedValue])
                        }
                    }
                    ))

                }
            }
        }
    }
    handleScalingRemove = event => {
        const id = this.state.preprocessForm.scaling_column_name.indexOf(event.target.value);
        const rbs = document.querySelectorAll('input[name=' + "\"" + event.target.value + 'scaletype"]');
        for (const rb of rbs) {
            rb.checked = false;
        }
        let x = this.state.preprocessForm.scaling_column_name.splice(id + 1)
        let y = this.state.preprocessForm.scaling_column_name.splice(0, id)
        let x2 = this.state.preprocessForm.scaling_type.splice(id + 1)
        let y2 = this.state.preprocessForm.scaling_type.splice(0, id)
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "scaling_column_name": y.concat(x),
                "scaling_type": y2.concat(x2)
            }
        }
        ))

    }
    handleImputationChange = (key) => event => {
        var checkBox = document.getElementById(key + "impute");
        const rbs = document.querySelectorAll('input[name=' + "\"" + key + 'imputetype"]');
        let selectedValue;
        if (key !== 0) {
            for (const rb of rbs) {
                if (rb.checked) {
                    selectedValue = rb.value;
                    break;
                }
            }
            if (checkBox.checked === false)
                checkBox.checked = true;
            if (checkBox.checked === true) {
                const id = this.state.preprocessForm.imputation_column_name.indexOf(key);

                if (id !== -1) {
                    let x = this.state.preprocessForm.impution_type.splice(id + 1)
                    let y = this.state.preprocessForm.impution_type.splice(0, id)
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "impution_type": y.concat([selectedValue]).concat(x)
                        }
                    }
                    ))
                }
                else {
                    this.setState(prevState => ({
                        preprocessForm: {
                            ...prevState.preprocessForm,
                            "imputation_column_name": this.state.preprocessForm.imputation_column_name.concat([key]),
                            "impution_type": this.state.preprocessForm.impution_type.concat([selectedValue])
                        }
                    }
                    ))

                }
            }
        }
    }
    handleImputationRemove = event => {
        const id = this.state.preprocessForm.imputation_column_name.indexOf(event.target.value);
        const rbs = document.querySelectorAll('input[name=' + "\"" + event.target.value + 'imputetype"]');
        for (const rb of rbs) {
            rb.checked = false;
        }
        let x = this.state.preprocessForm.imputation_column_name.splice(id + 1)
        let y = this.state.preprocessForm.imputation_column_name.splice(0, id)
        let x2 = this.state.preprocessForm.impution_type.splice(id + 1)
        let y2 = this.state.preprocessForm.impution_type.splice(0, id)
        this.setState(prevState => ({

            preprocessForm: {
                ...prevState.preprocessForm,
                "imputation_column_name": y.concat(x),
                "impution_type": y2.concat(x2)
            }
        }
        ))

    }
    render() {
        const rawdata = Object.values(this.props.rawdata);
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
                                                        <input type="checkbox" id={key + "encode"} name={key + "encode"} value={key} onChange={this.handleEncodingRemove} />
                                                        <label htmlFor={i + "encode"}>Encode Column <span className="fa fa-caret-right"> </span></label>
                                                        {/* <label>Encode Column  </label>   */}
                                                        <div className="dropdown-content2 " >
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "onehotencode"} name={key + "encodetype"} value="One-Hot Encoding" onChange={this.handleEncodingChange(key)} />
                                                                <label htmlFor={i + "encode"}>One Hot Encoding</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "label"} name={key + "encodetype"} value="Label Encodeing" onChange={this.handleEncodingChange(key)} />
                                                                <label htmlFor={i + "encode"}>Label Encoding</label>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className="prepro">
                                                        <input type="checkbox" id={key + "scale"} name={key + "scale"} value={key} onChange={this.handleScalingRemove} />
                                                        <label htmlFor={i + "scale"}>Scale Column <span className="fa fa-caret-right"> </span></label>

                                                        {/* <label>Scale Column  <span className="fa fa-caret-right"> </span></label> */}
                                                        <div className="dropdown-content2">
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "scaletype"} name={key + "scaletype"} value="standarization" onChange={this.handleScalingChange(key)} />
                                                                <label htmlFor={i + "scaletype"}>Standarization</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "scaletype"} name={key + "scaletype"} value="normalization" onChange={this.handleScalingChange(key)} />
                                                                <label htmlFor={i + "scaletype"}>Normalization</label>
                                                            </div>

                                                        </div>
                                                    </div>
                                                    <div className="prepro">
                                                        <input type="checkbox" id={key + "impute"} name={key + "impute"} value={key} onChange={this.handleImputationRemove} />
                                                        <label htmlFor={i + "impute"}>Imputation <span className="fa fa-caret-right"> </span></label>

                                                        {/* <label>Imputation  <span className="fa fa-caret-right"> </span></label> */}
                                                        <div className="dropdown-content2">
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "imputetype"} name={key + "imputetype"} value="mean" onChange={this.handleImputationChange(key)} />
                                                                <label htmlFor={i + "imputetype"}>Mean</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "imputetype"} name={key + "imputetype"} value="median" onChange={this.handleImputationChange(key)} />
                                                                <label htmlFor={i + "imputetype"}>Median</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "imputetype"} name={key + "imputetype"} value="most_frequent" onChange={this.handleImputationChange(key)} />
                                                                <label htmlFor={i + "imputetype"}>Most Frequent</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={key + "imputetype"} name={key + "imputetype"} value="knn" onChange={this.handleImputationChange(key)} />
                                                                <label htmlFor={i + "imputetype"}>KNN</label>
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
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="split">Train-Test Split Ratio</label>
                    </div>
                    <div className="col-60">

                        <select name="split" id="split" onChange={this.handleSplitChange}>
                            <option value="0.3">70-30</option>
                            <option value="0.25">75-25</option>
                            <option value="0.2">80-20</option>
                            <option value="0.15">85-15</option>
                            <option value="0.1">90-10</option>

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