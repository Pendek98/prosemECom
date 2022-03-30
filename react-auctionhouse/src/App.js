import './App.css';
import LogInPage from './Components/LogInPage';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import SignUpPage from './Components/SignUpPage';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<LogInPage />} />
          <Route path='/register' element={<SignUpPage />} />
        </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
