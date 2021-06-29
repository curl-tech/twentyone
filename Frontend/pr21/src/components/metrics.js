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
        
            return (
                <div>
                    {data.map((data, i) => (
                        i === 1 ?

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
                                    {/* <tbody>
                                    <tr>
                                        <td>Accuracy</td>
                                        <td>{data.Accuracy}</td>
                                    </tr>
                                    <tr>
                                        <td>Precision</td>
                                        <td>{data.Prec}</td>
                                    </tr>
                                    <tr>
                                        <td>Recall</td>
                                        <td>{data.Recall}</td>
                                    </tr>
                                    <tr>
                                        <td>F1 Score</td>
                                        <td>{data.F1}</td>
                                    </tr>
                                </tbody> */}
                                </table>
                            </div>) : null
                    ))
                    }
                </div>
            );
        }
    }
}

export default Metrics;