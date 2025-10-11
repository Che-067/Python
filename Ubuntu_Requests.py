'''
our Task

Requirements

Use the requests library to fetch the image

Check for HTTP errors and handle them appropriately

Create the directory if it doesn't exist using os.makedirs() with exist_ok=True

Extract the filename from the URL or generate one if not available

Save the image in binary mode

Ubuntu Principles to Implement

Community: Your program should connect to the wider web community

Respect: Handle errors gracefully without crashing

Sharing: Organize the fetched images for later sharing

Practicality: Create a tool that serves a real need

Save Your Work in a GitHub Repo Called "Ubuntu_Requests" and Submit the URL for this Repository to Complete the Assignment. 
'''


'''
Create a Python script that:

Prompts the user for a URL containing an image

Creates a directory called "Fetched_Images" if it doesn't exist

Downloads the image from the provided URL

Saves it to the Fetched_Images directory with an appropriate filename

Handles errors gracefully, respecting that not all connections succeed

'''

import requests
import os
image_url = input('Enter image url: ')
file_name = 'Downloaded_image.png'
try:
    response = requests.get(image_url)
except requests.exceptions.SSLError:
    print('SSL Error detected.Trying without verification...')

if response.status_code == 200:
# requesting for data from image_url
    os.makedirs('Fetched_image', exist_ok=True)
    # saving the file
    with open(f'Fetched_image/{file_name}','wb') as file:
        file.write(response.content)
    print(f'imaged saved as: Fetched_image/{file_name}')
else:
    print(f'Download failed, status code: {response.status_code}')


