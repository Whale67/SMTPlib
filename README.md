# SMTPlib
Using Gmail account without allowing access to insecure apps

To use SMTPlib without allows access from insecure apps:

1) Enable 2-Step Verification on your Gmail account.
2) Follow the steps listed here https://support.google.com/accounts/answer/185833?hl=en to create a App password.
3) In your config file, replace the Gmail password you log into your account with your new 16 digit app password:
    change FROM_PASSWORD = 'your_old_password' to FROM_PASSWORD = 'your_new_16_digit_app_password'
4) You should be good to go using the above.

