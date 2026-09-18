# Beauty Shop NLP Chatbot

## Project Overview

The **Beauty Shop NLP Chatbot** is a Python-based chatbot application built with **Streamlit** and **TextBlob**.

The chatbot helps customers get information about beauty products, prices, opening hours, recommendations, and appointments. Customers can also book appointments through the application, and the appointment details are saved in a CSV file for future reference.

## Features

* Customer greeting and conversation
* Natural Language Processing using TextBlob
* Sentiment analysis
* Intent detection
* Skincare product information
* Makeup product information
* Hair product information
* Product prices
* Opening hours
* Product recommendations
* Appointment booking
* Appointment information storage
* View saved appointments
* CSV file storage
* Streamlit web interface

## Technologies Used

* Python
* Streamlit
* TextBlob
* Pandas
* CSV
* JupyterLab
* GitHub

## Project Structure

```text
Beauty-Shop-NLP-Chatbot/
│
├── app.py
├── beauty_appointments.csv
├── requirements.txt
└── README.md
```

## How the Chatbot Works

The chatbot follows these main steps:

```text
Customer Message
       |
       v
Text Processing
       |
       v
Intent Detection
       |
       v
Sentiment Analysis
       |
       v
Response Generation
       |
       v
Bot Response
```

## Chatbot Intents

The chatbot can recognize different types of customer requests.

| Intent         | Example                       |
| -------------- | ----------------------------- |
| Greeting       | Hello                         |
| Appointment    | I want to book an appointment |
| Skincare       | Show me skincare products     |
| Makeup         | What makeup do you have?      |
| Hair           | Do you have hair products?    |
| Price          | How much is the foundation?   |
| Time           | What time do you open?        |
| Recommendation | What do you recommend?        |
| Help           | Can you help me?              |
| Goodbye        | Bye                           |

## Products and Prices

### Skincare

| Product         |     Price |
| --------------- | --------: |
| Face Wash       |   KSh 800 |
| Facial Cleanser | KSh 1,000 |
| Moisturizer     | KSh 1,200 |
| Face Serum      | KSh 1,500 |
| Sunscreen       | KSh 1,300 |
| Face Mask       |   KSh 700 |
| Body Lotion     | KSh 1,000 |

### Makeup

| Product           |     Price |
| ----------------- | --------: |
| Lipstick          |   KSh 700 |
| Lip Gloss         |   KSh 600 |
| Foundation        | KSh 1,800 |
| Concealer         | KSh 1,200 |
| Mascara           |   KSh 900 |
| Eyeliner          |   KSh 600 |
| Blush             | KSh 1,000 |
| Eyeshadow Palette | KSh 2,000 |

### Hair Products

| Product        |     Price |
| -------------- | --------: |
| Shampoo        |   KSh 900 |
| Conditioner    |   KSh 900 |
| Hair Oil       |   KSh 700 |
| Hair Treatment | KSh 1,500 |
| Hair Gel       |   KSh 600 |
| Edge Control   |   KSh 700 |
| Wig            | KSh 5,000 |

## Appointment Booking

Customers can book an appointment by providing:

* Customer name
* Phone number
* Service
* Appointment date
* Appointment time

Available appointment times:

```text
9:00 AM
11:00 AM
1:00 PM
3:00 PM
5:00 PM
```

Available services include:

```text
Manicure
Pedicure
Facial
Makeup
Hair Styling
Braiding
Bridal Makeup
Eyelashes
```

## Appointment Storage

Appointment information is saved in:

```text
beauty_appointments.csv
```

The CSV file stores:

```text
Customer Name
Phone
Service
Date
Time
```

This allows the application to keep appointment records for future reference.

## Sentiment Analysis

The chatbot uses **TextBlob** to analyze the sentiment of customer messages.

It classifies messages as:

```text
Positive
Negative
Neutral
```

For example:

```text
"I love your makeup products."
```

can be classified as:

```text
Positive
```

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Beauty-Shop-NLP-Chatbot
```

### 3. Install the Required Libraries

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the libraries manually:

```bash
pip install streamlit textblob pandas
```

### 4. Run the Application

Make sure your main Python file is named:

```text
app.py
```

Then run:

```bash
streamlit run app.py
```

Streamlit will provide a local web address where you can open the chatbot.

## Running From JupyterLab

If you are using JupyterLab, open the **Terminal** inside JupyterLab.

Navigate to your project folder:

```bash
cd path/to/Beauty-Shop-NLP-Chatbot
```

Then run:

```bash
streamlit run app.py
```

## Deployment

The application can be deployed online using a Streamlit-compatible hosting service.

Before deployment, make sure your GitHub repository contains:

```text
app.py
requirements.txt
README.md
```

The `requirements.txt` file should contain:

```text
streamlit
textblob
pandas
```

After deploying, the chatbot can be accessed through a web browser.

## Future Improvements

The project can be improved by adding:

* Online database storage
* Customer login
* Admin dashboard
* Appointment cancellation
* Appointment editing
* Automatic appointment reminders
* More beauty products
* Better NLP intent detection
* Online payment integration
* Customer history
* WhatsApp integration

## Learning Objectives

This project demonstrates how to:

* Build a simple NLP chatbot
* Use TextBlob for sentiment analysis
* Detect user intents
* Create a Streamlit web application
* Collect information from users
* Save data using CSV files
* Display stored data using Pandas
* Run a Python application online
* Prepare a project for GitHub and deployment

## Author

**Beauty Shop NLP Chatbot Project**

Built using Python, Streamlit, TextBlob, and Pandas.
