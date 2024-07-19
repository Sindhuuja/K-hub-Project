// Note.js
import React, { useState } from 'react';

const Note = ({ note, deleteNote, updateNote }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [updatedText, setUpdatedText] = useState(note.text);

  const handleUpdate = () => {
    updateNote({
      ...note,
      text: updatedText,
      updatedAt: new Date().toLocaleString()
    });
    setIsEditing(false);
  };

  return (
    <div className="card mb-3">
      <div className="card-body">
        {!isEditing ? (
          <>
            <p className="card-title" style={{ fontWeight: 'bold' }}>{note.title}</p> {/* Display title */}
            <p className="card-text">{note.text}</p>
            <p className="card-text"><small className="text-muted">Created: {note.createdAt}</small></p>
            {note.updatedAt && <p className="card-text"><small className="text-muted">Updated: {note.updatedAt}</small></p>}
            <div className="btn-container">
              <button className="btn btn-sm btn-danger" onClick={() => deleteNote(note.id)}>Delete</button>
              <button className="btn btn-sm btn-primary" onClick={() => setIsEditing(true)}>Edit</button>
            </div>
          </>
        ) : (
          <>
            <textarea
              className="form-control mb-2"
              rows="3"
              value={updatedText}
              onChange={(e) => setUpdatedText(e.target.value)}
            ></textarea>
            <button className="btn btn-sm btn-success mr-2" onClick={handleUpdate}>Update</button>
            <button className="btn btn-sm btn-secondary" onClick={() => setIsEditing(false)}>Cancel</button>
          </>
        )}
      </div>
    </div>
  );
};

export default Note;
