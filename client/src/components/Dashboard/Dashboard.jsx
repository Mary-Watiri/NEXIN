import React, { useState } from 'react';
import { Box, IconButton, Button } from '@mui/material';
import MarkEmailReadOutlinedIcon from '@mui/icons-material/MarkEmailReadOutlined';
import PointOfSaleOutlinedIcon from '@mui/icons-material/PointOfSaleOutlined';
import DownloadOutlinedIcon from '@mui/icons-material/DownloadOutlined';
import PersonAddOutlinedIcon from '@mui/icons-material/PersonAddOutlined';
import DonutLargeIcon from '@mui/icons-material/DonutLarge';
import TicketForm from './TicketForm';
import TicketList from './TicketList';

const Dashboard = ({ ThemeStyles }) => {
  const [tickets, setTickets] = useState([]);

  const handleCreateTicket = (newTicket) => {
    setTickets([...tickets, { id: tickets.length + 1, ...newTicket }]);
  };

  const ticketQuantityPerCounty = [
    { country: 'Nairobi', quantity: 120 },
    { country: 'Mombasa', quantity: 150 },
    { country: 'Nakuru', quantity: 180 },
    { country: 'Kisumu', quantity: 210 },
  ];

  return (
    <div className="p-6 overflow-hidden h-screen">
      <Box class="justify-between flex" style={ThemeStyles}>
        <div>
          <h1 className="text-3xl font-bold mb-4">NEXIN LTD</h1>
          <h2 className="text-2xl font-semibold mb-8 text-emerald-600">WELCOME TO THE TICKETING SYSTEM</h2>
        </div>
        {/* download documents */}
        <DownloadPDF />
      </Box>

      <Box className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-2 mb-2">
        {/* Tickets */}
        <Box className="bg-sky-950 p-2 shadow-md flex items-center">
          <div className="w-4 h-8 text-blue-500 mr-2"><DonutLargeIcon /></div>
          <MarkEmailReadOutlinedIcon className="w-8 h-8 text-blue-500 mr-4" />
          <div>
            <h1 className="text-2xl text-slate-300 font-semibold">12,361</h1>
            <h2 className='text-blue-500'>Tickets Created</h2>
          </div>
        </Box>

        {/* New Tasks */}
        <div className="bg-sky-950 p-4 shadow-md flex items-center">
          <div className="w-8 h-8 text-green-500 mr-4"><DonutLargeIcon /></div>
          <PointOfSaleOutlinedIcon className="w-8 h-8 text-green-500 mr-4" />
          <div>
            <h1 className="text-2xl font-semibold text-slate-300">431,22</h1>
            <h2 className='text-green-500'>New Tasks +21%</h2>
          </div>
        </div>

        {/* Overdue Tasks */}
        <div className="bg-sky-950 p-4 shadow-md flex items-center">
          <div className="w-8 h-8 text-yellow-500 mr-4"><DonutLargeIcon /></div>
          <DownloadOutlinedIcon className="w-8 h-8 text-yellow-500 mr-4" />
          <div>
            <h1 className="text-2xl font-semibold text-slate-300">32,441</h1>
            <h2 className="text-yellow-500">Overdue Tasks +5%</h2>
          </div>
        </div>

        {/* Due Today Tasks */}
        <div className="bg-sky-950 p-4 shadow-md flex items-center">
          <div className="w-8 h-8 text-purple-500 mr-4"><DonutLargeIcon /></div>
          <PersonAddOutlinedIcon className="w-8 h-8 text-purple-500 mr-4" />
          <div>
            <h1 className="text-2xl font-semibold text-slate-300">30,440</h1>
            <h2 className="text-purple-500">Due Today Tasks +10%</h2>
          </div>
        </div>
      </Box>

      {/* Ticket Creation Form */}
      <TicketForm onSubmit={handleCreateTicket} />

      {/* Ticket List */}
      <TicketList tickets={tickets} />

      {/*
        Adjusted Bar Chart for Ticket Quantity
      */}
      <Box class="flex w-100 justify-between">
        <Box class="p-2 bg-sky-950 m-3 w-3/4 h-60 overflow-hidden">
          <div className="flex justify-between text-center">
            <h5 className="text-center text-emerald-400 font-extrabold">
              <span className='text-slate-300'>Ticket Quantity</span>
            </h5>
          </div>
          <div className="w-75 -mt-10 h-80">
            <Bar data={ticketQuantityPerCounty} />
          </div>
        </Box>
        <Box class="p-5 mr-2 overflow-y-scroll h-60 w-1/3 position-fixed scroll-">
          {/* Recent Tickets */}
          <div className="bg-cyan-950 text-center justify-center flex h-12 align-middle">
            <h2 class="text-slate-100 p-3 w-100">
              Recent Tickets
            </h2>
          </div>
          {/* Sample Recent Tickets */}
          <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Emmanuel Kimwaki</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">37009103</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Wrong BRC Measurements</Button>
            </div>
        </div>
          {/* Add your recent tickets here */}
          <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Emmanuel Kimwaki</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">37009103</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Wrong BRC Measurement</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">James Orengo</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">39764784</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Flatroof Design</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Samuel Omoding</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">3873785</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Parquet Flooring</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Arap Samoei</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">3873785</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Upadte on BQ</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Sarah Wanjiku</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">3873785</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Design Change</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle p-4 justify-between w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">George Okumu</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">3873785</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Report Progress</Button>
            </div>
        </div>
        <div className="flex mt-2 align-middle justify-between p-4 w-100 bg-sky-950">
            <div className=" p-2 align-middle">
            <h5 className="text-green-500 font-extrabold">009ur47</h5>
            <h6 className="text-slate-200">Victor Muteithia</h6>
            </div>
            <div className="m-3 text-slate-200">
            <h6 className="text-zinc-300 text-sm">3873785</h6>
            </div>
            <div className="m-3 text-slate-200">
            <Button class="bg-teal-500 text-slate-200 p-1 w-100 border-r-2">Need of Design</Button>
            </div>
        </div>
        </Box>
      </Box>
    </div>
  );
}

export default Dashboard;