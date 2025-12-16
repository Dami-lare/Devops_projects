function getWeather() {
  const city = document.getElementById("city").value;
  fetch(`/api/weather?city=${city}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
    });
}
