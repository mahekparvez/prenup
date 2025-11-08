import React from "react";
import NavMenuItem from "./NavMenuItem";

function NavMenu() {
  return (
    <ul className="nav-menu">
      <NavMenuItem to="/" label="Home" />
      <NavMenuItem to="/settings" label="Lesson" />
      <NavMenuItem to="/about" label="About" />
        <NavMenuItem to="/Tutor" label="AI Tutor"/>
      
    </ul>
  );
}

export default NavMenu;