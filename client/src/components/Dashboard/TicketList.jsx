import { useState } from 'react';
import { Box, Button, Container, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from '@mui/material';
import { useTheme } from '@mui/styles';
import tickets from './data/tickets';

const TicketList = () => {
  const theme = useTheme();
  const [showAddButton, setShowAddButton] = useState(true);

  const handleAddButtonClick = () => {
    setShowAddButton(false);
  };

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          bgcolor: '#1F2937',
          borderRadius: '10px',
          p: 3,
          mt: 3,
          color: '#fff',
        }}
      >
        <Typography variant="h5" component="h2" mb={2}>
          Ticket List
        </Typography>
        <Box display="flex" justifyContent="space-between" alignItems="center">
          {showAddButton && (
            <Button variant="contained" color="primary" onClick={handleAddButtonClick}>
              Add Ticket
            </Button>
          )}
          <Typography variant="subtitle1" color="textSecondary">
            {tickets.length} tickets
          </Typography>
        </Box>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell sx={{ color: theme.palette.text.primary }}>Title</TableCell>
                <TableCell sx={{ color: theme.palette.text.primary }}>Description</TableCell>
                <TableCell sx={{ color: theme.palette.text.primary }}>Due Date</TableCell>
                <TableCell sx={{ color: theme.palette.text.primary }}>Status</TableCell>
                <TableCell sx={{ color: theme.palette.text.primary }}>Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {tickets.map((ticket) => (
                <TableRow key={ticket.id}>
                  <TableCell>{ticket.title}</TableCell>
                  <TableCell>{ticket.description}</TableCell>
                  <TableCell>{ticket.dueDate}</TableCell>
                  <TableCell>{ticket.status}</TableCell>
                  <TableCell>
                    <Box display="flex" justifyContent="flex-end">
                      <Button variant="contained" color="primary" sx={{ mr: 1 }}>
                        Edit
                      </Button>
                      <Button variant="contained" color="secondary">
                        Delete
                      </Button>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    </Container>
  );
};

export default TicketList;