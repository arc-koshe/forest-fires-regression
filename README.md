# Fire Weather Index (FWI) Prediction

This project predicts the Fire Weather Index (FWI) based on various meteorological and environmental parameters. The prediction model is built using **Ridge Regression** from the **scikit-learn** library in Python and served via a **Flask** web application.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Model Details](#model-details)
6. [Contributing](#contributing)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)

## Overview

The Fire Weather Index (FWI) is a measure used to estimate the risk of fire occurrence based on weather conditions. This project provides an interface to input relevant data such as temperature, relative humidity, wind speed, and others to predict the FWI. It can be helpful for fire management and prevention efforts.

## Features

- **Input Parameters**: 
  - Temperature
  - Relative Humidity (RH)
  - Wind Speed (Ws)
  - Rain
  - Fine Fuel Moisture Code (FFMC)
  - Duff Moisture Code (DMC)
  - Drought Code (DC)
  - Initial Spread Index (ISI)
  - Buildup Index (BUI)
  - Class (fire or not fire)
  - Region (Bejaia or Sidi-Bel Abbes)
- **Prediction Output**: Provides the FWI prediction based on the given inputs.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/arc-koshe/forest-fires-regression
   cd FWI-Prediction

2. **Create a Virtual Environment and activate it:**

    ```bash
    conda create -p venv python==3.12

3. **Install the required packages:**

     ```bash
     pip install -r requirements.txt

## Usage

1. **Run the Flask application**

     ```bash
     python application.py

2. **Access the web interface:**

  Access the application by opening your browser and going to http://localhost:5000/predictdata

3. **Enter the required parameters and click "Predict" to get the FWI prediction:**

![Screenshot 2024-08-06 at 22 13 09](https://github.com/user-attachments/assets/e397cb96-cf97-40e2-83e2-dea548835ade)

![Screenshot 2024-08-06 at 22 45 04](https://github.com/user-attachments/assets/bb6c3c80-3df6-4ea0-8162-c6c2a31c9bbc)

## Model Details:

The prediction model uses Ridge Regression, a type of linear regression that includes an L2 regularization term to prevent overfitting. This choice was made to balance bias and variance, leading to more robust predictions. This model achieves an R-2 score of 98.81%
- Libraries Used:
  - Scikit-learn
  - Flask
  - Pandas
  - Nunpy
  - matplotlib


