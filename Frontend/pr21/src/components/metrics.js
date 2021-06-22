import React from 'react';
class Metrics extends React.Component {
    

    render() {
        const data = Object.values(this.props.data);
        return (
            <div>
                {data.map((data,i) => (
                i===1?
                    
                (<div className="metricstable">
                    
                <table>
                    <thead>
                    <tr>
                        <th>Model</th>
                    <th>{data.Model}</th>
                    </tr>
                    </thead>
                    <tbody>
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
                    </tbody>
                </table>
                </div>):null
                ))}   
             </div>
        );
    }
}

export default Metrics;