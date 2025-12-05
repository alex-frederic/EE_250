import { useState } from 'react'
import './App.css'

import "bootstrap/dist/css/bootstrap.min.css";

function App() {
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
