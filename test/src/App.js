import React from 'react';
import logo from './logo.svg';
import './App.css';
import Axios from 'axios';

function App() {
  function click(){
    Axios.get('http://127.0.0.1:5000/user').then(function(res){
      console.log(res);
      alert(res.data.user.age);
    }).catch(function(e){
      alert(e);
    })
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React

          <br/>

        </a>
        <button onClick={() => {click()}}>click</button>

      </header>
    </div>
  );
}

export default App;
