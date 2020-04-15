# Web browser module
# --------------------------------------------------------
# (sys module for the command line arguments)
import webbrowser,pyperclip, sys 

sys.argv # ['mapit.py', '870', 'Valencia', 'St']

# Check if the command arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() # takes whatever text we have copied
    webbrowser.open('https://www.google.com/maps/place/' + address)


# Request module (https://requests.readthedocs.io/en/master/user/quickstart)
# --------------------------------------------------------
import requests

# Downloanding from the web
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(res.status_code)
print(len(res.text))
print(res.text[0:500])

# Handling errors
bad_request = requests.get('http://automatetheboringstuff.com/files/dewujf')
print(bad_request.raise_for_status())

# Save web information in our computer
web_file = open('romeo_julieta.txt', 'wb') # binary data to not modify the original text

for chunk in res.iter_content(100000): # making a byte type object and iterating
    web_file.write(chunk)

web_file.close()

