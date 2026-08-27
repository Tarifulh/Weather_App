let cityInput = document.getElementById("cityInput")
let searchButton = document.getElementById("searchButton")
searchButton.addEventListener("click", function(){
    let city = cityInput.value;
    let url = "http://127.0.0.1:5000/weather?city=" + city;
    fetch(url);
});