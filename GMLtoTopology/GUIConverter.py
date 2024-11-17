import tkinter as tk
from tkinter import filedialog, messagebox
import os
import random
import os.path as op
from GMLtoTopology import GMLtoTopology
from tkinter import font as tkFont
import json

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'


DICT_LINKS_CONF = {}

def save_link_config():
    with open('LinkConfig.json', 'w') as lkc: 
        json.dump(DICT_LINKS_CONF, lkc, indent=4)

def load_link_config():
    with open('LinkConfig.json', 'r') as lkc:
        return json.load(lkc)

def convert_specific():
    name = os.path.basename(filedialog.askopenfilename(initialdir=PATH_DATASET, title="Select GML file",
                                      filetypes=(("GML files", "*.gml"), ("all files", "*.*"))))
    if name:
        converter.convert_gml_topo(name, PATH_DATASET, PATH_TOPOLOGIES, flagLink.get(), DICT_LINKS_CONF)
        messagebox.showinfo("Success", f"Converted: {name}")

def convert_random():
    random.seed()
    try:
        randFile = random.choice(os.listdir(PATH_DATASET))
        converter.convert_gml_topo(randFile, PATH_DATASET, PATH_TOPOLOGIES, flagLink.get(), DICT_LINKS_CONF)
        messagebox.showinfo("Success", f"Randomly converted: {randFile}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def convert_all():
    for file in os.listdir(PATH_DATASET):
        try:
            converter.convert_gml_topo(file, PATH_DATASET, PATH_TOPOLOGIES, flagLink.get(), DICT_LINKS_CONF)
        except:
            print(f"Error converting {file}")
    messagebox.showinfo("Success", "Converted all GML files in dataset.")

def clear_topologies():
    for file in os.listdir(PATH_TOPOLOGIES):
        os.remove(op.join(PATH_TOPOLOGIES, file))
    messagebox.showinfo("Success", "All topology files cleared.")

def quit_app():
    root.quit()

def show_frame(frame):
    print_link_conf()
    frame.tkraise()

def delete_config(n):
    del DICT_LINKS_CONF[n]
    i=0
    for key in DICT_LINKS_CONF.keys():
        if i != int(key) and i<int(key):
            DICT_LINKS_CONF[str(i)]=DICT_LINKS_CONF[str(key)]
            del DICT_LINKS_CONF[str(key)]
        i=i+1
        
    save_link_config()
    print_link_conf()

def apply_config():

    bw = entry_bw.get().strip()
    delay = entry_delay.get().strip()
    jitter = entry_jitter.get().strip()
    loss = entry_loss.get().strip()
    speedup = entry_speedup.get().strip()
    latency = entry_latency.get().strip()
    max_queue = entry_max_queue.get().strip()

    try:
        bw = float(bw) if bw else None
        delay = float(delay) if delay else 0
        jitter = float(jitter) if jitter else 0
        loss = float(loss) if loss else None
        speedup = float(speedup) if speedup else 0
        latency = float(latency) if latency else None
        max_queue = int(max_queue) if max_queue else None

        if bw is not None and bw <= 0:
            raise ValueError("Bandwidth must be greater than 0.")
        if delay is not None and delay < 0:
            raise ValueError("Delay cannot be negative.")
        if jitter is not None and jitter < 0:
            raise ValueError("Jitter cannot be negative.")
        if loss is not None and not (0 <= loss <= 100):
            raise ValueError("Loss must be between 0 and 100.")
        if speedup is not None and speedup < 0:
            raise ValueError("Speedup cannot be negative.")
        if latency is not None and latency < 0:
            raise ValueError("Latency cannot be negative.")
        if max_queue is not None and max_queue <= 0:
            raise ValueError("Max Queue Size must be greater than 0.")

        config_values = {
            'bw': bw,
            'delay': str(int(delay)) + "ms",
            'jitter':str(int(jitter)) + "ms",
            'loss': loss,
            'gro': var_gro.get(),
            'txo': var_txo.get(),
            'rxo': var_rxo.get(),
            'speedup': speedup,
            'use_hfsc': var_use_hfsc.get(),
            'use_tbf': var_use_tbf.get(),
            'latency_ms': latency,
            'enable_ecn': var_enable_ecn.get(),
            'enable_red': var_enable_red.get(),
            'max_queue_size': max_queue,
        }
        DICT_LINKS_CONF[len(DICT_LINKS_CONF)] = config_values
        save_link_config()

        messagebox.showinfo("Success", "Configuration applied successfully!")

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def print_link_conf():
    global DICT_LINKS_CONF
    DICT_LINKS_CONF = load_link_config()
    update_dropdown()
    text_area.delete('1.0', tk.END)
    for link_id in DICT_LINKS_CONF:
        link_info = str(DICT_LINKS_CONF[link_id])
        text_area.insert(tk.END, link_info)
        text_area.insert(tk.END, "\n\n")

def update_dropdown():
    menu = dropdown["menu"]
    menu.delete(0, "end")
    
    if DICT_LINKS_CONF:
        for key in DICT_LINKS_CONF.keys():
            menu.add_command(label=key, command=tk._setit(var, key))
        var.set(list(DICT_LINKS_CONF.keys())[0]) 
        btn_del.config(state="normal")  
    else:
        var.set("")  
        btn_del.config(state="disabled") 

if __name__ == "__main__":
    converter = GMLtoTopology()

    root = tk.Tk()
    root.title("GML to Topology Converter")
    root.geometry("327x480")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")  

    font_title = tkFont.Font(family="Helvetica", size=18, weight="bold")
    font_button = tkFont.Font(family="Helvetica", size=12)

    container = tk.Frame(root)
    container.pack(fill="both", expand=True)

    page1 = tk.Frame(container, bg="#f7f7f7")
    page2 = tk.Frame(container, bg="#f7f7f7")
    page3 = tk.Frame(container, bg="#f7f7f7")

    for frame in (page1, page2, page3):
        frame.grid(row=0, column=0, sticky="nsew")

    # ===== Page 1 =====
    label_title = tk.Label(page1, text="GML to Topology Converter", font=font_title, fg="#333333", bg="#f7f7f7")
    label_title.pack(pady=20)

    frame_buttons = tk.Frame(page1, bg="#ffffff", padx=20, pady=20, relief=tk.RIDGE, bd=2)
    frame_buttons.pack(pady=10, fill="both", expand=True)

    btn_specific = tk.Button(frame_buttons, text="Convert Specific GML", font=font_button, bg="#4CAF50", fg="black", padx=10, pady=5, command = convert_specific)
    btn_specific.pack(pady=10, fill="x")

    btn_random = tk.Button(frame_buttons, text="Convert Random GML", font=font_button, bg="#03A9F4", fg="black", padx=10, pady=5, command = convert_random)
    btn_random.pack(pady=10, fill="x")

    btn_all = tk.Button(frame_buttons, text="Convert All GML Files", font=font_button, bg="#FF9800", fg="black", padx=10, pady=5, command = convert_all)
    btn_all.pack(pady=10, fill="x")

    btn_clear = tk.Button(frame_buttons, text="Clear Topologies", font=font_button, bg="#F44336", fg="black", padx=10, pady=5, command = clear_topologies)
    btn_clear.pack(pady=10, fill="x")

    flagLink = tk.BooleanVar()  
    checkbox = tk.Checkbutton(frame_buttons, text="Add Link Capacity", variable=flagLink, font=font_button, bg="#ffffff")
    checkbox.pack(pady=10)

    btn_next_page = tk.Button(page1, text="Go to Settings", command=lambda: show_frame(page2), font=font_button, bg="#9E9E9E", fg="black", padx=10, pady=5)
    btn_next_page.pack(pady=10)

    # ===== Page 2 =====
    label_settings = tk.Label(page2, text="Link Configurations", font=font_title, fg="#333333", bg="#f7f7f7")
    label_settings.pack(pady=20)

    text_area = tk.Text(page2, width=40, height=15, font=font_button, wrap=tk.WORD)
    text_area.pack(pady=5)

    btn_next_page = tk.Button(page2, text="Add Link Config", command=lambda: show_frame(page3), font=font_button, bg="#4CAF50", fg="black", padx=10, pady=5)
    btn_next_page.pack(pady=5)

    frame_dropdown_delete = tk.Frame(page2, bg = "white")
    frame_dropdown_delete.pack(pady=5)

    var = tk.StringVar(root)


    dropdown = tk.OptionMenu(frame_dropdown_delete, var, "")
    dropdown.pack(side=tk.RIGHT, padx=(0, 10))  

   
    btn_del = tk.Button(frame_dropdown_delete, text="Del Link Config", command=lambda: delete_config(var.get()), font=("Arial", 12), bg="#F44336", fg="black", padx=10, pady=5)
    btn_del.pack(side=tk.LEFT)  
    btn_del.config(state="disabled") 

    btn_back = tk.Button(page2, text="Back to Converter", command=lambda: show_frame(page1), font=font_button, bg="#9E9E9E", fg="black", padx=10, pady=5)
    btn_back.pack(pady=5)

    # ===== Page 3 =====
    label_config = tk.Label(page3, text="Configure Link Parameters", font=font_title, fg="#333333", bg="#f7f7f7")
    label_config.grid(row=0, column=0, columnspan=2, pady=20)

    tk.Label(page3, text="Bandwidth (Mbps):", bg="#f7f7f7").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_bw = tk.Entry(page3)
    entry_bw.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(page3, text="Delay (ms):", bg="#f7f7f7").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_delay = tk.Entry(page3)
    entry_delay.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(page3, text="Jitter (ms):", bg="#f7f7f7").grid(row=3, column=0, padx=5, pady=5, sticky="e")
    entry_jitter = tk.Entry(page3)
    entry_jitter.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(page3, text="Loss (%):", bg="#f7f7f7").grid(row=4, column=0, padx=5, pady=5, sticky="e")
    entry_loss = tk.Entry(page3)
    entry_loss.grid(row=4, column=1, padx=5, pady=5)

    var_gro = tk.BooleanVar()
    tk.Checkbutton(page3, text="Enable GRO", variable=var_gro, bg="#f7f7f7").grid(row=5, column=0, padx=5, pady=5, sticky="e")

    var_txo = tk.BooleanVar(value=True)
    tk.Checkbutton(page3, text="Enable TXO", variable=var_txo, bg="#f7f7f7").grid(row=5, column=1, padx=5, pady=5, sticky="w")

    var_rxo = tk.BooleanVar(value=True)
    tk.Checkbutton(page3, text="Enable RXO", variable=var_rxo, bg="#f7f7f7").grid(row=6, column=0, padx=5, pady=5, sticky="e")

    tk.Label(page3, text="Speedup:", bg="#f7f7f7").grid(row=7, column=0, padx=5, pady=5, sticky="e")
    entry_speedup = tk.Entry(page3)
    entry_speedup.grid(row=7, column=1, padx=5, pady=5)

    var_use_hfsc = tk.BooleanVar()
    tk.Checkbutton(page3, text="Use HFSC", variable=var_use_hfsc, bg="#f7f7f7").grid(row=8, column=0, padx=5, pady=5, sticky="e")

    var_use_tbf = tk.BooleanVar()
    tk.Checkbutton(page3, text="Use TBF", variable=var_use_tbf, bg="#f7f7f7").grid(row=8, column=1, padx=5, pady=5, sticky="w")

    tk.Label(page3, text="Latency (ms):", bg="#f7f7f7").grid(row=9, column=0, padx=5, pady=5, sticky="e")
    entry_latency = tk.Entry(page3)
    entry_latency.grid(row=9, column=1, padx=5, pady=5)

    var_enable_ecn = tk.BooleanVar()
    tk.Checkbutton(page3, text="Enable ECN", variable=var_enable_ecn, bg="#f7f7f7").grid(row=10, column=0, padx=5, pady=5, sticky="e")

    var_enable_red = tk.BooleanVar()
    tk.Checkbutton(page3, text="Enable RED", variable=var_enable_red, bg="#f7f7f7").grid(row=10, column=1, padx=5, pady=5, sticky="w")

    tk.Label(page3, text="Max Queue Size:", bg="#f7f7f7").grid(row=11, column=0, padx=5, pady=5, sticky="e")
    entry_max_queue = tk.Entry(page3)
    entry_max_queue.grid(row=11, column=1, padx=5, pady=5)

    btn_apply = tk.Button(page3, text="Apply Configuration", command=apply_config, font=font_button, bg="#4CAF50", fg="black", padx=10, pady=5)
    btn_apply.grid(row=13, column=0, columnspan=2, pady=5)

    btn_back_to_settings = tk.Button(page3, text="Back to Settings", command=lambda: show_frame(page2), font=font_button, bg="#9E9E9E", fg="black", padx=10, pady=5)
    btn_back_to_settings.grid(row=14, column=0, columnspan=2, pady=10)

    show_frame(page1)

    root.mainloop()
