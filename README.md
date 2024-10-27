Spam Detection Streamlit App
============================

This repository contains a **Streamlit web application** for the **Spam Detection Model**. The app allows users to enter text and check whether it is classified as spam or not spam, using natural language processing and machine learning techniques.

Table of Contents
-----------------

1.  [Project Overview](#project-overview)
2.  [Features](#features)
3.  [Technologies Used](#technologies-used)
4.  [Installation](#installation)
5.  [Usage](#usage)
6.  [Contributing](#contributing)
7.  [License](#license)

Project Overview
----------------

The Spam Detection Streamlit App uses a trained machine learning model to detect spam messages in real-time. Users can input messages, and the model will classify each message as either "spam" or "ham (for not spam)."

Features
--------

-   **Real-time Spam Detection**: Users can enter text messages to check for spam.
-   **Interactive Interface**: Simple, user-friendly UI built with Streamlit.
-   **Clear Results**: Displays the classification result

Technologies Used
-----------------

-   **Streamlit**: For building the web app interface
-   **Python**: Core programming language
-   **NLTK**: Used for text preprocessing and NLP tasks in the model
-   **Scikit-learn**: For training the spam detection model
-   **Pandas and NumPy**: For data manipulation and numerical operations

Installation
------------

1.  Clone this repository:

    `git clone https://github.com/bonk18/spam-detection-app.git`

2.  Navigate to the project directory:

    `cd spam-detection-app`

3.  Install the required packages:

    `pip install -r requirements.txt`

4.  Run the Streamlit app:

    `streamlit run app.py`

    > **Note**: Ensure you have Python and Streamlit installed on your system.

Usage
-----

1.  After running the command above, a new tab will open in your web browser displaying the Streamlit app.
2.  Enter a text message you want to classify in the input box.
3.  Press the "Predict" button.
4.  The app will display whether the message is classified as spam or ham, based on the trained model's prediction.

Contributing
------------

Contributions are welcome! To contribute:

1.  Fork the repository.
2.  Create a new branch for your feature (`git checkout -b feature-name`).
3.  Commit your changes (`git commit -m 'Add new feature'`).
4.  Push to the branch (`git push origin feature-name`).
5.  Open a Pull Request.

License
-------

This project is licensed under the GPL-3.0 License. See the LICENSE file for more information.
