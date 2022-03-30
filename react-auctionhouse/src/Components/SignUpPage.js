import React from "react";
import {Link} from 'react-router-dom';

const SignUpPage = () =>{
    return(
        <div className='login-container'>
            <form className='login-form'>
                <input className='input-login' type="text" placeholder={"login"}></input>
                <input className='input-email' type="text"placeholder={"e-mail"}></input>
                <input className='input-password' type="text"placeholder={"password"}></input>
                <button className='login-btn'>Register</button>
                <span className='signup-comm'>
                    <Link to="/">Sign In!</Link>
                </span>
            </form> 
        </div>
    )
}

export default SignUpPage;