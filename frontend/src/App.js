import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [videos, setVideos] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [videosPerPage] = useState(10);

  useEffect(() => {

    const fetchData = async () => {
      try{
        const result = await axios.get(`http://localhost:8000/api/videos/`);
        console.log("fetching videos from database")
        setVideos(result.data);
        console.log(result.data) // logging data to see the changes in the console
      } catch(error) {
        console.error(error)
      }
    };

    const intervalId = setInterval(() => {
      fetchData();
    }, 5000);

    return () => clearInterval(intervalId);
  }, []);

  // Get current videos
  const indexOfLastVideo = currentPage * videosPerPage;
  const indexOfFirstVideo = indexOfLastVideo - videosPerPage;
  const currentVideos = videos.slice(indexOfFirstVideo, indexOfLastVideo);

  // Change page
  const paginate = pageNumber => setCurrentPage(pageNumber);

  return (
    <div className="App">
      <div className="video-cards">
        {currentVideos.map(video => (
          <div className="video-card" key={video.id}>
            <a target="_blank" rel="noreferrer" href={`https://youtube.com/watch?v=${video.videoid}`}>
              <img className="video-card-thumbnail" src={video.thumbnail_url} alt={video.title} />
            </a>
            <h3 className="video-card-title">{video.title}</h3>
            <p className="video-card-published-datetime">
              {video.published_datetime}
            </p>
          </div>
        ))}
      </div>
      <div className="pagination">
        <button
          className="pagination-button prev"
          disabled={currentPage === 1}
          onClick={() => paginate(currentPage - 1)}
        >
          Prev
        </button>
        <span className="page-number">
          Page {currentPage} of {Math.ceil(videos.length / videosPerPage)}
        </span>
        <button
          className="pagination-button next"
          disabled={currentPage === Math.ceil(videos.length / videosPerPage)}
          onClick={() => paginate(currentPage + 1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}

export default App;
