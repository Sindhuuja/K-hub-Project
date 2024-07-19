import React from 'react';
import Note from './Note';
import './NoteList.css';
const NoteList = ({ notes, deleteNote, updateNote }) => {
  return (
    <div className="row mt-4">
      {notes.map((note) => (
        <div className="col-md-4" key={note.id}>
          <Note note={note} deleteNote={deleteNote} updateNote={updateNote} />
        </div>
      ))}
    </div>
  );
};

export default NoteList;
