import React from 'react'
import { Box,IconButton } from '@mui/material'
import SearchOutlinedIcon from '@mui/icons-material/SearchOutlined';
//import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';
import LightModeOutlinedIcon from '@mui/icons-material/LightModeOutlined';
import NotificationsOutlinedIcon from '@mui/icons-material/NotificationsOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import Person2OutlinedIcon from '@mui/icons-material/Person2Outlined';
import DarkModeOutlinedIcon from '@mui/icons-material/DarkModeOutlined';
import { Link } from 'react-router-dom';
function TopNav({toggleColor,darkTheme}) {
  const ThemeStyles={
    backgroundColor:darkTheme?"rgb(10,10,30)":"rgb(240,250,250)",
    color:darkTheme?"rgb(240,240,240)":"rgb(10,10,30)"
  }

return (
    <Box  class="flex justify-between mt-2 p-5" style={ThemeStyles} >
    {/*searchbar*/}
    <Box class="flex">
      <input className="text-slate-700 bg-sky-950 " placeholder="search"/>
      <IconButton style={ThemeStyles} class="text-slate-700">
        <SearchOutlinedIcon />
      </IconButton>
      
    </Box>
    {/*icons*/}
    <Box display="flex p-2">
      <IconButton style={ThemeStyles} class="text-xl"  onClick={toggleColor}>
       {darkTheme?<DarkModeOutlinedIcon/>:<LightModeOutlinedIcon />}
      </IconButton>
      <Link to="/FAQ">
         <IconButton class='p-2' style={ThemeStyles}>
        <NotificationsOutlinedIcon />
      </IconButton>
      </Link>
     <Link>
      <IconButton class="text-slate-800" style={ThemeStyles}>
        <SettingsOutlinedIcon />
      </IconButton>
</Link>
     
      <Link to="/Profile">
        <IconButton class="text-neutral-800" style={ThemeStyles}>
        <Person2OutlinedIcon />

      </IconButton>
      </Link>
      
    </Box>
  </Box>

    
  )
}

export default TopNav
