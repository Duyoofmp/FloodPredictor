import React, { useState } from 'react';
import './Home.css';

const Home = () => {
  const [height, setHeight] = useState('');

  const handleHeightChange = (event) => {
    setHeight(event.target.value);
  };

  const handleSubmit = () => {
    const iframe = document.getElementById('floodmapIframe');
    const floodmapDocument = iframe.contentDocument || iframe.contentWindow.document;
    const heightInput = floodmapDocument.getElementById('heightInput');
    const submitButton = floodmapDocument.getElementById('submitButton');

    if (heightInput && submitButton) {
      heightInput.value = height;
      submitButton.click();
    }
  };

  return (
    <div className="container">
      <div className="iframe-container">
        <iframe id="floodmapIframe" src="https://www.youtube.com/" title="Flood Map"></iframe>
      </div>
      <div className="input-container">
        <input
          type="number"
          placeholder="Enter height"
          value={height}
          onChange={handleHeightChange}
        />
        <button onClick={handleSubmit}>Submit</button>
      </div>
    </div>
  );
};

export default Home;
