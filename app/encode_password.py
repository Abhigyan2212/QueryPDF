import urllib.parse

password = "Abhi@123"
encoded_password = urllib.parse.quote(password)

# Print the encoded password
print("Encoded Password:", encoded_password)