import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    // Perform login logic here (e.g., form validation, API call)
    // After successful login, navigate to the note application page
    navigate('/add-note');
  };

  return (
    <div className="container">
      <div className="card">
        <div className="card-header">
          Login
        </div>
        <div className="card-body">
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email address</label>
              <input type="email" className="form-control" id="email" placeholder="Enter email" required />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input type="password" className="form-control" id="password" placeholder="Password" required />
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
            <a href="/register" className="link">Don't have an account? Register</a>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Login;
