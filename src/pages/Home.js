import React from 'react';
import './Home.css';

const Home = () => {
  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-8">
          <div className="card">
            <div className="card-header">Welcome to NoteApp</div>
            <div className="card-body">
              <h5 className="card-title">Your Personal Note Manager</h5>
              <p className="card-text">
                NoteApp is designed to help you manage your notes efficiently and effortlessly. With NoteApp, you can:
              </p>
              <ul className="list-group list-group-flush">
                <li className="list-group-item">Create new notes to capture your thoughts and ideas.</li>
                <li className="list-group-item">Edit existing notes to update or modify the content.</li>
                <li className="list-group-item">Delete notes that are no longer needed.</li>
                <li className="list-group-item">Organize your notes by categories or tags for easy retrieval.</li>
                <li className="list-group-item">Search for specific notes using keywords.</li>
                <li className="list-group-item">Access your notes from any device, anywhere.</li>
              </ul>
              <p className="card-text mt-3">
                Start using NoteApp today to stay organized and keep track of all your important information!
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Home;
