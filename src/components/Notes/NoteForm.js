// NoteForm.js
import React, { useState } from 'react';
import { v4 as uuidv4 } from 'uuid';

const NoteForm = ({ addNote }) => {
  const [noteTitle, setNoteTitle] = useState('');
  const [noteText, setNoteText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!noteText.trim()) return;

    const newNote = {
      id: uuidv4(),
      title: noteTitle.trim(), // Include title in newNote
      text: noteText.trim(),
      createdAt: new Date().toLocaleString()
    };

    addNote(newNote);
    setNoteTitle('');
    setNoteText('');
  };

  return (
    <div className="card mb-4">
      <div className="card-header">Add New Note</div>
      <div className="card-body">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="noteTitle">Title:</label>
            <input
              id="noteTitle"
              className="form-control mb-2"
              type="text"
              value={noteTitle}
              onChange={(e) => setNoteTitle(e.target.value)}
              placeholder="Enter note title"
              required
            />
            <label htmlFor="noteText">Note:</label>
            <textarea
              id="noteText"
              className="form-control"
              rows="3"
              value={noteText}
              onChange={(e) => setNoteText(e.target.value)}
              placeholder="Enter your note here"
              required
            ></textarea>
          </div>
          <button type="submit" className="btn btn-primary">Add Note</button>
        </form>
      </div>
    </div>
  );
};

export default NoteForm;
