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
  import "@reach/combobox/styles.css"
  import "../GenericFunctions";
  import { sentSyncrhonousAccessRequest } from '../GenericFunctions';
  import Geocode from "react-geocode";
  


const libraries = ['places'];
Geocode.setApiKey("AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw");
function UserPage(){
    //Sets up Google scripts
  const {isLoaded,loadError} = useLoadScript({
         googleMapsApiKey: 'AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw',
         libraries,
     });
  const {register, handleSubmit, reset} = useForm();

//Sents user submission data to the database
  const onSubmit = (data) =>{
        //console.log(data);
        fetch("/submission", {
         method: "PUT",
         headers: {
             'Content-Type': 'application/json;charset=utf-8',
             'Authorization': `Bearer ${document.cookie.substring(10)}`,},
             
         body: JSON.stringify(data),
       },
       ).then(
         (value) => {
           return value.json();
         }
       ).then(
           (result)=>{
               console.log(result);
              },
       );
       reset();
    };
    //Marker coordinates
  const [marker, setMarker] = useState();
  const onMapClick = useCallback((event)=>{
           setMarker({
            lat: event.latLng.lat(),
            lng: event.latLng.lng(),
           },
           );
           
  },[])
  const [center, setCenter] = useState({
    lat: 54.978252,
    lng: -1.617780,
});
//Saves map instance
  const mapRef = useRef();
  const onMapLoad = useCallback((map)=>{
      mapRef.current = map;
  });
//Recenters the map accordind to the marker
  function handleCenter() {
    if (!mapRef.current) return;

    const newPos = mapRef.current.getCenter().toJSON();
    setCenter(newPos);
  }
  //Moves the map to,and zooms in,the specified location
  const goTo = useCallback(({ lat, lng }) => {
    mapRef.current.panTo({ lat, lng });
    mapRef.current.setZoom(16);
  }, []);

  if (loadError) return 'Error loading maps';
  if(!isLoaded) return 'Loading maps';

 //Google map styling
  const mapContainerStyle = {
        position: "absolute",
        top: "70px",
        left: "800px",
        right: "200px",
        bottom: "0px",
        width:'700px',
        height:'430px',  
  }

  const options={
        disableDefaultUI:true,
        zoomControl: true,
    }

    const address = (marker) =>{
        if (marker===undefined){
          return 'empty';
        }
        else{
          Geocode.fromLatLng(marker.lat.toString(),marker.lng.toString()).then(
            (response) => {
              const address = response.results[0].formatted_address;
              console.log(address);
            },
            (error) => {
              console.error(error);
            }
          )
        }
        
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
            <input type={'file'} {...register('picture')}/>
        </div>
        <div className='contactInfo'>
          <label>Address</label>
          {/*TODO: put the return of the function in to the input field*/}
            <input type={'text'} {...register('location')}/>
            
        </div>
      
        <Search goTo={goTo}></Search>
        <GoogleMap className='mapContainer'
        mapContainerStyle={mapContainerStyle} 
        zoom={15} 
        center={center}
        onDragEnd={handleCenter}
        options={options}
        onLoad={onMapLoad}
        onClick={onMapClick }
       
        >  
            {<Marker position={marker} />}
           
            
        </GoogleMap>
        <button>Submit</button>
    </form>
)  
}
function Search({goTo}){
    const {ready, value, suggestions:{status,data},setValue, clearSuggestions} = usePlacesAutocomplete({
        requestOptions: {
            location: {lat:() =>54.978252,lng:() =>-1.617780},
            radius:100*1000,
        }
    });
        return (
        <div className='contactInfo'>
            <Combobox className='contactInfo'
            onSelect={async (address)=>{
                setValue(address,false);
                clearSuggestions();
                try{
                    const results = await getGeocode({ address });
                    console.log(results);
                    const { lat, lng } = await getLatLng(results[0]);
                    goTo({lat,lng});
                }
                catch(error){
                    console.log(error);
                }
                }}>
                <ComboboxInput
                className="city-search-input" 
                value={value} 
                onChange={(e)=>{setValue(e.target.value);}}
                disabled={!ready}
                placeholder='Enter Address here'
                />
                <ComboboxList>
                    <ComboboxPopover>
                        {status==="OK" && data.map(({id, description})=><ComboboxOption key={id} value={description}/>)}
                    </ComboboxPopover>
                </ComboboxList>
            </Combobox>
        </div>
        )
}
export default UserPage;