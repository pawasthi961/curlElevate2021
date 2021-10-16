import './App.css';
import { useState } from 'react';
// import { Button, Alert } from 'react-bootstrap'
import "bootstrap/dist/css/bootstrap.min.css"

function App() { 
  const [imgPreview, setImgPreview] = useState(null);
  const [score,setScore] = useState(0)
  const [showImage, setShowImage]  =  useState(false);

  const handleimageChange = (e) =>
  {
    const selected = e.target.files[0]
    let reader = new FileReader();
    reader.onloadend = () =>
    {
      setImgPreview(reader.result);
    }
    reader.readAsDataURL(selected);
   }
  // const handleImage = () => {
  //   fetch('/plot').
  //   then(function(res){
  //     console.log(res)
  //     setShowImage(true)
  //   })
  // }
  
  const handleScore = (e) =>{
    fetch('/plot').then(res => 
      setImgPreview(res.url)
    ).then(data => {
      
      fetch('/show_result').then(res =>res.json()
        ).then(data =>{
          setScore(data);
          setShowImage(true)
        })
      
    });
    
    
  }

  return (
    <div className="App">
      <header className="App-header">
       <h3 style={{marginTop: 30, fontSize: 40}}>MNist</h3>
      <div style={{marginTop: 150}}>
        <label class="form-label, mb-3" for="customFile">
          Upload the image in .png format 
        </label>
        <input 
          class="form-control" id="formFileLg" type="file" 
          onChange={handleimageChange}
          style={{width:400}} accept='image/png, image/jpg' />
      </div>
      {/* <div className="result"></div> 
      <div 
      className='image'
      style={{background: imgPreview? `url("${imgPreview}") no-repeat center/cover` : "#fff" }}> 
      </div> */}
      <div>
        {showImage ? <img src = {imgPreview} /> : null}
      </div>
      <div>
        <button onClick = {handleScore}>Get Score</button>
      </div>
      <div>{score}</div>
      </header>
    </div>
  );
}

export default App;
