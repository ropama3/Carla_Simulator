# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:55:27 2024

@author: MPALOMO
"""
import carla 
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
import time
import random
import math
import glob
import os
import sys
import argparse
import keyboard as kb
import re
import tkinter as tk
from tkinter import ttk
import webbrowser


# APP
selected_color = '255,0,255'
selected_weather = [0, 0, 50, 0, 0, 0]
selected_model = 'vehicle.tesla.model3'

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

root = tk.Tk()
root.title('Window for Carla Simulator App')
root.geometry('500x500+50+50')
root.iconbitmap('Images/carla.ico')
root.configure(bg='#cfe2ff')

style = ttk.Style()
style.configure('TLabel', font=('Century Gothic', 10), foreground='#1f1f1f', background='#cfe2ff')
style.configure('TRadiobutton', font=('Century Gothic', 10), foreground='#1f1f1f', background='#cfe2ff')
style.configure('TNotebook', tabposition='wn', tabmargins=(2, 2, 0, 0), background='#cfe2ff')
style.map('TNotebook.Tab', background=[('selected', 'red')], foreground=[('selected', '#1f1f1f')])

notebook = ttk.Notebook(root, style='TNotebook')
notebook.pack(pady=10, expand=True)

general_info_tab = ttk.Frame(notebook, style="TLabel", width=400, height=280)
notebook.add(general_info_tab, text="Abstract")

info_text = tk.Text(general_info_tab, wrap="word", width=70, height=20, font=('Century Gothic', 9), foreground='#1f1f1f', background='#cfe2ff')
info_text.insert("1.0", "This is an application where we can specify the preferences of our simulator in Carla Simulator. This application connects with scripts that provide autonomy to the car, allowing us to modify certain aspects.\nInstructions: Select each of the aspects and then close the tab.\n\nFor more information about the complete Final Degree Project (TFG), as this is only a part of it, please visit ")
info_text.tag_configure("link", foreground="blue")
info_text.tag_bind("link", "<Button-1>", open_link)

info_text.insert("end", "www.github.com", "link")
info_text.config(state="disabled")
info_text.grid(column=0, row=0, padx=20, pady=20)

general_info_tab.columnconfigure(0, weight=1)
general_info_tab.rowconfigure(0, weight=1)

profile_tab = ttk.Frame(notebook, style="TLabel", width=400, height=500)
notebook.add(profile_tab, text="Options")

color_canvas = tk.Canvas(profile_tab, width=20, height=20, background="white", bd=1, relief="solid")
color_canvas.place(x=150, y=50)

color_title_label = ttk.Label(profile_tab, text="➢ Choose car color", style='TLabel')
color_title_label.place(x=10, y=20)

color_button = ttk.Menubutton(profile_tab, text="color", direction="below", style='TButton')
color_button.place(x=30, y=50)
color_menu = tk.Menu(color_button, tearoff=False)
color_button["menu"] = color_menu

colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple"]
for color in colors:
    color_menu.add_command(label=color, command=lambda c=color: select_color(c))

weather_title_label = ttk.Label(profile_tab, text="➢ Choose weather", style='TLabel')
weather_title_label.place(x=10, y=100)

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


lf_text = "➢ Choose car model"  
lf = ttk.Label(profile_tab, text=lf_text, style='TLabel')
lf.place(x=10, y=320)

lf_frame = ttk.Frame(profile_tab)
lf_frame.place(x=30, y=343)

alignment_var_model = tk.StringVar()
alignments_model = ('Tesla', 'Mini', 'Audi', 'Dodge')

grid_column = 0
for alignment in alignments_model:
    radio = ttk.Radiobutton(lf_frame, text=alignment, value=alignment, variable=alignment_var_model, command=model, style='TRadiobutton')
    radio.grid(column=grid_column, row=0, ipadx=10, ipady=10)
    grid_column += 1

profile_tab.columnconfigure(0, weight=1)
profile_tab.columnconfigure(1, weight=0)  
profile_tab.rowconfigure(0, weight=1)

root.mainloop()

#--------------------------------------------------------------------------------------------------------------
#Carla
#world
client = carla.Client('localhost', 2000)
client.set_timeout(2000)
client.load_world("Town05")
world = client.get_world()
map = world.get_map()

#loc=carla.Transform(carla.Location(x=106.557922, y=191.3, z=1.138501), carla.Rotation(pitch=0.533207, yaw=-186.194565, roll=0.006472))
loc=carla.Transform(carla.Location(x=-124.557922, y=-190.525208, z=10.138501), carla.Rotation(pitch=0.533207, yaw=-1.194565, roll=0.006472))
spectator = world.get_spectator()
spectator_pos = carla.Transform(loc.location + carla.Location(x=10,y=0,z=4),carla.Rotation(yaw=loc.rotation.yaw))
spectator.set_transform(spectator_pos)

#car
blueprint_library = world.get_blueprint_library()
bp = random.choice(blueprint_library.filter(selected_model))

if bp.has_attribute('color'):
    color = bp.get_attribute('color').recommended_values[2]
    bp.set_attribute('color', selected_color)

vehicle = world.spawn_actor(bp, loc)

#sensor
def camera_callback(image,data_dict):
    data_dict['image'] = np.reshape(np.copy(image.raw_data),(image.height,image.width,4))
CAMERA_POS_Z = 3
CAMERA_POS_X = -5
camera_bp=world.get_blueprint_library().find('sensor.camera.rgb')
camera_bp.set_attribute('image_size_x','640')
camera_bp.set_attribute('image_size_y','360')
camera_init_trans= carla.Transform(carla.Location(z=CAMERA_POS_Z,x=CAMERA_POS_X))
camera=world.spawn_actor(camera_bp,camera_init_trans,attach_to=vehicle)
image_w= camera_bp.get_attribute('image_size_x').as_int()
image_h= camera_bp.get_attribute('image_size_y').as_int()
camera_data = {'image':np.zeros((image_h,image_w,4))}
camera.listen(lambda image: camera_callback(image,camera_data))

#speed
def maintain_speed(s,preferred_speed,speed_threshold):
    if s >= preferred_speed:
        return 0
    elif s < preferred_speed - speed_threshold:
        return 0.8
    else:
        return 0.4
    
#angle
def angle_between(v1, v2):
    return math.degrees(np.arctan2(v1[1], v1[0]) - np.arctan2(v2[1], v2[0]))

def get_angle(car,wp):
    vehicle_pos = car.get_transform()
    car_x = vehicle_pos.location.x
    car_y = vehicle_pos.location.y
    wp_x = wp.transform.location.x
    wp_y = wp.transform.location.y
    
    x = (wp_x - car_x)/((wp_y - car_y)**2 + (wp_x - car_x)**2)**0.5
    y = (wp_y - car_y)/((wp_y - car_y)**2 + (wp_x - car_x)**2)**0.5
    
    car_vector = vehicle_pos.get_forward_vector()
    degrees = angle_between((x,y),(car_vector.x,car_vector.y))
    return degrees   

#steer
def steer(predicted_angle,MAX_STEER_DEGREES):
    if predicted_angle<-180:
        predicted_angle = predicted_angle+360
    elif predicted_angle > 180:
        predicted_angle = predicted_angle-360
    steer_input = predicted_angle
    if predicted_angle<-MAX_STEER_DEGREES:
        steer_input = -MAX_STEER_DEGREES
    elif predicted_angle>MAX_STEER_DEGREES:
        steer_input = MAX_STEER_DEGREES
    steer_input = steer_input/75
    return steer_input
    
#weather
def weather():
    weather = carla.WeatherParameters(
            cloudiness=selected_weather[0],
            precipitation=selected_weather[1],
            sun_altitude_angle=selected_weather[2],
            precipitation_deposits =selected_weather[3],
            fog_density =selected_weather[4],
            wetness = selected_weather[5])
    world.set_weather(weather)

    
#traffic light
def is_traffic_light_red(vehicle, world):
    location = vehicle.get_location()
    actor_list = world.get_actors()

    for actor in actor_list:
        if actor.type_id.startswith("traffic.traffic_light"):
            traffic_light_location = actor.get_location()
            distance = location.distance(traffic_light_location)
            traffic_light_state = actor.get_state()
            traffic_light_waypoint = world.get_map().get_waypoint(traffic_light_location) 
            if traffic_light_waypoint.road_id == 2353 and traffic_light_waypoint.lane_id == 1:
                if 30 < distance < 37.0:
                    if traffic_light_state == carla.TrafficLightState.Red:
                        return True
                    elif traffic_light_state == carla.TrafficLightState.Green:
                        return False
                    
            if traffic_light_waypoint.road_id == 2043 and traffic_light_waypoint.lane_id == 1:
                if 30 < distance < 37.0 and location.x<traffic_light_location.x:
                    if traffic_light_state == carla.TrafficLightState.Red:
                        return True
                    elif traffic_light_state == carla.TrafficLightState.Green:
                        return False    

#breake
def freno(light,brake_intensity,vehicle,estimated_throttle,steer_input):
    if light:
        control = carla.VehicleControl(brake=brake_intensity)
        vehicle.apply_control(control)
    else:    
        vehicle.apply_control(carla.VehicleControl(throttle= estimated_throttle, steer=steer_input))
        
#signs
def signs(vehicle, world):
    location = vehicle.get_location()
    actor_list = world.get_actors()

    for actor in actor_list:
        if actor.type_id.startswith("traffic.speed_limit"):
            traffic_sign_location = actor.get_location()
            distance = location.distance(traffic_sign_location)
            if distance < 20.0:
                # Obtiene el waypoint del vehículo y de la señal de tráfico
                vehicle_waypoint = world.get_map().get_waypoint(location)
                sign_waypoint = world.get_map().get_waypoint(traffic_sign_location)
                # Verifica si la señal de tráfico está en la misma carretera que el vehículo
                if sign_waypoint.lane_id == 4:
                    # Verifica si la señal de tráfico tiene información de velocidad límite
                    match = re.search(r'traffic\.speed_limit\.(\d+)', actor.type_id)
                    numero = match.group(1) 
                    speed_limit_kph = int(numero)
                    return speed_limit_kph
    return 0        

#driving
brake_intensity = 0.8
preferred_speed = 90
speed_threshold = 2
MAX_STEER_DEGREES = 20
cv2.namedWindow('RGB Camera', cv2.WINDOW_AUTOSIZE)
cv2.imshow('RGB Camera', camera_data['image'])
quit=False

while True:
    world.tick()
    if cv2.waitKey(1)==ord('q'): 
        quit=True
        break
    image = camera_data['image']
    
    weather()
        
    loc=vehicle.get_location()
    current_w = map.get_waypoint(loc)
    waypoint_separation = 5
    next_w0 = list(current_w.next(waypoint_separation))[0]
    next_w = map.get_waypoint(next_w0.transform.location,project_to_road=True, lane_type=(carla.LaneType.Driving))
    
    velocity = vehicle.get_velocity()
    speed = round(3.6 *math.sqrt(velocity.x**2+ velocity.y**2+velocity.z**2),0)
    image=cv2.putText(image,'Speed: '+str(int(speed))+' km/h', (30,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1,cv2.LINE_AA)
    estimated_throttle = maintain_speed(speed,preferred_speed,speed_threshold)
    predicted_angle = get_angle(vehicle,next_w)
    steer_input=steer(predicted_angle,MAX_STEER_DEGREES)
    sign=signs(vehicle, world)
    if sign!=0:
        preferred_speed=sign

    light=is_traffic_light_red(vehicle, world)
    if steer_input > 0.05:
        estimated_throttle=0.2
    freno(light,brake_intensity,vehicle,estimated_throttle,steer_input)
    cv2.imshow('RGB Camera', image)
cv2.destroyAllWindows()
camera.stop()

#destroy
for actor in world.get_actors().filter('*vehicle*'):
    actor.destroy()
for sensor in world.get_actors().filter('*sensor*'):
    sensor.destroy()

    