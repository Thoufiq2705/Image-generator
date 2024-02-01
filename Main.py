import asyncio
import io
import webbrowser
from bs4 import BeautifulSoup
import tracemalloc
import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk
import requests
import httpx
import json

tracemalloc.start()
## global variables

page = 10
image_num = 0
links_num = 0
i = 1

images = []
links = []
download_links = []

update = False
current_image_id = None

## global variables

## ------------API Request and Getting Data from API ----------------------

async def fetch_single(url, client):
        links_responses = await client.get(url)
        html_text = links_responses.text
        soup = BeautifulSoup(html_text, 'html.parser')
        classist = soup.find('a',
                                class_="slPFO DQBsa p1cWU jpBZ0 EzsBC KHq0c IKU9M zhYdL I0aPD dEcXu yn5eT jpBZ0 V6yz9 lT8_y")
        final_links = classist.get('href')
        return final_links
async def fetch(urls):
    global download_links
    async with httpx.AsyncClient() as client:
        tasks = [fetch_single(url, client) for url in urls ]
        download_links = await asyncio.gather(*tasks)
def generate_image():
    global image_num
    global page
    global update

    url = "https://api.unsplash.com/search/photos?"
    params = {
        "page": page,
        "query": input_search.get('0.0', tk.END),
        "client_id": "w_Vw6L10napk9Ftv3en4_RbUyLWFJflc2oq1VPJgixo"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_data = response.json()
        final_response = json.dumps(json_data, indent=2)
        final = json.loads(final_response)
        final_result = final['results']
    else:
        print(f"Error: {response.status_code}")


    for results in final_result:
        global i
        images.append(results['urls']['small'])
        links.append(results['links']['html'])
        i += 1
    # print(links)

    # ------------API Request and Getting Data from API ----------------------

    # # ------------Web Scraping ----------------------

    download_links.clear()
    # print(len(links))
    asyncio.run(fetch(links))


    # for link in links:
    #     html_text = requests.get(link).text
    #     soup = BeautifulSoup(html_text, 'html.parser')
    #     classist = soup.find('a',
    #                          class_="slPFO DQBsa p1cWU jpBZ0 EzsBC KHq0c IKU9M zhYdL I0aPD dEcXu yn5eT jpBZ0 V6yz9 lT8_y")
    #     final_links = classist.get('href')
    #     download_links.append(final_links)

    #
    # # # ------------Web Scraping ----------------------
    Image_response = requests.get(images[image_num])

    images_photo = Image.open(io.BytesIO(Image_response.content))
    photo_image = ImageTk.PhotoImage(images_photo)
    canvas.create_image(300, 300, anchor="center", image=photo_image)

    canvas.update()
    update_buttons_state(generate_nxt)
    showmore_btn.grid_remove()

# ------------Tkinter Desktop app for API image generator ----------------------

# ------Tkinter Functions-------------
def update_buttons_state(btn):
    if image_num == len(images) - 1:
        btn.configure(state="disabled")
        showmore_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky='news')
        canvas.update()
    else:
        btn.configure(state="normal")
def next_function():
    global image_num
    global images
    global current_image_id

    if current_image_id is not None:
        canvas.delete(current_image_id)

    if image_num < len(images) - 1:
        image_num += 1
        Image_response = requests.get(images[image_num])
        images_photo = Image.open(io.BytesIO(Image_response.content))
        photo_image = ImageTk.PhotoImage(images_photo)
        canvas.create_image(300, 300, anchor="center", image=photo_image)
        canvas.photo = photo_image

        update_buttons_state(generate_nxt)
        update_buttons_state2(generate_prev)
def previous_function():
    global image_num
    global images
    global current_image_id
    showmore_btn.grid_remove()

    if current_image_id is not None:
        canvas.delete(current_image_id)

    if image_num > 0:
        image_num -= 1
        Image_response = requests.get(images[image_num])
        images_photo = Image.open(io.BytesIO(Image_response.content))
        photo_image = ImageTk.PhotoImage(images_photo)
        canvas.create_image(300, 300, anchor="center", image=photo_image)
        canvas.photo = photo_image

        update_buttons_state(generate_nxt)
        update_buttons_state2(generate_prev)

def download_image():
    global image_num
    global download_links

    download_link = download_links[image_num]
    webbrowser.open_new(download_link)

def showmore():
    global page

    showmore_btn.grid_remove()
    # page += 10
    generate_image()
def update_buttons_state2(btn):
    if image_num <= 0:
        btn.configure(state="disabled")
    else:
        btn.configure(state="normal")

# ------Tkinter Functions-------------

root = ctk.CTk()
root._set_appearance_mode('dark')
root.title('Image Generator')

input_frame = ctk.CTkFrame(root)
input_frame.pack(side="left", expand='True', padx=10, pady=10)

input_Image = ctk.CTkLabel(input_frame, text='Create', placeholder="hi")
input_Image.grid(row=0, column=0, padx=10, pady=10)

input_search = ctk.CTkTextbox(input_frame, height=10)
input_search.grid(row=0, column=1, padx=10, pady=10)

generate_btn = ctk.CTkButton(input_frame, text="Generate Image", command=generate_image)
generate_btn.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky='news')

generate_prev = ctk.CTkButton(input_frame, text=' < ', width=60, command=previous_function)
generate_prev.grid(row=2, column=0, padx=10, pady=10, sticky='news')

generate_nxt = ctk.CTkButton(input_frame, text=" > ", width=2, command=next_function)
generate_nxt.grid(row=2, column=1, padx=(150, 10), pady=10, sticky='news')

download_btn = ctk.CTkButton(input_frame, text="Download Image", command=download_image)
download_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='news')

showmore_btn = ctk.CTkButton(input_frame, text="Show More", command=showmore)
showmore_btn.grid_remove()

canvas = tk.Canvas(root, width=600, height=600, yscrollcommand='True')
canvas.pack(side='left')


root.mainloop()

# ------------Tkinter Desktop app for API image generator ----------------------
