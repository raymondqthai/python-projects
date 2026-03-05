# Automated Cookie Clicker

A Python script that automates the browser game Cookie Clicker using Selenium. It clicks the cookie repeatedly and buys upgrades automatically when you have enough cookies. Built as a learning project to practice browser automation, looping logic, and dynamic element interaction.

---

## Features

- Opens Cookie Clicker in Chrome automatically
- Selects the English language on startup
- Clicks the cookie in a continuous loop
- Reads your current cookie count from the page
- Buys the first available upgrade when you can afford it
- Skips upgrades with non-numeric prices to avoid crashes

---

## Requirements

You need Python installed. Then install Selenium:

```
pip3 install selenium
```

Selenium on Mac automatically downloads the correct ChromeDriver for you. No manual setup or download needed.

**Windows users:** You need to download ChromeDriver manually and update the script to use the `Service` path. Instructions are in the comments inside `automated_cookie_clickers.py`.

---

## How to Run

1. Clone the repository
   ```
   git clone https://github.com/yourusername/your-repo.git
   ```
2. Navigate to the folder
   ```
   cd your-repo
   ```
3. Run the script
   ```
   python3 automated_cookie_clickers.py
   ```

A Chrome window will open, load Cookie Clicker, and start playing on its own. To stop it, close the terminal or press `Ctrl + C`.

---

## No API Key Required

This tool works out of the box. You do not need to register for any service or set up API credentials.

---

## Usage

Once running, the script performs these steps automatically:

```
1. Opens https://g8hh.github.io/cookieclicker/
2. Clicks "English" to set the language
3. Finds the big cookie and starts clicking
4. Checks your cookie count after each click
5. Scans the first 4 upgrades for an affordable price
6. Buys the first upgrade it can afford, then keeps clicking
```

The game link used here bypasses the Cloudflare CAPTCHA on the original Cookie Clicker site, so the script loads without interruption.

---

## What I Learned

- How to find HTML elements using XPATH with text content matching
- How to parse and clean live text from a webpage (removing commas from numbers)
- How to write a loop that reads page state and makes decisions on each iteration
- How to handle non-numeric edge cases with input validation
- How Selenium on Mac auto-manages ChromeDriver, removing the need for manual setup

---

## Credits

Based on a tutorial by Tech With Tim.
Link: https://www.youtube.com/watch?v=NB8OceGZGjA&t=101s

The Cookie Clicker link was changed to bypass Cloudflare CAPTCHA, and the script was adjusted to remove the manual ChromeDriver setup step.
