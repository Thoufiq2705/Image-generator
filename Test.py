import io
import os
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import httpx
import asyncio
import requests

# ------------Tkinter Desktop app for API image generator ----------------------
# root = ctk.CTk()
# root.title('Image Generator')

#
# input_frame = ctk.CTkFrame(root)
# input_frame.pack(side="left", expand='true', padx=10, pady=10)
#
# input_Image = ctk.CTkLabel(input_frame, text='Image')
# input_Image.grid(row=0, column=0, padx=10, pady=10)
# input_search = ctk.CTkTextbox(input_frame, height=10)
# input_search.grid(row=0, column=1, padx=10, pady=10)
# generate_btn = ctk.CTkButton(input_frame, text="Generate Image")
# generate_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='news')
# generate_btn = ctk.CTkButton(input_frame, text="Download Image")
# generate_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='news')
#
# canvas = tk.Canvas(root, width='600', height='600', yscrollcommand='true')
# canvas.pack(side='left')
#
# response = requests.get('https://images.unsplash.com/photo-1510731588248-80ced73bae78?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0ODMzNjF8MHwxfHNlYXJjaHw5Mnx8U2FudGElMjBDbGF1c3xlbnwwfHx8fDE3MDY0NjM5NDd8MA&ixlib=rb-4.0.3&q=80&w=400')
#
# images = Image.open(io.BytesIO(response.content))
# print(images)
# photo_image = ImageTk.PhotoImage(images)
# print(photo_image)
# canvas.create_image(300, 300, anchor="center", image=photo_image)
#
# root.mainloop()

# ------------Tkinter Desktop app for API image generator ----------------------

# ------------Downloading Image and Storing it from API ----------------------
# for i, image in enumerate(images, 1):
#     response = requests.get(image)
#
#     if response.status_code == 200:
#         # Specify the folder where you want to save the image
#         folder_path = 'D:/Python/images'
#
#         # Extract the file name from the URL
#
#         # Create the full path to the file
#         full_path = os.path.join(folder_path, f"{params['query']}{i}.jpg")
#
#         # Save the image to the specified folder
#         with open(full_path, 'wb') as f:
#             f.write(response.content)
#
#         # print(f"Image downloaded successfully as {full_path}{i}")
#         # print(image)
#     else:
#         print(f"Error: {response.status_code}")

# ------------Downloading Image and Storing it from API ----------------------
# async def fetch(urls, params):
#     async with httpx.AsyncClient() as client:
#         response = await client.get(urls, params= params)
#         return response.json()['results']
#
# async def generate_image():
#     global image_num
#
#     url = "https://api.unsplash.com/search/photos?"
#
#     params = {
#         "page": 10,
#         "query": "cars",
#         "client_id": "w_Vw6L10napk9Ftv3en4_RbUyLWFJflc2oq1VPJgixo"
#     }
#
#     responses = await fetch(url, params)
#     images = []
#     links = []
#     for response in responses:
#         images.append(response['urls']['small'])
#         links.append(response['links']['html'])
#
#     print(len(images), images)
#     print(len(links), links)
#
urls = ['https://unsplash.com/photos/white-and-red-plastic-bottle-cap-lot-LT3-9wxB9wo', 'https://unsplash.com/photos/selective-color-photography-of-brown-bottle-IsAbRXSCsEY', 'https://unsplash.com/photos/black-and-gold-spray-bottle-OE9cEaxxdPU', 'https://unsplash.com/photos/seven-small-bottle-in-a-grey-surface-close-up-photography-PvcNeT0-O88', 'https://unsplash.com/photos/black-and-red-plastic-bottle-on-white-textile-hMHwKbYWQEs', 'https://unsplash.com/photos/silver-and-gold-round-coins-on-white-printer-paper-OPUnhl2GDCo', 'https://unsplash.com/photos/green-plant-on-brown-clay-pot-e1KYRCR8SI8', 'https://unsplash.com/photos/flat-lay-photography-of-spices-on-plate-i0IvwAhhGZM', 'https://unsplash.com/photos/brown-glass-bottle-5ffYKP0-6wE', 'https://unsplash.com/photos/four-white-labeled-bottle-close-up-photography-ePPcMfzYQ-Y', 'https://unsplash.com/photos/white-and-black-labeled-bottle-GT7JHAp2lug', 'https://unsplash.com/photos/brass-and-silver-trophy-on-brown-wooden-table-QL5U3CzxzlY', 'https://unsplash.com/photos/woman-in-black-long-sleeve-shirt-holding-bottle-of-beer-Iq81PDqQyAU', 'https://unsplash.com/photos/white-and-black-floral-textile-aDDV33MI_ow', 'https://unsplash.com/photos/white-and-black-glass-bottle-eBW4v2dC-ts', 'https://unsplash.com/photos/a-painting-of-two-girls-and-a-dog-in-a-forest-5F3u0j6s6pM', 'https://unsplash.com/photos/red-and-blue-flowers-painting-LpCq6mjbMPo', 'https://unsplash.com/photos/person-holding-white-and-black-labeled-bottle-ErNCyAsDgfg', 'https://unsplash.com/photos/brown-glass-bottle-beside-box-WnVrO-DvxcE', 'https://unsplash.com/photos/dish-with-tomato-salad-toppings-rPkgYDh2bmo']

async def fetch(urls):
    async with httpx.AsyncClient() as client:
        request = [client.get(url) for url in urls]
        final = await asyncio.gather(*request)

    print(final)




asyncio.run(fetch(urls))