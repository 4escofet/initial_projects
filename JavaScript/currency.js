document.addEventListener('click', function() {
    var myHeaders = new Headers();
    myHeaders.append("apikey", "uWk92CTCRANCWAcffh54Jjpt9Ps0AGhw");
    
    var requestOptions = {
      method: 'GET',
      redirect: 'follow',
      headers: myHeaders
    };
    let rate = 0.1;
    fetch("https://api.apilayer.com/exchangerates_data/convert?to=ARS&from=USD&amount=1", requestOptions)
      .then(response => response.json())
      .then(result => {
        console.log(result)
        rate = result.info.rate
        // Display message on the screen
        document.querySelector('body').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ARS.`;
      })
      .catch(error => console.log('error', error));

      //const rate = result;

    
});