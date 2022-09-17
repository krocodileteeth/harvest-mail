// import logo from './logo.svg';
import test from './pixelated_ground1.jpg';
import './App.css';
import React, { useState, useEffect } from "react";
import {Container} from './Container.js';

// get server_url/mail/status : gives json objects 


// actual creation of the website
function App() {
  
  // initialzing data
  const[data, setData] = useState({data: []});
  const[isLoading, setIsLoading] = useState(false);
  const[err, setErr] = useState('');

  const triggerText = "compose email";
  const onSubmit = (event) => {
    event.preventDefault(event);
    console.log(event.target.name.value);
    console.log(event.target.email.value);
  }

  const handleClick = async () => {
    setIsLoading(true);

    try {
      const response = await fetch('http://172.26.50.101:5000/mail/status', {
        method: 'GET',
        headers: {
          Accept: 'application/json',
          CORS: 'disable'
        },
      });

      if (!response.ok) {
        throw new Error(`Error! status: ${response.status}`);
      }

      const result = await response.json();

      console.log('result is: ', JSON.stringify(result, null, 4));

      setData(result);
    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetch("/mail/status").then((res) =>
    res.json().then((data) => {
        // Setting a data from api
        // setdata(git swicd{
        //     id: data.id,
        //     sender: data.sender,
        //     receiver: data.receiver,
        //     content: data.content,
        //     read: data.read,
        //     next_id: data.next_id,
        //     prev_id: data.prev_id,
        //     timestamp: data.timestamp
        //   });
        document.title = data;
        console.log(data);
      })
    );
  }, []);

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
        <div id = "shop">
          <button> view shop </button>
        </div>
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
            <div className = "email-click" >
            <button>{data.Sender} &emsp; {data.Subject} &emsp; {data.Timestamp}</button>
            </div>
            <br/>
            <div>
              {err && <h2>{err}</h2>}

              <button onClick={handleClick}>Fetch data</button>
              {isLoading && <h2>Loading...</h2>}
            
            </div>
        </p>
      </h4>
      <h5>
        <div>
        <img src = {test} className = "Ground-Default" alt = "ground" />
        </div>
        <Container triggerText={triggerText} onSubmit={onSubmit} />
        <div id = "compose">
          <button>compose email</button>
        </div>
      </h5>

    </div>
  );
}

export default App;