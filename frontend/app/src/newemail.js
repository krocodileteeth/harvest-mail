import React from 'react';
import { useForm } from 'react-hook-form';

const NewEmail = () => {
  return (
    <div className='newemail'>
        <h1>New Email</h1>
        <form id='contact-form' onSubmit={handleSubmit(onSubmit)}>
            <input type='text' name='user_name' ref={register} placeholder='Name' />
            <br/>
            <input type='email' name='user_email' ref={register} placeholder='Email' />
            <br/>
            <textarea name='message' ref={register} placeholder='Message'/>
            <br/>
            <input type='submit' value='Send' />
        </form>
    </div>
  );
}
const { register, handleSubmit, watch, errors } = useForm();
const onSubmit = data => console.log(data);

export default NewEmail;