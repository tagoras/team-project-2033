import React, { useState,useCallback, useRef } from 'react';
import { useForm } from 'react-hook-form';
import {GoogleMap,useLoadScript, Marker} from '@react-google-maps/api';
import './User.style.css';
import usePlacesAutocomplete, {
    getGeocode,
    getLatLng,
  } from "use-places-autocomplete";
  import {
    Combobox,
    ComboboxInput,
    ComboboxPopover,
    ComboboxList,
    ComboboxOption,
  } from "@reach/combobox";
  import { formatRelative } from "date-fns";



const libraries = ['places'];

function UserPage(){
  const {isLoaded,loadError} = useLoadScript({
         googleMapsApiKey: 'AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw',
         libraries,
     });
  const {register, handleSubmit, reset} = useForm();
  //FIX: file and address are not being sent to the DB
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
  const [marker, setMarker] = useState();

  const onMapClick = useCallback((event)=>{
      console.log(event.latLng.lat());
      console.log(event.latLng.lng());
           setMarker({
            lat: event.latLng.lat(),
            lng: event.latLng.lng(),
            time: new Date(),
           }
           );
           
  },[])
  const mapRef = useRef();
  const onMapLoad = useCallback((map)=>{
      mapRef.current = map;
  });
  const goTo = useCallback(({ lat, lng }) => {
    mapRef.current.panTo({ lat, lng });
    mapRef.current.setZoom(16);
  }, []);
  if (loadError) return 'Error loading maps';
  if(!isLoaded) return 'Loading maps';
 
  const mapContainerStyle = {
        position: "absolute",
        top: "70px",
        left: "800px",
        right: "200px",
        bottom: "0px",
        width:'700px',
        height:'430px',  
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
        {/* FIX: returns 'undifined' instead of coordinates*/ }
        <Search goTo={goTo} {...register('adress')}  />
        <div >
            
            <GoogleMap className='mapContainer'
            mapContainerStyle={mapContainerStyle} 
            zoom={15} 
            center={center}
            options={options}
            onClick={onMapClick}
            onLoad={onMapLoad}>

                {<Marker position={marker}/>}

            </GoogleMap>
        </div>
        <button>Submit Picture</button>
    </form>
)  
}
//TODO: add to the address that is typed in
function Search({goTo}){
const {ready, value, suggestions:{status,data},setValue, clearSuggestions} = usePlacesAutocomplete({
    requestOptions: {
        location: {lat:() =>54.978252,lng:() =>-1.617780},
        radius:100*1000,
    }
});
    return ( 
        <Combobox className='contactInfo'
        onSelect={async (address)=>{
            setValue(address,false);
            clearSuggestions();
            try{
                const results = await getGeocode({ address });
                const { lat, lng } = await getLatLng(results[0]);
                goTo({lat,lng});
            }
            catch(error){
                console.log(error);
            }
            }}>
            <ComboboxInput 
            value={value} 
            onChange={(e)=>{setValue(e.target.value);}}
            disabled={!ready}
            placeholder='Enter Address here'/>
            <ComboboxList>
                <ComboboxPopover>
                    {status==="OK" && data.map(({id, description})=><ComboboxOption key={id} value={description}/>)}
                </ComboboxPopover>
            </ComboboxList>
        </Combobox>


    )
}
export default UserPage;