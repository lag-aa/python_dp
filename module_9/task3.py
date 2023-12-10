from base64 import urlsafe_b64encode

text = input().encode('utf-8')
print(urlsafe_b64encode(text).decode('utf-8'))