import React, { Component } from 'react';
import { Link } from "react-router-dom";
class PageWrapper extends Component {
    render() {
        return (
            <div>
                <header >
                    <nav className="navbar navbar-expand-lg ">
                        <div className="container-fluid">
                            <Link className="navbar-brand" to="/">AutoMl</Link>
                            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                                <span className="line"></span>
                                <span className="line"></span>
                                <span className="line"></span>
                            </button>
                            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                                    <li className="nav-item">
                                        <Link className="nav-link active" aria-current="page" to="/">Home</Link>
                                    </li>
                                    <li className="nav-item">
                                        <Link className="nav-link" to="/newproject">Create Project</Link>
                                    </li>

                                    <li className="nav-item">
                                        <Link className="nav-link" to="/MyProjects">MyProjects</Link>
                                    </li>
                                </ul>
                                <form className="d-flex">
                                    <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                                    <button className="btn btn-outline-success" type="submit">Search</button>
                                </form>
                            </div>
                        </div>
                    </nav>

                </header>
                <button id="topButton" title="Go to top" >➤</button>
                {this.props.children}

                <footer className=" text-light py-3 footer">
                    <p className="text-center">
                        Copyright &copy; Curl Tech 2021
            </p>
                </footer>

            </div>

        );
    }
}
export default PageWrapper;