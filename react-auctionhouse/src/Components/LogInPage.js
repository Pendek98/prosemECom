import { React }from 'react';
import '../Styles/loginpage.css'
import { Link } from 'react-router-dom';

const LogInPage = () => {
    return(
        <div className='login-container'>
            <form className='login-form'>
                <input className='input-login' type="text" placeholder={"login"}></input>
                <input className='input-password' type="text"placeholder={"password"}></input>
                <button className='login-btn'>Log In!</button>
                <span className='signup-comm'>Don't have an account yet? <Link to='/register'>Sign Up </Link></span>
            </form> 
        </div>
    )
}

export default LogInPage;