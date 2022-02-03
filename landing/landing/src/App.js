import logo from './img/logo.webp';
import './App.css';
import { Typography, Container, Stack } from '@mui/material';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Typography fontFamily='"Condiment", cursive' variant="h1" fontSize={"3.8rem"} className="name">SigNoize</Typography>
      </header>
      <Typography variant="h2" className="Links-title" fontWeight={"600"}>Links</Typography>
      <Stack div className="Links" spacing={0}>
        <a href="https://opensea.io/signoize" target="_blank" rel="noopener noreferrer">
          <Stack item className="OpenSea">
            &nbsp;
          </Stack>
        </a>
        <a href="https://rarible.com/signoize" target="_blank" rel="noopener noreferrer">
          <Stack item className="Rarible">
            &nbsp;
          </Stack>
        </a>
        <a href="https://twitter.com/SigNoizeVisions" target="_blank" rel="noopener noreferrer">
          <Stack item className="Twitter">
            &nbsp;
          </Stack>
        </a>
        <a href="https://www.instagram.com/SigNoizeVisions/" target="_blank" rel="noopener noreferrer">
          <Stack item className="Instagram">
            &nbsp;
          </Stack>
        </a>
      </Stack>
    </div>
  );
}

export default App;
