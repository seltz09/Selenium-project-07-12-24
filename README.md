# Selenium Amazon Bot

## Project Description
This project is a Selenium-based bot that automates the process of searching for a GoPro Hero 12 Black on Amazon, adding it to the cart, and proceeding to the checkout page. The script also fills in an email address on the login page.

### What the Bot Does:
1. Opens the Amazon website.
2. Maximizes the browser window.
3. Searches for "Go Pro 12 hero black".
4. Adds the product to the cart.
5. Navigates to the cart.
6. Proceeds to checkout.
7. Enters the email address on the login page.

## Prerequisites
- Python 3.x
- Google Chrome browser
- ChromeDriver (compatible with your Chrome browser version)
- Selenium library

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine:
```sh
git clone https://github.com/seltz09/selenium-amazon-bot.git
cd selenium-amazon-bot

# Step 2: Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux

# Step 3: Install Selenium
pip install selenium

# Step 4: Download ChromeDriver
# Download ChromeDriver from the official site and ensure it matches your Chrome browser version. 
# Place the chromedriver executable in your project directory or add it to your system's PATH.

# Step 5: Update the Script (if necessary)
# If you place chromedriver in a different directory, update the path in the script accordingly.

# Step 6: Run the Script
python test_script.py

