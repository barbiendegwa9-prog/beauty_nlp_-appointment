# Catering Brand NLP Chatbot

## Project Description

The **Catering Brand NLP Chatbot** is a simple Python-based chatbot designed to help customers interact with a catering business.

The chatbot can answer questions about:

* Catering services
* Food and menus
* Cakes and baking
* Events
* Prices
* Delivery
* Booking appointments

The chatbot also uses **Natural Language Processing (NLP)** to detect the customer's intention and **sentiment analysis** to identify whether the customer's message is positive, negative, or neutral.

Customers can also make catering appointments. The appointment information is saved in a CSV file so that it can be viewed later.

---

## Project Objectives

The main objectives of this project are to:

1. Build a simple NLP chatbot using Python.
2. Detect customer intentions from messages.
3. Perform sentiment analysis using TextBlob.
4. Provide automatic responses to customers.
5. Allow customers to book catering appointments.
6. Save appointment information for future reference.
7. Allow saved appointments to be viewed from the chatbot.

---

## Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Programming language                      |
| TextBlob   | Sentiment analysis                        |
| CSV        | Store appointment information             |
| OS         | Check whether the appointment file exists |
| JupyterLab | Development environment                   |

---

## Python Libraries

The project uses the following libraries:

```python
from textblob import TextBlob
import csv
import os
```

### TextBlob

TextBlob is used to analyze the sentiment of customer messages.

For example:

```text
Customer: I love your catering service
```

The chatbot can identify this as:

```text
Positive
```

---

## Main Features

### 1. Greeting

The chatbot recognizes greetings such as:

```text
hello
hi
hey
```

Example:

```text
Customer: Hello

Bot: Hello! Welcome to our catering brand. How can we help you today?
```

---

### 2. Menu Information

Customers can ask about food or menus.

Example:

```text
Customer: What food do you offer?

Bot: We offer meals, snacks, desserts, refreshments and other catering options.
```

---

### 3. Baking and Cakes

The chatbot recognizes questions about:

* Cakes
* Baking
* Pastries

Example:

```text
Customer: Do you make cakes?

Bot: We offer cakes, pastries and other baked products for different occasions.
```

---

### 4. Catering Services

Customers can ask about catering services.

Example:

```text
Customer: Do you provide catering services?

Bot: We provide catering services for weddings, birthdays, parties, meetings and other events.
```

---

### 5. Events

The chatbot can identify events such as:

* Weddings
* Birthdays
* Parties
* Corporate events

Example:

```text
Customer: Do you cater for weddings?

Bot: We cater for weddings, birthdays, parties, corporate events and other special occasions.
```

---

### 6. Prices

Customers can ask about prices.

Example:

```text
Customer: How much does catering cost?

Bot: Our prices depend on the type of service, menu and number of guests.
```

---

### 7. Delivery

Customers can ask about delivery.

Example:

```text
Customer: Do you offer delivery?

Bot: We offer catering delivery depending on the location and order.
```

---

## Appointment Booking

One of the main features of the chatbot is **catering appointment booking**.

When a customer asks to book an appointment, the chatbot collects:

1. Customer name
2. Phone number
3. Event type
4. Event date
5. Event time
6. Event location
7. Number of guests
8. Catering service/package

Example:

```text
Customer: I want to make a booking.

Bot: Sure! I can help you make a catering appointment.

Customer name: Mary
Phone number: 0712345678
Type of event: Wedding
Event date: 20/10/2026
Event time: 2:00 PM
Event location: Nairobi
Number of guests: 100
Catering service/package: Wedding package

Appointment saved successfully!
Thank you, Mary
Your catering appointment has been recorded.
```

---

## Saving Appointments

Appointments are saved in a CSV file called:

```text
catering_appointments.csv
```

The file contains the following columns:

```text
Name
Phone
Event Type
Event Date
Event Time
Location
Guests
Service
```

This allows the business to keep appointment information for future reference.

---

## Viewing Appointments

To view saved appointments, type:

```text
view appointments
```

Example:

```text
Customer: view appointments
```

The chatbot will display the saved bookings.

---

## Intent Detection

The chatbot uses an `detect_intent()` function to identify what the customer wants.

The main intents are:

