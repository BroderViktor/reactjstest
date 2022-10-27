import React from 'react'
import logo from './logo.svg';
import './App.css';

function App() {

  const [data, setData] = React.useState(null);

  /*React.useEffect(() => {
    fetch("https://tt02.altinn.no/api/authentication/authenticatewithpassword", {
      method: "POST",
      headers: ({
        //'Authorization': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766',
      }),
      body: ({
        "UserName": "brasa1",
        "UserPassword": "passord123"
      })
    }).then((res) => console.log(res)).then((data) => console.log(data))
  });*/
  React.useEffect(() => {
    fetch("https://tt02.altinn.no/api/metadata?language=1044", {
      method: "GET",
      headers: ({
        //'Authorization': '7A2BA1FE-384E-4793-BD77-58561B15D766', 
        'Host': 'tt02.altinn.no',
        'Content-Type': 'application/hal+json',
        'Accept': 'application/hal+json',
        //'ApiKey': '7A2BA1FE-384E-4793-BD77-58561B15D766',
      }),
    }).then((res) => console.log(res.json()))
  });

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Test server
        </p>
        <p>Sent fra server: {data}</p>
      </header>
    </div>
  );
}

export default App;
