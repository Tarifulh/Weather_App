let cityInput = document.getElementById("cityInput");
let searchButton = document.getElementById("searchButton");


function searchWeather() {

    let city = cityInput.value;

    let url = "http://127.0.0.1:5000/weather?city=" + encodeURI(city);

    document.getElementById("conditions").textContent = "Loading...";

    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Weather request failed")
            }
            
            return response.json();
        })
        .then(data => {

            document.getElementById("temperature").textContent = data.temperature;
            document.getElementById("humidity").textContent = data.humidity;
            document.getElementById("wind").textContent = data.wind_speed;
            document.getElementById("feels").textContent = data.feels_like;
            document.getElementById("visibility").textContent = data.visibility;
            document.getElementById("precipitations").textContent = data.precipitation;
            document.getElementById("snowfalls").textContent = data.snowfall;
            document.getElementById("conditions").textContent = data.condition;

        })
        .catch(error => {
            console.log(error);
            document.getElementById("conditions").textContent = "Unable to get weather";

        });
}


// When Search button is clicked
searchButton.addEventListener("click", searchWeather);


// When Enter is pressed inside the input box
cityInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {
        searchWeather();
    }           

});