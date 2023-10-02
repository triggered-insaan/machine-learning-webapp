# **Machine Learning Web App**

This web application implements a machine learning model created by [CodeWithHarry](https://www.youtube.com/@CodeWithHarry) as part of the [Project 1: End To End Python ML Project (Complete)](https://www.youtube.com/watch?v=iIkJrwVUl1c) YouTube video tutorial. The web app allows users to interact with and utilize the machine learning model demonstrated in the video. You can find the original source code and tutorial [here](https://www.codewithharry.com/videos/ml-tutorials-in-hindi-20/).

## **Table of Contents**

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [Contributing](#contributing)
- [License](#license)

## **Overview**

This web app is an implementation of the Machine learning project created by CodeWithHarry. The model has been trained on a dataset, which is available [here](https://github.com/triggered-insaan/Machine-Learning/blob/master/data.csv).

## **Getting Started**

To use the web app, please visit [this link](https://dragon-lww8.onrender.com/).

### **Prerequisites**

Before using the web app, make sure you have the following dependencies installed:

- numpy
- scikit-learn
- aiohttp
- Flask
- gunicorn

### **Installation**

Follow these steps to set up and run the web app:  

Clone the repository
```bash
git clone https://github.com/triggered-insaan/machine-learning-webapp.git
```

Change to the project directory
```bash
cd machine-learning-webapp
```

Install dependencies
```bash
pip install -r requirements.txt
```

Run the web app
```bash
gunicorn app:app
``````
