// import logo from './logo.svg';
import test from './pixelated_ground1.jpg';
import './App.css';
import React, { useState, useEffect } from "react";
import {Container} from './Container.js';
import {Container2} from './Container2.js';
import {EmailContainer} from './EmailContainer.js';

// get server_url/mail/status : gives json objects 


// actual creation of the website
function App() {
  let flatten_list = (l) => {
    const l_out = [];
    for (let i = 0; i < l.length; i = i + 1) {
      for (let j = 0; j < l[i].length; j = j + 1) {
        l_out.push(l[i][j]);
      }
    }
    return l_out;
  };
  
  // initialzing data
  const[data, setData] = useState({data: []});
  const[isLoading, setIsLoading] = useState(false);
  const[err, setErr] = useState('');

  const handleClick = async () => {
    setIsLoading(true);

    try {
      const response = await fetch('http://172.26.50.101:5000/mail/status', {
        method: 'GET',
        headers: {
          ContentType: 'application/json'
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


  const triggerText = "compose email";
  const shopTrigger = "view shop";
  const openTrigger = "open email";
  const onSubmit = (event) => {
    event.preventDefault(event);
    console.log(event.target.name.value);
    console.log(event.target.email.value);
  }

  useEffect(() => {
    fetch("/mail/status").then((res) =>
    res.json().then((data) => {
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
        <div className = "email-click">
              {err && <h2>{err}</h2>}

              <button onClick={handleClick}>refresh emails</button>
              {isLoading && <h4>Loading...</h4>}
            
            </div>
            <div>
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
          <br/>
          {console.log(data)}
          {flatten_list(data).map(mail => {
                return (
                  <div key={mail.id}>
                            <EmailContainer triggerText={openTrigger} onSubmit={onSubmit} data={data} />

                    <button>{mail.sender} &emsp; {mail.content}  &emsp;{mail.timestamp}</button>
            <br/>
          </div>
        );
          })}

            <div className = "email-click" >
            </div>
            <br/>
        </p>
      </h4>
      <h5>
        <div>
        <img src = {test} className = "Ground-Default" alt = "ground" />
        </div>
        <Container triggerText={triggerText} onSubmit={onSubmit} />
        <Container2 triggerText={shopTrigger} onSubmit={onSubmit} />
      </h5>

    </div>
  );
}

export default App;