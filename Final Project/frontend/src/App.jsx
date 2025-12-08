import { useState, useEffect } from 'react'
import './App.css'

import {LogEntry} from "./LogEntry.jsx"

import "bootstrap/dist/css/bootstrap.min.css";

function App() {

  const [currImg, setCurrImg] = useState("placeholder.jpg");
  const [logImgs, setLogImgs] = useState(["placeholder.jpg"]);
  const [showLogImg, setShowLogImg] = useState(logImgs[0]);

  let logEntryKey = 1;

  async function pollingFunc(){
    const currResponse = await fetch("http://172.20.10.5:5000/curr_img");
    const currResults = await currResponse.json();
    console.log(currResults);
    setCurrImg(currResults.currImg);

    const logResponse = await fetch("http://172.20.10.5:5000/log_img");
    const logResults = await logResponse.json();
    console.log(logResults);
    setLogImgs(logResults.log);

  }

  useEffect( () => {
    // const pollingRef = useRef(null);
    function startPolling () {
      setInterval( () => {
        pollingFunc();
      }, 5000); // Poll every 5 seconds
    }
    startPolling();

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
            <img src={currImg} alt="Currently Displayed Image" />
            <img src={showLogImg} alt={showLogImg} />
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
