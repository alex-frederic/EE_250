import { useState, useEffect, useRef } from 'react'
import './App.css'

import "bootstrap/dist/css/bootstrap.min.css";

const [currImg, setCurrImg] = useState("");
const [logImgs, setLogImgs] = useState([]);

function App() {

  let currImg = "";
  async function pollingFunc(){
    const currResponse = await fetch("http://127.0.0.1:5000/curr_img");
    const currResults = await currResponse.json();
    console.log(currResults);


    const logResponse = await fetch("127.0.0.1:5000/log_img");
    const logResults = await logResponse.json();
    console.log(logResults);


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

  return (
    <>
      <div id="header">
        <h1>PiWatch</h1>
      </div>
      <div className="container">
        <div className="row">
          <div id="curr-img" className="col-8">
            <img src="img/image.jpg" alt="Currently Displayed Image" />
          </div>
          <div id="log" className="col-4">
            <h2>Log</h2>

            {/* PUT LOG ENTRIES HERE */}

          </div>
        </div>
      </div>
    </>
  )
}

export default App
