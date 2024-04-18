import React, { useContext, useState } from 'react';
import PropTypes from 'prop-types'; // Import PropTypes

const ThemeContext = React.createContext(); // Create a theme context
const UpdateThemeContext = React.createContext();

export function UseTheme() {
  // Create custom hook for theme
  return useContext(ThemeContext);
}

export function UpdateTheme() {
  // Create custom hook for button
  return useContext(UpdateThemeContext);
}

function ThemeProvider({ children }) {
  const [darkTheme, setDarkTheme] = useState(true); // Set state for the theme

  const toggleColor = () => {
    setDarkTheme(prevTheme => !prevTheme);
  };

  return (
    <div>
      {/* Theme providers */}
      <ThemeContext.Provider value={darkTheme}>
        <UpdateThemeContext.Provider value={toggleColor}>
          {children}
        </UpdateThemeContext.Provider>
      </ThemeContext.Provider>
    </div>
  );
}

// Define propTypes for the ThemeProvider component
ThemeProvider.propTypes = {
  children: PropTypes.node, // Use PropTypes.node for the 'children' prop
};

export default ThemeProvider;
