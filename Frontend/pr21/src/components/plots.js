import React from 'react';
function iframe() {
    return {
        __html: '<iframe src="/output.html" width="1080" height="540"></iframe>'
    }
}
export default function Plots() {
    return (
        <div>
            <div className="plot" dangerouslySetInnerHTML={iframe()} />
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