| Intent   | Example Keywords           |
| -------- | -------------------------- |
| Greeting | hello, hi, hey             |
| Menu     | menu, food, meal           |
| Baking   | cake, baking, pastry       |
| Catering | catering, cater            |
| Events   | event, wedding, party      |
| Price    | price, cost, charge        |
| Booking  | book, booking, appointment |
| Delivery | delivery, deliver          |
| Help     | help, assist               |
| Goodbye  | bye, exit, quit            |

If the chatbot does not recognize the customer's message, it returns:

```text
unknown
```

---

## Sentiment Analysis

The project uses TextBlob to analyze customer sentiment.

There are three possible results:

### Positive

```text
I love your food.
```

Result:

```text
positive
```

### Negative

```text
Your service is bad.
```

Result:

```text
negative
```

### Neutral

```text
I need information about catering.
```

Result:

```text
neutral
```

The sentiment is determined using the polarity score from TextBlob.

---

## Chatbot Workflow

The chatbot follows this process:

```text
Customer Message
       ↓
Text Processing
       ↓
Intent Detection
       ↓
Sentiment Analysis
       ↓
Response Selection
       ↓
Bot Response
       ↓
If Booking → Collect Customer Details
       ↓
Save Appointment to CSV
```

---

## How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

You can also use **Anaconda/JupyterLab**.

---

### Step 2: Open JupyterLab

Open Anaconda Navigator and start:

```text
JupyterLab
```

---

### Step 3: Create a Notebook

Create a new Python notebook.

For example:

```text
Catering_Brand_NLP_Chatbot.ipynb
```

---

### Step 4: Install TextBlob

If TextBlob is not installed, run:

```python
!pip install textblob
```

---

### Step 5: Import Libraries

Run:

```python
from textblob import TextBlob
import csv
import os
```

---

### Step 6: Add the Chatbot Code

Copy the chatbot Python code into your notebook and run the cells.

---

### Step 7: Start the Chatbot

Run the final cell.

You should see:

```text
==========================================
       CATERING BRAND CHATBOT
==========================================
Welcome to our catering service!
Type 'bye' to end the conversation.
Type 'view appointments' to see saved bookings.
```

The chatbot is now ready to receive customer messages.

---

## Example Conversation

```text
Customer: Hello

Bot: Hello! Welcome to our catering brand. How can we help you today?

Customer: What food do you offer?

Bot: We offer meals, snacks, desserts, refreshments and other catering options.

Customer: Do you make cakes?

Bot: We offer cakes, pastries and other baked products for different occasions.

Customer: I want to book

Bot: Sure! I can help you make a catering appointment.

--- CATERING APPOINTMENT ---

Customer name: Jane
Phone number: 0712345678
Type of event: Birthday
Event date: 25/10/2026
Event time: 1:00 PM
Event location: Nairobi
Number of guests: 50
Catering service/package: Birthday package

Appointment saved successfully!
Thank you, Jane
Your catering appointment has been recorded.

Customer: bye

Bot: Goodbye! Thank you for choosing our catering brand.
```

---

## Project Files

A possible project folder structure is:

```text
Catering_NLP_Chatbot/
│
├── Catering_Brand_NLP_Chatbot.ipynb
├── README.md
└── catering_appointments.csv
```

The `catering_appointments.csv` file will be created automatically after the first appointment is saved.

---

## Important Note

This chatbot is a **rule-based NLP chatbot**.

It does not train a machine-learning model or learn automatically from customer conversations.

Instead, Python rules and keywords are used to identify customer intentions and select responses.

The project demonstrates basic concepts of:

* Python programming
* Natural Language Processing (NLP)
* Sentiment Analysis
* Intent Detection
* File Handling
* CSV Data Storage
* Chatbot Development

---

## Future Improvements

The chatbot could be improved by adding:

* A larger menu with food prices
* Catering packages and prices
* Automatic appointment confirmation
* Appointment cancellation
* Appointment editing
* Date and time validation
* Customer order history
* A database such as SQLite or MySQL
* A web interface
* WhatsApp integration
* Online deployment
* A machine-learning-based intent classifier

---

## Conclusion

The Catering Brand NLP Chatbot is a beginner-friendly AI/NLP project that demonstrates how Python can be used to create a customer service chatbot.

It combines **intent detection, sentiment analysis, automatic responses, and appointment storage** to provide a simple catering business solution.

### Author

**Catering Brand NLP Chatbot Project**

### Project Type

**Python + NLP + Chatbot + Appointment Booking**
