import streamlit as st
from textblob import TextBlob
import pandas as pd
import os


# ==========================================
# BEAUTY SHOP NLP CHATBOT
# ==========================================

st.set_page_config(
    page_title="Beauty Shop Chatbot",
    page_icon="💄"
)


# ------------------------------------------
# 1. SENTIMENT ANALYSIS
# ------------------------------------------

def analyze_sentiment(text):

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "positive"

    elif polarity < 0:
        return "negative"

    else:
        return "neutral"


# ------------------------------------------
# 2. INTENT DETECTION
# ------------------------------------------

def detect_intent(message):

    message = message.lower()

    if "hello" in message or "hi" in message or "hey" in message:
        return "greeting"

    elif "appointment" in message or "book" in message or "booking" in message:
        return "appointment"

    elif "appointment list" in message or "show appointments" in message:
        return "show_appointments"

    elif "skin" in message or "skincare" in message:
        return "skincare"

    elif "makeup" in message or "lipstick" in message:
        return "makeup"

    elif "hair" in message or "wig" in message or "shampoo" in message:
        return "hair"

    elif "price" in message or "cost" in message or "how much" in message:
        return "price"

    elif "time" in message or "open" in message or "hours" in message:
        return "time"

    elif "recommend" in message or "suggest" in message:
        return "recommendation"

    elif "help" in message:
        return "help"

    elif "bye" in message or "exit" in message or "quit" in message:
        return "goodbye"

    else:
        return "unknown"


# ------------------------------------------
# 3. GENERATE RESPONSE
# ------------------------------------------

def generate_response(intent):

    if intent == "greeting":

        return """
Hello! Welcome to our Beauty Shop!

I can help you with:
- Skincare
- Makeup
- Hair products
- Prices
- Appointments
- Opening hours
"""

    elif intent == "skincare":

        return """
SKINCARE PRODUCTS

Face Wash - KSh 800
Facial Cleanser - KSh 1,000
Moisturizer - KSh 1,200
Face Serum - KSh 1,500
Sunscreen - KSh 1,300
Face Mask - KSh 700
Body Lotion - KSh 1,000
"""

    elif intent == "makeup":

        return """
MAKEUP PRODUCTS

Lipstick - KSh 700
Lip Gloss - KSh 600
Foundation - KSh 1,800
Concealer - KSh 1,200
Mascara - KSh 900
Eyeliner - KSh 600
Blush - KSh 1,000
Eyeshadow Palette - KSh 2,000
"""

    elif intent == "hair":

        return """
HAIR PRODUCTS

Shampoo - KSh 900
Conditioner - KSh 900
Hair Oil - KSh 700
Hair Treatment - KSh 1,500
Hair Gel - KSh 600
Edge Control - KSh 700
Wig - KSh 5,000
"""

    elif intent == "price":

        return """
BEAUTY SHOP PRICES

Skincare: from KSh 700
Makeup: from KSh 600
Hair products: from KSh 600
"""

    elif intent == "time":

        return """
OPENING HOURS

Monday - Saturday
9:00 AM - 6:00 PM

Available appointment times:

9:00 AM
11:00 AM
1:00 PM
3:00 PM
5:00 PM
"""

    elif intent == "recommendation":

        return """
I can recommend something for you.

You can choose:

1. Skincare
2. Makeup
3. Hair Products
"""

    elif intent == "help":

        return """
I can help you with:

Skincare
Makeup
Hair products
Prices
Book an appointment
View saved appointments
Opening hours
"""

    elif intent == "goodbye":

        return "Thank you for visiting our Beauty Shop. Goodbye!"

    else:

        return """
Sorry, I did not understand.

Try asking about:
- Prices
- Skincare
- Makeup
- Hair
- Appointments
"""


# ------------------------------------------
# 4. SAVE APPOINTMENT
# ------------------------------------------

def save_appointment(
    customer_name,
    phone,
    service,
    date,
    time
):

    file_name = "beauty_appointments.csv"

    appointment = {
        "Customer Name": customer_name,
        "Phone": phone,
        "Service": service,
        "Date": str(date),
        "Time": time
    }

    if os.path.exists(file_name):

        appointments = pd.read_csv(file_name)

        new_appointment = pd.DataFrame([appointment])

        appointments = pd.concat(
            [appointments, new_appointment],
            ignore_index=True
        )

    else:

        appointments = pd.DataFrame([appointment])

    appointments.to_csv(
        file_name,
        index=False
    )


# ==========================================
# STREAMLIT PAGE
# ==========================================

st.title("💄 Beauty Shop Chatbot")

st.write(
    "Welcome to our Beauty Shop. "
    "I can help you with products, prices and appointments."
)

st.divider()


# ==========================================
# CHATBOT
# ==========================================

st.subheader("Chat With Our Bot")

user_message = st.text_input(
    "Customer:",
    placeholder="Type your message..."
)


if st.button("Send Message"):

    if user_message.strip() == "":
        st.warning("Please type a message.")

    else:

        intent = detect_intent(user_message)

        sentiment = analyze_sentiment(user_message)

        response = generate_response(intent)

        st.write("**Customer:**", user_message)

        st.info(response)

        st.write("Intent:", intent)

        st.write("Sentiment:", sentiment)


# ==========================================
# APPOINTMENT BOOKING
# ==========================================

st.divider()

st.subheader("📅 Book an Appointment")

with st.form("appointment_form"):

    customer_name = st.text_input(
        "Your Name"
    )

    phone = st.text_input(
        "Phone Number"
    )

    service = st.selectbox(
        "Choose Service",
        [
            "Manicure",
            "Pedicure",
            "Facial",
            "Makeup",
            "Hair Styling",
            "Braiding",
            "Bridal Makeup",
            "Eyelashes"
        ]
    )

    date = st.date_input(
        "Choose Date"
    )

    time = st.selectbox(
        "Choose Appointment Time",
        [
            "9:00 AM",
            "11:00 AM",
            "1:00 PM",
            "3:00 PM",
            "5:00 PM"
        ]
    )

    submit = st.form_submit_button(
        "Confirm Appointment"
    )


if submit:

    if customer_name and phone:

        save_appointment(
            customer_name,
            phone,
            service,
            date,
            time
        )

        st.success(
            "Appointment confirmed successfully!"
        )

        st.write("Customer:", customer_name)
        st.write("Phone:", phone)
        st.write("Service:", service)
        st.write("Date:", date)
        st.write("Time:", time)

    else:

        st.warning(
            "Please enter your name and phone number."
        )


# ==========================================
# VIEW APPOINTMENTS
# ==========================================

st.divider()

st.subheader("📋 Saved Appointments")

if st.button("View Appointments"):

    file_name = "beauty_appointments.csv"

    if os.path.exists(file_name):

        appointments = pd.read_csv(
            file_name
        )

        st.dataframe(
            appointments,
            use_container_width=True
        )

    else:

        st.info(
            "There are no appointments saved yet."
        )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Beauty Shop NLP Chatbot"
)
