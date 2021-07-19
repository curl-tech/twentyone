import React from 'react';

// function iframe(plot) {
//     return {
//         __html: '<iframe src='+plot+' width="1080" height="540"></iframe>'
//     }
// }
export default function Plots(plot) {

    const plotdata = plot.plot
    if (plotdata === "")
        return (
            <div>
                
                <div className="centered spinner-location">
                        <div className="spinner-border text-dark spinner-border-lg" role="status">
                        <span className="loadertext">Loading...</span>
                        </div>
                    </div>
            </div>
        )
    else {
        return (

            <div>
                {/* <div className="plot" dangerouslySetInnerHTML={iframe({plotdata})} /> */}
                <iframe title="Plot" srcDoc={plotdata} width="1080" height="540">hi</iframe>
            </div>)
    }
}
