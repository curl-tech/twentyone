import React from 'react';
import $ from 'jquery';
// import axios from 'axios';




class Preprocess extends React.Component {
    handlePreProcess = event => {
        event.preventDefault();
        var theFormItself = document.getElementById('form4');
        $(theFormItself).hide();
        var theFormItself2 = document.getElementById('form5');
        $(theFormItself2).show();
        

        // axios.post('http://localhost:8000/manualpreprocess', JSON.stringify(data))
        //     .then(res => { console.log("Successful", res) },
        //         (error) => { console.log(error) });
    }
    render() {
        const rawdata = Object.values(this.props.rawdata);
        // console.log(this.props.rawdata)
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
                                                        <input type="radio" id={i + "drop"} name={i + "drop"} />
                                                        <label htmlFor={i + "drop"}>Drop Column</label>
                                                    </div>

                                                    <div className="prepro ">
                                                        <label>Encode Column  <span className="fa fa-caret-right"> </span></label>
                                                        <div className="dropdown-content2">
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "encode"} name={i + "encode"} />
                                                                <label htmlFor={i + "encode"}>One Hot Encoding</label>
                                                            </div>
                                                            <div className="prepro">
                                                                <input type="radio" id={i + "encode"} name={i + "encode"} />
                                                                <label htmlFor={i + "encode"}>Label Encoding</label>
                                                            </div>
                                                           
                                                        </div>
                                                    </div>
                                                    <div className="prepro">
                                                        <label>Scale Column  <span className="fa fa-caret-right"> </span></label>
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
                                                        <label>Imputation  <span className="fa fa-caret-right"> </span></label>
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

                        <select name="target" id="target" onChange={this.handletargetChange}>
                            {Object.keys(rawdata[0]).map((key, i) =>
                                <option value={i}>{key}</option>
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
                    <select name="imbalance" id="imbalance"  onChange={this.handleChange}>
                        <option value="fasle">No</option>
                        <option value="true">Yes</option>
                    </select>
                    </div>
                </div>
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="outlier">Check for Outliers?</label>
                    </div>
                     <div className="col-60 ">
                    <select name="outlier" id="outlier"  onChange={this.handleChange}>
                        <option value="fasle">No</option>
                        <option value="true">Yes</option>
                    </select>
                    </div>
                </div>
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="featureeng">Want us to perform feature engineering?</label>
                    </div>
                     <div className="col-60 ">
                    <select name="featureeng" id="featureeng"  onChange={this.handleChange}>
                        <option value="fasle">No</option>
                        <option value="true">Yes</option>
                    </select>
                    </div>
                </div>
                <button className="preprocessbtn" onClick={this.handlePreProcess} >Preprocess Now</button>
            </div>
        );
    }
}

export default Preprocess;