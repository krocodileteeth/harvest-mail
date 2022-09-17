// import logo from './logo.svg';
import test from './pixelated_ground1.jpg';
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
        <div id = "shop">
          <button> view shop </button>
        </div>
      </h4>
      <h5>
        <div>
        <img src = {test} className = "Ground-Default" alt = "ground" />
        </div>
        <div id = "compose">
          <button>compose email</button>
        </div>
      </h5>

    </div>
  );
}

export default App;
