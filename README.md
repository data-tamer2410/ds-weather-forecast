# Weather Forecast API
A Dockerized weather prediction API using an RNN model to forecast next-day conditions based on the past 7 days of weather data.

## Description
This project provides a weather prediction API using a recurrent neural network (RNN). The API predicts weather conditions for the next day based on the past 7 days of data. It has been containerized with Docker and deployed on a server, making it easily accessible via HTTP requests.

## Features

- **Machine Learning Model**: The API utilizes an RNN trained on weather data to provide predictions.
- **Input Requirements**: The API accepts a POST request at `https://rnn-weather-forecast-api.onrender.com/predict/` with the following JSON format:
  ```json
  {
      "data": [
          [MinTemp, MaxTemp, Rainfall, WindGustSpeed, WindSpeed9am, WindSpeed3pm, Pressure9am, Pressure3pm, Temp9am, Temp3pm, WindDir9am, WindDir3pm, Humidity9am, Humidity3pm, Cloud9am, Cloud3pm, RainToday],
          ...
      ]
  }
  ```
  - `data`: A list of 7 sublists, where each sublist contains 17 numerical values representing weather features for a single day.
  - Features include:
    - `MinTemp`: Minimum temperature (°C)
    - `MaxTemp`: Maximum temperature (°C)
    - `Rainfall`: Rainfall amount (mm)
    - `WindGustSpeed`: Maximum wind gust speed (km/h)
    - `WindSpeed9am`, `WindSpeed3pm`: Wind speed (km/h) at 9 AM and 3 PM
    - `Pressure9am`, `Pressure3pm`: Atmospheric pressure (hPa) at 9 AM and 3 PM
    - `Temp9am`, `Temp3pm`: Temperature (°C) at 9 AM and 3 PM
    - `WindDir9am`, `WindDir3pm`: Wind direction at 9 AM and 3 PM
    - `Humidity9am`, `Humidity3pm`: Humidity percentage at 9 AM and 3 PM
    - `Cloud9am`, `Cloud3pm`: Cloud coverage percentage at 9 AM and 3 PM
    - `RainToday`: Binary indicator for rain (0 = No, 1 = Yes)

- **Output**: The API returns a dictionary with predicted values for the following keys:
  - `MaxTemp`: Maximum temperature of the day (°C)
  - `MinTemp`: Minimum temperature of the day (°C)
  - `Pressure3pm`: Atmospheric pressure at 3 PM (hPa)
  - `Pressure9am`: Atmospheric pressure at 9 AM (hPa)
  - `Rainfall`: Amount of rainfall (mm)
  - `Temp3pm`: Temperature at 3 PM (°C)
  - `Temp9am`: Temperature at 9 AM (°C)
  - `WindGustSpeed`: Maximum wind gust speed (km/h)
  - `WindSpeed3pm`: Wind speed at 3 PM (km/h)
  - `WindSpeed9am`: Wind speed at 9 AM (km/h)
  - `RainToday`: Probability of rain (0.0 to 1.0)

## Deployment

The API has been containerized using Docker and deployed on a server. It supports easy scalability and ensures reliable performance. You can test the API or view its documentation at [API Documentation](https://rnn-weather-forecast-api.onrender.com/docs).
