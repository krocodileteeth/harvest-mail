// import logo from './logo.svg';
import './App.css';
import React from "react";

// actual creation of the website
function App() {
 // replace button with calling data to it. event listens to if theres a new email
  return (
    <div className="App">
      <header className="App-header">
      <h1>
        Harvest Mail ! &emsp;
        <input type="text" name="search" size ="120" id="search" />
        <button>Search</button>
      </h1>
      <br/>
      </header>
      <br/>
      <h4>       
        <div id = "nav">
          <ul>
            <li><a href = "#inbox">Inbox </a></li>
            <br/>
            <li><a href="#junk">Junk </a></li>
            <br/>
            <li><a href ="#student">Trash</a></li>
            <br/>
          </ul>
        </div>
        <p className = "Mail-content">
          emails go here lmao
          <br/>
          emails go brrr
          <br/>
          emails
          <br/>
        </p>
      </h4>

    </div>
  );
}

export default App;
