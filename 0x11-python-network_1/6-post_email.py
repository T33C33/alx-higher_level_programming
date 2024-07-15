#!/usr/bin/python3
"""
a Python script that takes in a URL and
an email address,
sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response.
Usage: python3 6-post_email.py <URL> <email>
"""
import requests
import sys

# Get the URL and email address from command line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email as the value for the 'email' key
param = {'email': email}

# Send a POST request to the URL with the payload data
response = requests.post(url, data=param)

# Print the email address and the body of the response
print("Your email is:", email)
print(response.text)
