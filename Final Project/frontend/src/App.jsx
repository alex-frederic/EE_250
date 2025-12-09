import { useState, useEffect } from 'react'
import './App.css'

import {LogEntry} from "./LogEntry.jsx"

import "bootstrap/dist/css/bootstrap.min.css";

function App() {

  const [currImg, setCurrImg] = useState("img/placeholder.jpg");
  const [logImgs, setLogImgs] = useState([]);
  const [showLogImg, setShowLogImg] = useState("");

  let logEntryKey = 1;

  async function pollingFunc(){
    try {
      const currResponse = await fetch("http://127.0.0.1:5000/curr_img");
      const currResults = await currResponse.json();
      setCurrImg(currResults.curr_img);
    } catch (error) {
      console.error("Error fetching current image:", error);
    }

    try {
      const logResponse = await fetch("http://127.0.0.1:5000/log_img");
      const logResults = await logResponse.json();
      console.log(logResults);
      setLogImgs(logResults.log);
    } catch (error) {
      console.error("Error fetching log images:", error);
    }
  }

  useEffect( () => {
    // Initial fetch
    pollingFunc();

    const intervalId = setInterval( () => {
      pollingFunc();
    }, 5000); // Poll every 5 seconds

    return () => clearInterval(intervalId);
  },
  []);

  function handleEntryClick(url) {
    setShowLogImg(url);
  }

  return (
    <>
      <div id="header">
        <h1>PiWatch</h1>
      </div>
      <div className="container">
        <div className="row">
          <div id="curr-img" className="col-8">
            <h2>Current Live Image</h2>
            <img src={currImg} alt="Currently Displayed Image" style={{ maxWidth: '100%', marginBottom: '20px' }} />
            
            <h2>Selected Log Image</h2>
            <img src={showLogImg} alt={showLogImg || "Select an image from log"} style={{ maxWidth: '100%' }} />
          </div>
          <div id="log" className="col-4">
            <h2>Log</h2>

            {/* PUT LOG ENTRIES HERE */}

            {logImgs.map( (entry) => {
              logEntryKey ++;
              return (<LogEntry url={entry} parentHandleClick={handleEntryClick} key={logEntryKey} />);
            } ) }

          </div>
        </div>
      </div>
    </>
  )
}

export default App
