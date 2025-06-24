# M-Pesa STK Push Flask Demo

## Setup

1. Replace values in `config.py`:
   - `consumer_key`
   - `consumer_secret`
   - `passkey`
   - `shortcode`
   - `callback_url`

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run app:

```
python app.py
```

4. Visit `http://127.0.0.1:5000/` in your browser.

## Sandbox Credentials

- Use Safaricom [Daraja Portal](https://developer.safaricom.co.ke/daraja/apis/post/safaricom-safaricom/v1/oauth/generate) to get sandbox credentials.