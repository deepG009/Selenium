# Selenium Flipkart Automation

This Python script utilizes Selenium in conjunction with undetected_chromedriver to automate interactions with the Flipkart website. The automation involves opening the Flipkart homepage, entering a phone number into the login form, and simulating a click on the login button. A 25-second delay ensures that the page fully loads before extracting and saving the session cookies into a binary file named "flipkartcookies3.pkl" using the Pickle module.

## Prerequisites

Make sure you have Python installed on your machine. Install the required dependencies by running:

```bash

pip install undetected-chromedriver
pip install selenium

## Usage
Clone this repository: 

git clone https://github.com/deepghuge/Selenium-CookieLogin.git
cd Flipkart_cookie_dump.py 
(for extracting login cookies)

cd Flipkart_cookie_load.py
(for login using extracted cookies, but make sure to make relevant your problem-specific changes in highlighted fields marked in the code)

 Run the script:

 python Flipkart_cookie_dump.py

 ##Configuration
 You can modify the script to perform different actions on the Flipkart website by adjusting the relevant code sections.


 ##License
 This project is licensed under the MIT License - see the LICENSE.md file for details.
