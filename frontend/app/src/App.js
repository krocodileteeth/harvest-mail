// import logo from './logo.svg';
import './App.css';
import React from "react";

/*
// display this when looking at stats 
// all the mail set to empty until given information ??
const front_values = {
  // mail initially empty
  mail : [],

  // stats that will be incr/decr based off of the user's performance
  points : 0,
  mail_sent : 0,
  mail_received : 0,
  // fastest_time : 0,

  // store items
  store_flower_count : 0,
  flower_names : [],
  water : 0,

  // garden
  garden_flower_count : 0
  
};

// retrieving the object values 
let mail = front_values.mail;
let points = front_values.points;
let mail_sent = front_values.mail_sent;
let mail_received = front_values.mail_received;
// let fastest_time = front_values.fastest_time;

let store_flower_count = front_values.store_flower_count;
let flower_names = front_values.flower_names;
let water = front_values.water;

let garden_flower_count = front_values.garden_flower_count;
*/

// actual creation of the website
function App() {
  return (
    <div className="App">
      <header className="App-header">
      <h1>
        Harvest Mail ! 
        <input type="text" name="search" id="search" />
        <button>Search</button>
      </h1>
      </header>
    </div>
  );
}

export default App;
