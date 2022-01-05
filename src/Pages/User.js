import React from 'react';
import { useForm } from 'react-hook-form';

function UserPage(){
   const {register, handleSubmit, reset} = useForm();
   const onSubmit = (data) =>{
       console.log(data)
       reset();
        //TODO: after the fields are resetted, file input is not saved
   }
       return(
        <form onSubmit={handleSubmit(onSubmit)}>
            <h1>User page</h1>
            <div className="contactInfo">
                <label>Name</label>
                <input type={'text'} {...register('name')}></input>
            </div>
            <div className="contactInfo">
                <label>Email</label>
                <input type={'text'} {...register('email')} ></input>
            </div>
            <div className="contactInfo">
                <label>Descripton</label>
                <input type={'textarea'} {...register('description')} ></input>
            </div>
            <div className='picture'>
                <input type='file' name='picture' {...register('picture')} />
                <button>Submit Picture</button>
            </div>
        </form>
    )
    
}
export default UserPage;