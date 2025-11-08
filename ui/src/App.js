import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./Homepage.jsx";
import AIChatBot from "./AIChatBot.jsx";


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/AIChatBot" element={<AIChatBot />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
