let cityInput = document.getElementById("cityInput")
let searchButton = document.getElementById("searchButton")

searchButton.addEventListener("click", function() {
    let city = cityInput.value
    let url = "http://127.0.0.1:5000/weather?city=" + encodeURIComponent(city);

    fetch(url)
        .then(response => {
            return response.json()
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
});