# Bitcoin Price Alert App
A custom app I wrote in Python that will alert you via email if the price of Bitcoin drops below a specified amount.

### Summary
1. You are asked for a few inputs: Enter your name, Enter your email address (gmail only), Enter your password, Enter an email address to send alerts to, and the amount of Bitcoin by which you want to be alerted.
2. Next, it checks the Coinbase API for the current price (which is updated every minute).
3. If it is NOT below the amount you indicated, it will check again in 5 minutes.
4. If it IS below the amount you indicated, it will send you an email alert, and it will check again in 3 minutes.

### How to run
python bitcoin_price_alert.py

...and follow the prompts