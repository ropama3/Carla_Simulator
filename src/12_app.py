# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:12:34 2024

@author: MPALOMO
"""
import tkinter as tk
from tkinter import ttk
import webbrowser

selected_color = '255,0,255'
selected_weather = [0, 0, 50, 0, 0, 0]
selected_algorithm = None
selected_model = 'vehicle.tesla.model3'

def on_algorithm_selected():
    global selected_algorithm
    selected_algorithm = alignment_var.get()

def select_color(color):
    global selected_color
    color_button.config(text=color)
    color_canvas.configure(background=color)
    if color in ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]:
        selected_color = color_name_to_rgb(color)

def color_name_to_rgb(color_name):
    colors = {
        "Red": '255, 0, 0',
        "Green": '0, 255, 0',
        "Blue": '0, 0, 255',
        "Yellow": '255, 255, 0',
        "Orange": '255, 165, 0',
        "Purple": '128, 0, 128'
    }
    return colors.get(color_name, '255,0,255')

def select_weather(value):
    global selected_weather
    selected_weather = [slider1.get(), slider2.get(), slider3.get(), slider4.get(), slider5.get(), slider6.get()]

def model():
    global selected_model
    model = alignment_var_model.get()
    if model in ['Tesla', 'Mini', 'Audi', 'Dodge']:
        selected_model = carla_models(model)

def carla_models(model):
    models = {
        "Tesla": 'vehicle.tesla.model3',
        "Mini": 'vehicle.mini.cooper_s',
        "Audi": 'vehicle.audi.etron',
        "Dodge": 'vehicle.dodge.charger_2020'
    }
    return models.get(model, 'vehicle.tesla.model3')

def open_link(event):
    webbrowser.open("https://github.com/ropama3/Carla_Simulator")

# GUI Configuration
root = tk.Tk()
root.title('Window for Carla Simulator App')
root.geometry('500x600+50+50')
root.iconbitmap('Images/carla.ico')
root.configure(bg='#cfe2ff')

# Style Configuration
style = ttk.Style()
style.configure('TLabel', font=('Century Gothic', 10), foreground='#1f1f1f', background='#cfe2ff')
style.configure('TRadiobutton', font=('Century Gothic', 10), foreground='#1f1f1f', background='#cfe2ff')
style.configure('TNotebook', tabposition='wn', tabmargins=(2, 2, 0, 0), background='#cfe2ff')
style.map('TNotebook.Tab', background=[('selected', 'red')], foreground=[('selected', '#1f1f1f')])

# Creating a notebook
notebook = ttk.Notebook(root, style='TNotebook')  # Estilo del Notebook
notebook.pack(pady=10, expand=True)

# Creating a tab "General Information"
general_info_tab = ttk.Frame(notebook, style="TLabel", width=400, height=280)
notebook.add(general_info_tab, text="Abstract")

# Creating a text box in the "General Information" tab
info_text = tk.Text(general_info_tab, wrap="word", width=70, height=20, font=('Century Gothic', 9), foreground='#1f1f1f', background='#cfe2ff')
info_text.insert("1.0", "This is an application where we can specify the preferences of our simulator in Carla Simulator. This application connects with scripts that provide autonomy to the car, allowing us to modify certain aspects.\nInstructions: Select each of the aspects and then close the tab.\n\nFor more information about the complete Final Degree Project (TFG), as this is only a part of it, please visit ")
info_text.tag_configure("link", foreground="blue")
info_text.tag_bind("link", "<Button-1>", open_link)

# Adding the link
info_text.insert("end", "www.github.com", "link")
info_text.config(state="disabled")
info_text.grid(column=0, row=0, padx=20, pady=20)

# Setting up the expansion of the "General Information" tab
general_info_tab.columnconfigure(0, weight=1)
general_info_tab.rowconfigure(0, weight=1)

# Creating a tab "Profile"
profile_tab = ttk.Frame(notebook, style="TLabel", width=400, height=500)
notebook.add(profile_tab, text="Options")

# Creating a Canvas to display the selected color
color_canvas = tk.Canvas(profile_tab, width=20, height=20, background="white", bd=1, relief="solid")
color_canvas.place(x=150, y=50)

# Creating a Label for the color with a space before
color_title_label = ttk.Label(profile_tab, text="➢ Choose car color", style='TLabel')
color_title_label.place(x=10, y=20)

# Creating a Menubutton to select the color in the "Profile" tab
color_button = ttk.Menubutton(profile_tab, text="color", direction="below", style='TButton')
color_button.place(x=30, y=50)
color_menu = tk.Menu(color_button, tearoff=False)
color_button["menu"] = color_menu

# Adding color options to the menu
colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: select_color(c))

# Creating a Label for the title "Weather" with a space before
weather_title_label = ttk.Label(profile_tab, text="➢ Choose weather", style='TLabel')
weather_title_label.place(x=10, y=100)

# Creating sliders to select the weather in the "Profile" tab
slider1_label = ttk.Label(profile_tab, text='Cloudiness:', font=('Century Gothic', 8), style='TLabel')
slider1_label.place(x=30, y=130)
slider1 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider1.place(x=180, y=130)

slider2_label = ttk.Label(profile_tab, text='Precipitation:', font=('Century Gothic', 8), style='TLabel')
slider2_label.place(x=30, y=160)
slider2 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider2.place(x=180, y=160)

slider3_label = ttk.Label(profile_tab, text='Sun altitude:', font=('Century Gothic', 8), style='TLabel')
slider3_label.place(x=30, y=190)
slider3 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider3.place(x=180, y=190)

slider4_label = ttk.Label(profile_tab, text='Precipitation deposits:', font=('Century Gothic', 8), style='TLabel')
slider4_label.place(x=30, y=220)
slider4 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider4.place(x=180, y=220)

slider5_label = ttk.Label(profile_tab, text='Fog density:', font=('Century Gothic', 8), style='TLabel')
slider5_label.place(x=30, y=250)
slider5 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider5.place(x=180, y=250)

slider6_label = ttk.Label(profile_tab, text='Wetness:', font=('Century Gothic', 8), style='TLabel')
slider6_label.place(x=30, y=280)
slider6 = ttk.Scale(profile_tab, from_=0, to=100, orient=tk.HORIZONTAL, command=lambda value: select_weather(value))
slider6.place(x=180, y=280)

# Other elements of the "Profile" tab

lf_text = "➢ Choose Algorithm"  
lf = ttk.Label(profile_tab, text=lf_text, style='TLabel')
lf.place(x=10, y=350)

# Creating a Frame inside the LabelFrame
lf_frame = ttk.Frame(profile_tab)
lf_frame.place(x=30, y=373)

alignment_var = tk.StringVar()
alignments = ('Algorithm 1', 'Algorithm 2')

# Creating radio buttons and placing them in the Frame inside the LabelFrame
grid_column = 0
for alignment in alignments:
    radio = ttk.Radiobutton(lf_frame, text=alignment, value=alignment, variable=alignment_var, command=on_algorithm_selected, style='TRadiobutton')
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

lf_text = "➢ Choose car model"  
lf = ttk.Label(profile_tab, text=lf_text, style='TLabel')
lf.place(x=10, y=420)

# Creating a Frame inside the LabelFrame
lf_frame = ttk.Frame(profile_tab)
lf_frame.place(x=30, y=443)

alignment_var_model = tk.StringVar()
alignments_model = ('Tesla', 'Mini', 'Audi', 'Dodge')

# Creating radio buttons and placing them in the Frame inside the LabelFrame
grid_column = 0
for alignment in alignments_model:
    radio = ttk.Radiobutton(lf_frame, text=alignment, value=alignment, variable=alignment_var_model, command=model, style='TRadiobutton')
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

# Setting up the expansion of the "Profile" tab
profile_tab.columnconfigure(0, weight=1)
profile_tab.columnconfigure(1, weight=0)  # Preventing the column with the Canvas from expanding
profile_tab.rowconfigure(0, weight=1)

# Starting the main loop
root.mainloop()

print("Selected color",selected_color)
print("Selected weather",selected_weather)
print("Selected algorithm",selected_algorithm)
print("Selected model",selected_model)
