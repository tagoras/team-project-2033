import React from 'react';
import { useForm } from 'react-hook-form';

function UserPage(){
   const {register, handleSubmit, reset} = useForm();
   const onSubmit = (data) =>{
       fetch("/User", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json;charset=utf-8'},
        body: JSON.stringify(data),
      }).then(
        (value) => {
          console.log(value);
        }
      );
       reset();
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