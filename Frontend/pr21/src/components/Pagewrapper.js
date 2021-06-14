import React, { Component } from 'react';
import { Link } from "react-router-dom";

class PageWrapper extends Component {
    render() {
        return (
            <div>
                <header>
                    <h1> header</h1>
                </header>

                {this.props.children}


                <div className="container mt-3 pt-3"></div>


                <footer className="footer">
                    <h3>footer</h3>
                </footer>

            </div>

        );
    }
}
export default PageWrapper;