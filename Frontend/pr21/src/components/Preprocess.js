import React from 'react';




class Preprocess extends React.Component {

    render() {
        const rawdata = Object.values(this.props.rawdata);
        console.log(this.props.rawdata)
        return (
            <div>
                {rawdata.map((data, i) => (
                    i === 1 ? (
                        <div className="preprocesstable ">
                            <table>
                                <thead>
                                    <tr>
                                        {Object.keys(data).map((key) =>
                                            <th className="dropdown ">
                                                {key}<span className="fa fa-caret-down"></span>
                                                <div class="dropdown-content">
                                                    <div className="prepro">
                                                        <input type="checkbox" id="drop" name="drop" />
                                                        <label for="drop">Drop Column</label>
                                                    </div>
                                                    <a href="#">Link 2</a>
                                                    <a href="#">Link 3</a>
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
                <div className="row">
                    <div className="col-40">
                        <label htmlFor="nulltype">How are null values specified in dataset?</label>
                    </div>
                    <div className="col-60" >
                        <input type="text" id="nulltype" name="nulltype" onChange={this.handleNullTypeChange} placeholder="Is it NULL, NA , ? , 0 or other (specify)" required />
                    </div>
                </div>
                <button className="preprocessbtn">Preprocess Now</button>
            </div>
        );
    }
}

export default Preprocess;