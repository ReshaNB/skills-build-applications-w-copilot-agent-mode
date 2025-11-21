
import React from "react";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import Activities from "./components/Activities";
import Leaderboard from "./components/Leaderboard";
import Teams from "./components/Teams";
import Users from "./components/Users";
import Workouts from "./components/Workouts";
import "./App.css";
import logo from "./logo.svg";

const navItems = [
  { path: "/activities", label: "Activities" },
  { path: "/leaderboard", label: "Leaderboard" },
  { path: "/teams", label: "Teams" },
  { path: "/users", label: "Users" },
  { path: "/workouts", label: "Workouts" },
];

function App() {
  return (
    <BrowserRouter>
      <header>
        <nav className="navbar navbar-expand navbar-light mb-4">
          <div className="container-fluid">
            <NavLink className="navbar-brand d-flex align-items-center" to="/">
              <img src={logo} alt="OctoFit Logo" className="octofit-logo me-2" />
              <span>OctoFit Tracker</span>
            </NavLink>
            <ul className="navbar-nav flex-row">
              {navItems.map((item) => (
                <li className="nav-item mx-2" key={item.path}>
                  <NavLink className="nav-link" to={item.path}>
                    {item.label}
                  </NavLink>
                </li>
              ))}
            </ul>
          </div>
        </nav>
      </header>
      <main className="container">
        <Routes>
          <Route path="/" element={<h2>Welcome to OctoFit Tracker!</h2>} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/users" element={<Users />} />
          <Route path="/workouts" element={<Workouts />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;