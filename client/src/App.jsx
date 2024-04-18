import { UseTheme } from "./Theme";
import SideBar from "./components/Dashboard/SideBar";
import { Routes, Route } from "react-router-dom";
import Dashboard from "./components/Dashboard/Dashboard";

function App() {
  const darkTheme = UseTheme(); //usetheme hook

  //create the themes
  const ThemeStyles = {
    backgroundColor: darkTheme? "rgb(10,10,30)" : "rgb(240,250,250)",
    color: darkTheme? "rgb(230,220,220)" : "rgb(10,10,30)",
  };

  return (
    <>
      <div className="app overflow-hidden" style={ThemeStyles}>
        <SideBar />
        <main className="content">
          {/* Routes */}
          <Routes>
            <Route path="/" element={<Dashboard ThemeStyles={ThemeStyles} />}/>
          </Routes>
        </main>
      </div>
    </>
  );
}

export default App;