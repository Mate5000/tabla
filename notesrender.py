import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import Listbox, Scrollbar, SINGLE
import os

def hex_to_rgb(hex_color):
    hex_color = hex_color.strip('#')
    return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4))


fig, ax = plt.subplots(figsize=(16, 9)) 
ax.set_facecolor('black')  
fig.patch.set_facecolor('black') 
ax.set_aspect('equal')
ax.invert_yaxis() 
ax.axis('off')     
plt.tight_layout(pad=0)  

# workpath
xml_path = "c:\\a"  
xml_files = [os.path.join(xml_path, file) for file in os.listdir(xml_path) if file.endswith(".xml")]


current_file = xml_files[0] if xml_files else None

def loadkinaitablacucc():
    if current_file is None:
        return
    
    tree = ET.parse(current_file)
    root = tree.getroot()
    
    for package in root.findall('.//Package'):
        data = package.find('Data')
        if data is not None:
            points_str = data.find('Points').text
            color_hex = data.find('ForegroundColor').text
            thickness = float(data.find('Thickness').text) / 2  #stroke size fix
            linestyle = data.find('LineStyle').text if data.find('LineStyle') is not None else 'solid'
            
            
            color_rgb = hex_to_rgb(color_hex)
            

            if sum(color_rgb) < 1.5:  
                color_rgb = (1, 1, 1) 
            
    
            points = []
            for point_str in points_str.strip().split(';'):
                if point_str:
                    coords = point_str.split(',')
                    if len(coords) >= 2:
                        x, y = float(coords[0]), float(coords[1])
                        points.append((x, y))
            
            if points:
                x_vals, y_vals = zip(*points)
                ax.plot(x_vals, y_vals, color=color_rgb, linewidth=thickness, linestyle='--' if linestyle == 'dashed' else '-')
                # nem megy még így se a szaggatott vonal rendere
def update(frame):
    ax.clear()
    ax.set_facecolor('black')  
    ax.set_aspect('equal')
    ax.invert_yaxis()  
    ax.axis('off')     
    loadkinaitablacucc()

def on_file_select(event):
    global current_file
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        current_file = event.widget.get(index)
        update(None)

root = tk.Tk()
root.title("xml valaszto")
root.geometry("220x150")

# ez csak win alatt megy!!!!!!!!!!!
root.attributes('-toolwindow', True)

listbox = Listbox(root, selectmode=SINGLE)
scrollbar = Scrollbar(root)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
for file in xml_files:
    listbox.insert(tk.END, file)


listbox.bind('<<ListboxSelect>>', on_file_select)


ani = FuncAnimation(fig, update, interval=1000)



plt.show()
root.mainloop()