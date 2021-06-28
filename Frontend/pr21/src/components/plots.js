import React from 'react';
// import renderHTML from 'react-render-html';
// function iframe(plot) {
//     return {
//         __html: '<iframe src='+plot+' width="1080" height="540"></iframe>'
//     }
// }
export default function Plots(plot) {
    
    const plotdata=plot.plot
    // const renderHTML = require('react-render-html');
    return (
        
        <div>
            <h1>Loading</h1>
            {/* <div className="plot" dangerouslySetInnerHTML={iframe({plotdata})} /> */}
            <iframe title="Plot" srcdoc={plotdata} width="1080" height="540">hi</iframe>
        </div>)
}
// class Plots extends Component {
//     render() {
//         return (
//             <div >
//                <h1>hi</h1>

//             </div>
//         );
//     }
// }

// export default Plots;