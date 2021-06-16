import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import $ from 'jquery';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

// Create page start engine
var startengine = document.getElementById('startengine');
startengine.onclick = function() {
  var theFormItself = document.getElementById('form1');
  $( theFormItself ).fadeOut( 2000 );
  var theFormItself2 = document.getElementById('form2');
  $( theFormItself2).fadeIn( 5000 );
}
// display 3rd form and hide 2nd
var auto = document.getElementById('form2button');
auto.onclick = function() {
  var theFormItself = document.getElementById('form2');
  $( theFormItself ).fadeOut( 2000 );
  var theFormItself2 = document.getElementById('form3');
  $( theFormItself2).fadeIn( 5000 );
}