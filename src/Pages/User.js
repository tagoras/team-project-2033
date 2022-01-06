import React, { useState,useCallback } from 'react';
import { useForm } from 'react-hook-form';
import {GoogleMap,useLoadScript, Marker} from '@react-google-maps/api';
import './User.style.css';


const libraries = ['places'];

function UserPage(){
  const {isLoaded,loadError} = useLoadScript({
         googleMapsApiKey: 'AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw',
         libraries,
     });
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
  const [markers, setMarkers] = useState([]);
  const onMapClick = useCallback((event)=>{        
           setMarkers(current =>[...current,{
               lat: event.latLng.lat(),
               lng: event.latLng.lng(),
               time: new Date(),
           }]);
  },[])

  if (loadError) return 'Error loading maps';
  if(!isLoaded) return 'Loading maps';
 
  const mapContainerStyle = {
        width:'400px',
        height:'400px',     
  }
  
  const center ={
        lat: 54.978252,
        lng: -1.617780,
    }
  const options={
        disableDefaultUI:true,
        zoomControl: true,
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
        </div>
        <div className='mapContainer'>
            <GoogleMap 
            mapContainerStyle={mapContainerStyle} 
            zoom={15} 
            center={center}
            options={options}
            onClick={onMapClick}>
                {markers.map(marker => <Marker 
                key={marker.time.toISOString()} 
                position={{lat:marker.lat, lng:marker.lng}}/>)
                //TODO: make that only one marker apears at a time
            }
            </GoogleMap>
        </div>
        <button>Submit Picture</button>
        
    </form>
)
    
}
export default UserPage;
