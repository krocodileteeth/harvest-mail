// import logo from './logo.svg';
import test from './pixelated_ground1.jpg';
import './App.css';
import React, { useState, useEffect } from "react";

// get server_url/mail/status : gives json objects 


// actual creation of the website
function App() {
  
  // initialzing data
  const[data, setData] = useState({data: []});
  const[data2, setData2] = useState({data2: []});
  const[isLoading, setIsLoading] = useState(false);
  const[err, setErr] = useState('');
  const openInNewTab = url => {
    window.open(url, '_blank', 'noopener,noreferrer');
  };



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

  const handleClick2 = async () => {
    setIsLoading(true);

    try {
      const response2 = await fetch('http://172.26.50.101:5000/game/status', {
        method: 'GET',
        headers: {
          ContentType: 'application/json'
        },
      });

      if (!response2.ok) {
        throw new Error(`Error! status: ${response2.status}`);
      }

      const result2 = await response2.json();

      console.log('result is: ', JSON.stringify(result2, null, 4));

      setData2(result2);

    } catch (err) {
      setErr(err.message);
    } finally {
      setIsLoading(false);
    }
  };


  const triggerText = "compose email";
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
    fetch("/game/status").then((res) =>
    res.json().then((data2) => {
        document.title = data2;
        console.log(data2);
      })
    )
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
              
              <br/>

              {err && <h2>{err}</h2>}

              <button onClick={handleClick2}>check points</button>
              {isLoading && <h4>Loading...</h4>}

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
        <h3>
        <div id = "pointss">
          points: {data2.points}
        </div>
        </h3>
        <p className = "Mail-content">
          emails go here lmao
          <br/>
          {flatten_list(data).map(mail => {
                return (
                  <div key={mail.id}>
                    <button>{mail.sender} &emsp; {mail.content}  &emsp;{mail.timestamp}</button>
            <br/>
          </div>
        );
          })}
            <br/>
        </p>
      </h4>
      <h5>
        <div>
        <img src = {test} className = "Ground-Default" alt = "ground" />
        </div>
        <div id = "content">
        <Container triggerText={triggerText} onSubmit={onSubmit} />
        </div>
      </h5>

    </div>
  );
}

export default App;
