import React, { useState,useCallback, useRef } from 'react';
import { useForm } from 'react-hook-form';
import backgroundImage from "../Components/Photos/x.jpg";
import {GoogleMap,useLoadScript, Marker} from '@react-google-maps/api';
import './User.style.css';
import {useNavigate} from 'react-router-dom';
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
import Geocode from "react-geocode";
import {sentSyncrhonousAccessRequest} from '../GenericFunctions';
import {navigate} from 'react-router-dom';


const libraries = ['places'];
Geocode.setApiKey("AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw");

function UserPage() {
    //Sets up Google scripts
    const {isLoaded, loadError} = useLoadScript({
        googleMapsApiKey: 'AIzaSyAi4NJSYk62SkXRXqDDwjaGAoo4e30rkjw',
        libraries,
    });
  const {register, handleSubmit} = useForm();
  const [name, setName] = useState();
  const [email, setEmail] = useState();
  const [description, setDescription] = useState();
  const [selectedFile, setSelectedFile] = useState(null);
//Sents user submission data to the database
  const onSubmit = (data) =>{
      data['location'] = addressRef.current;
      console.log(data);
      // console.log(JSON.stringify(data.location, data.email, data.name, data.desc),);
      let json_body = {
          'name': data.name,
          'description': data.name,
          'location': data.name,
          'date': data.date,

      }

      let result = fetch("/submission", {
              method: "PUT",
              headers: {
                  'Content-Type': 'application/json;charset=utf-8',
                  'Authorization': `Bearer ${document.cookie.substring(10)}`,
              },

              body: JSON.stringify(json_body)
          },
          // setName(""), setEmail(""), setDescription(""),
      );
      let resultInJSON = result.then((result) => result.json());
      resultInJSON.then((result) => console.log(result));

      let sendRawImage = fetch("/submission_file/2", {
          method: "PUT",
          headers: {
              'Content-Type': 'application/json;charset=utf-8',
              'Authorization': `Bearer ${document.cookie.substring(10)}`,
          },

          body: data.picture[0],
      })
      sendRawImage.then((result) => result.json()).then((resultInJSON) => console.log(resultInJSON));

  };

    // if(!access) return null;
    // let result = sentSyncrhonousAccessRequest('/get_role', 'GET');
    // result.then((value) => {
    //   console.log(value);
    //   if(value.role != 'user'){
    //     setAccess(false);
    //   }else setAccess(true);
    // });
    let navigate = useNavigate();
    let result = sentSyncrhonousAccessRequest('/get_role', 'GET').then((jsonResult) => {
        if (jsonResult.role != 'user') {
            console.log(jsonResult.role);
            navigate('/login');
        }
    })

    const addressRef = useRef();
    //Marker coordinates
    const [marker, setMarker] = useState();
    const onMapClick = useCallback((event) => {
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

//  Google map styling
  const mapContainerStyle = {
      width: "100%",
      height: "100%"
  }

  const options={
        disableDefaultUI:true,
        zoomControl: true,
    }

  const address = (marker) =>{
      if (marker===undefined){
        return addressRef.current;
      }
      else{
        Geocode.fromLatLng(marker.lat.toString(),marker.lng.toString()).then(
          (response) => {
            const address = response.results[0].formatted_address;
            addressRef.current=address;
            //console.log(address);
          },
          (error) => {
            console.error(error);
          }
        )
        return addressRef.current
      }
      
  }
 return(
   <div className='MainComplaintContainer'>
   <div className='FormIntroduction selectedWidth'>
   <h1 className='h1-user'>Complaint submission</h1>
    <p className='p-user'>Here you can submit your infastructure complaint. <br/> Our team will contact you once the issue has been reviewed.</p>
    </div>
   <div className='ComplaintFormContainer'>
    <form onSubmit={handleSubmit(onSubmit)} className='SubmitComplaintForm selectedWidth'>
        
        <div className="contactInfo">
            <label>Name</label>
            <input className="input-user" type={'text'} value={name} onChange={(e) => setName(e.target.value)} {...register('name')}></input>
            <label>Email</label>
            <input className="input-user" type={'text'} value={email} onChange={(e) => setEmail(e.target.value)} {...register('email')} ></input>
            <label>Descripton</label>
            <input className="input-user" type={'textarea'} value={description} onChange={(e) => setDescription(e.target.value)} {...register('description')} ></input>
            <input className="input-user" type={'file'} value={selectedFile} onChange={(e) => setSelectedFile(e.target.files[0])} {...register('picture')}/>
            <label>Address</label>
            <input className="input-user" type={'text'} value={address(marker)}/>
            
        </div>
       
    </form>
    </div>
    <hr className='SectionBreaker selectedWidth'/>
    <h3 className='PleaseSelectPlace selectedWidth'>Please select the place from the map below</h3>
    <div className='GoogleMapContainer selectedWidth'>
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
    </div>
    <button onClick={handleSubmit(onSubmit)} className='SubmitComplaintButton selectedWidth'>Submit</button>    
    </div>
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
        <div className='searchBar'>
            <Combobox 
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
                className="city-search-input" 
                value={value} 
                onChange={(e)=>{setValue(e.target.value);}}
                disabled={!ready}
                placeholder='Search address here'
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