import { useState } from 'react';
import PropTypes from 'prop-types'; // Import PropTypes
import { Box, Button, Container, TextField, Typography } from '@mui/material';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';

const TicketForm = ({ onSubmit }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [dueDate, setDueDate] = useState(null);

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit({ title, description, dueDate });
    setTitle('');
    setDescription('');
    setDueDate(null);
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
          Create a New Ticket
        </Typography>
        <form onSubmit={handleSubmit}>
          <Box mb={2}>
            <TextField
              label="Title"
              variant="outlined"
              fullWidth
              value={title}
              onChange={(event) => setTitle(event.target.value)}
              required
            />
          </Box>
          <Box mb={2}>
            <TextField
              label="Description"
              variant="outlined"
              fullWidth
              multiline
              rows={4}
              value={description}
              onChange={(event) => setDescription(event.target.value)}
              required
            />
          </Box>
          <Box mb={2}>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
              <DatePicker
                label="Due Date"
                value={dueDate}
                onChange={(newValue) => setDueDate(newValue)}
                renderInput={(params) => <TextField {...params} />}
              />
            </LocalizationProvider>
          </Box>
          <Box display="flex" justifyContent="flex-end">
            <Button type="submit" variant="contained" color="primary">
              Create
            </Button>
          </Box>
        </form>
      </Box>
    </Container>
  );
};

// Define propTypes for the TicketForm component
TicketForm.propTypes = {
  onSubmit: PropTypes.func.isRequired, // Ensure onSubmit is a required function prop
};

export default TicketForm;
