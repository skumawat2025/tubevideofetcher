import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  //Some changes
  const [sfsf, setfsdfhsd] = useState()
  const [videos , setVideos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchVideos = async () => {
      setLoading(true );
      const res = await axios.get('http://localhost:8000/api/get-videos');
      setVideos(res.data);
      setLoading(false);
    };
    fetchVideos();
  }, []);

  return (
    <div>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <ul>
          {videos}
        </ul>
      )}
    </div>
  );
};

export default App;
