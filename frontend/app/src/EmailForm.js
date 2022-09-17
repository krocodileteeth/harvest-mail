import React from "react";
import {useState} from 'react';
import {useEffect} from 'react';

export const EmailForm = ({ onSubmit}) => {
    let flatten_list = (l) => {
        const l_out = [];
        for (let i = 0; i < l.length; i = i + 1) {
          for (let j = 0; j < l[i].length; j = j + 1) {
            l_out.push(l[i][j]);
          }
        }
        return l_out;
    };

    const[data, setData] = useState({data: []});
    const[isLoading, setIsLoading] = useState(false);
    const[err, setErr] = useState('');
    const myData = [
        [
          {
            "content": "hello", 
            "id": 0, 
            "next_id": 1, 
            "prev_id": -1, 
            "read": 0, 
            "receiver": "receiver", 
            "sender": "sender", 
            "subject": "s1", 
            "timestamp": 1663447148.657154
          }, 
          {
            "content": "hi", 
            "id": 1, 
            "next_id": 2, 
            "prev_id": 0, 
            "read": 0, 
            "receiver": "sender", 
            "sender": "receiver", 
            "subject": "re: s1", 
            "timestamp": 1663447148.658153
          }, 
          {
            "content": "bye", 
            "id": 2, 
            "next_id": -1, 
            "prev_id": 1, 
            "read": 0, 
            "receiver": "receiver", 
            "sender": "sender", 
            "subject": "re: re: s1", 
            "timestamp": 1663447148.658153
          }
        ], 
        [
          {
            "content": "heh", 
            "id": 3, 
            "next_id": -1, 
            "prev_id": -1, 
            "read": 0, 
            "receiver": "receiver", 
            "sender": "sender", 
            "subject": "s2", 
            "timestamp": 1663447148.658153
          }
        ]
      ];

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

  return (
    <form onSubmit={onSubmit}>
      <div className="form-group">
      <label>Sent From: </label>
      <label> {myData[0][0].sender} </label>
      <br />
      <label> Topic: </label>
      <label> {myData[0][0].subject} </label>
      <br />
      <label> Content: </label>
      <label> {myData[0][0].content} </label>
      </div>
    </form>
  );
};
export default EmailForm;
