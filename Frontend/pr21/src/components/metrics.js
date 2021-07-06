import React from 'react';
class Metrics extends React.Component {


    render() {
        if (this.props.data === "a")
            return (
                <div>

                    <div className="centered spinner-location">
                        <div className="spinner-border text-dark spinner-border-lg" role="status">
                            <span className="loadertext">Loading...</span>
                        </div>
                    </div>
                </div>
            );

        else {
            const data = Object.values(this.props.data);
            if (this.props.mtype !== "clustering") {
                return (
                    <div>
                        {data.map((data, i) => (
                            i === 0 ?

                                (<div className="metricstable">

                                    <table>
                                        <thead>
                                            <tr>
                                                <th>Model</th>
                                                <th>{data.Model}</th>
                                            </tr>
                                        </thead>
                                        <tbody>

                                            {Object.keys(data).map((key, i) => (

                                                (i > 1) ? (

                                                    < tr >
                                                        <td>{key}</td>
                                                        <td>   {data[key]}</td>
                                                    </tr>
                                                ) : null))}


                                        </tbody>

                                    </table>
                                </div>) : null
                        ))
                        }
                    </div>
                );
            }
            else {
                return (
                    <div>
                        {data.map((data2, i) => (
                            i === 0 ?

                                (<div className="metricstable">

                                    <table>
                                        <thead>
                                            < tr >
                                                {Object.keys(data2).map((key, i) => (
                                                    i>0?
                                                    <th>{key}</th>:null
                                                ))}
                                            </tr>
                                        </thead>
                                        <tbody>

                                            {data.map((key, i) => (

                                                (i < 5) ? (

                                                    < tr >
                                                        {Object.keys(data2).map((key, i) => (
                                                            i>0?
                                                            <td>   {data2[key]}</td>:null
                                                        ))}
                                                    </tr>
                                                ) : null))}


                                        </tbody>

                                    </table>
                                </div>) : null
                        ))
                        }
                        <h4 className="metricsNote">Note: Every row in dataset is alloted clusters and full list can be downloaded </h4>
                    </div>
                );
            }
        }
    }
}

export default Metrics;