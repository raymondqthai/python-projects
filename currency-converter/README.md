# Currency Converter

A terminal-based currency converter built in Python. Enter a base currency and an amount, and the script returns real-time exchange rates for ten major currencies. Built as a learning project to practice API requests, functions, and input validation.

---

## Features

- Fetches live exchange rates from the Free Currency API
- Accepts a user-defined base currency and amount
- Converts to ten major currencies: USD, EUR, JPY, GBP, CNY, CAD, AUD, CHF, HKD, SGD
- Validates user input before processing
- Displays each converted amount with the exchange rate used
- Loops until the user quits

---

## Requirements

- Python 3.x
- A free API key from [freecurrencyapi.com](https://freecurrencyapi.com/)

Install the required library:

```
pip install requests
```

---

## Setup

1. Clone the repository
   ```
   git clone https://github.com/raymondqthai/python-projects.git
   ```
2. Navigate to the folder
   ```
   cd currency-converter
   ```
3. Open `currency_converter.py` and replace the `API_KEY` value with your own key from the Free Currency API dashboard.

4. Run the script
   ```
   python currency_converter.py
   ```

---

## Usage

```
Enter the base currency (q for quit): USD
What is the amount you would like to convert? 100
EUR: 0.921300 x 100.00 = 92.13
JPY: 149.820000 x 100.00 = 14982.00
GBP: 0.787400 x 100.00 = 78.74
CNY: 7.241000 x 100.00 = 724.10
...
```

Enter `q` to quit.

---

## What I Learned

- How to send HTTP requests and parse JSON responses using the `requests` library
- How to use f-strings to build dynamic API URLs
- How to validate user input with a `while` loop
- How to format and display dictionary data with a `for` loop
- How to handle errors with `try` and `except` blocks

---

## Credits

Based on Project 1 of 3 from "3 Python Automation Projects - For Beginners" by Tech With Tim.
Tutorial: [https://www.youtube.com/watch?v=zT7niRUOs9o](https://www.youtube.com/watch?v=zT7niRUOs9o)
API documentation: [https://freecurrencyapi.com/docs](https://freecurrencyapi.com/docs)