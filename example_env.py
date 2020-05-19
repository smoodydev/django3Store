#                     Minimum Requirements

# For setting environmental variables
import os

# Your Django Secret Key for Hashing, creating Tokens, prevent cross site attacks.
os.environ.setdefault("SECRET_KEY", "YOUR_SECRET_KEY")

# If you are developing you can have this environemental variable.  Remove for deployment and for generating databases 
os.environ.setdefault("DEVELOPMENT", "1")




#                   ADDITIONAL KEYS

# Sending emails

# Your email address
os.environ.setdefault("EMAIL_HOST_USER", "example@gmail.com")

# if you are using Gmail and have set up an app password or else your Password
os.environ.setdefault("EMAIL_HOST_PASS", "SECRET_GMAIL_PASSWORD")


# AWS

# If you want to connect to AWS
os.environ.setdefault('USE_AWS', "1")

# Three values only needed IF you are using AWS and have USE_AWS as a value
os.environ.setdefault('AWS_BUCKET_NAME', "YOUR_BUCKET_NAME")
os.environ.setdefault('AWS_ACCESS_KEY_ID', "YOUR_AWS_ACCESS_KEY")
os.environ.setdefault('AWS_SECRET_ACCESS_KEY', "YOUR_AWS_SECRET_KEY")
