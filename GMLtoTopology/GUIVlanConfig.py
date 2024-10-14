import os
import os.path as op
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import json

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'

VlanConfig = {}
HostToSwitchConfig = {}

def save_vlan_config():
    with open('VlanConfig.json', 'w') as vlc:
        json.dump(VlanConfig, vlc, indent=4)

def load_vlan_config():
    if os.path.exists('VlanConfig.json'):
        with open('VlanConfig.json', 'r') as vlc:
            return json.load(vlc)
    else:
        return {}

def save_host_config():
    with open('HostConfig.json', 'w') as htc:
        json.dump(HostToSwitchConfig, htc, indent=4)

def load_host_config():
    if os.path.exists('HostConfig.json'):
        with open('HostConfig.json', 'r') as htc:
            return json.load(htc)
    else:
        return {}

def add_vlans(nameFile):
    try:
        VlanConfig = load_vlan_config()
        HostToSwitchConfig = load_host_config()

        with open(op.join(PATH_TOPOLOGIES, nameFile), "r") as filepy:
            contents = filepy.readlines()

        indexToWrite = 15 + int(contents[1].strip("#"))

        contents.insert(9, f"""class VLANHost( Host ):
    "Host connected to VLAN interface"

    # pylint: disable=arguments-differ
    def config( self, vlan=100, **params ):

        r = super( VLANHost, self ).config( **params )

        intf = self.defaultIntf()
        # remove IP from default, "physical" interface
        self.cmd( 'ifconfig %s inet 0' % intf )
        # create VLAN interface
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
        # assign the host's IP to the VLAN interface
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
        # update the intf name and host's intf map
        newName = '%s.%d' % ( intf, vlan )
        # update the (Mininet) interface to refer to VLAN interface name
        intf.name = newName
        # add VLAN interface to host's name to intf map
        self.nameToIntf[ newName ] = intf

        return r\n\n""")


        for host in HostToSwitchConfig:
            contents.insert(indexToWrite, f"        self.addLink({host}, {HostToSwitchConfig[host]}) \n")
        contents.insert(indexToWrite, f"\n        #adding host to switch links\n")

        for host in HostToSwitchConfig:
            if not host in VlanConfig:
                contents.insert(indexToWrite, f"        {host} = self.addHost('{host}') \n")

        for host in VlanConfig:
            contents.insert(indexToWrite, f"        {host} = self.addHost('{host}', cls=VLANHost, vlan={VlanConfig[host]['vlan']}, ip='{VlanConfig[host]['ip']}') \n")
        contents.insert(indexToWrite, f"\n        #adding hosts \n")

        with open(op.join(PATH_TOPOLOGIES, nameFile), "w") as f:
            f.write("".join(contents))

        messagebox.showinfo("Success", "VLANs added successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_file():
    file_path = filedialog.askopenfilename(initialdir=PATH_TOPOLOGIES, title="Select topology file",
                                           filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))
    if file_path:
        file_name = os.path.basename(file_path)
        add_vlans(file_name)

def show_frame(frame):
    update_text_area()
    frame.tkraise()

def apply_vlan_config(host, vlan, ip):
    try:
        Vconf = {
            "vlan": int(vlan),
            "ip": ip,
        }
        VlanConfig[host] = Vconf
        save_vlan_config()
        messagebox.showinfo("Success", f"VLAN configuration for host {host} saved successfully!")
        update_text_area()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def apply_host_config(host, switch):
    HostToSwitchConfig[host] = switch
    save_host_config()
    update_host_menu()
    messagebox.showinfo("Success", f"Host {host} connected to switch {switch} saved successfully!")
    update_text_area()

def update_host_menu():
    hosts = list(HostToSwitchConfig.keys())
    host_menu['values'] = hosts
    if hosts:
        host_var.set(hosts[0])
    else:
        host_var.set('')

def update_text_area():
    text_area.delete(1.0, tk.END)  
    if HostToSwitchConfig:
        for host, switch in HostToSwitchConfig.items():
            text_area.insert(tk.END, f"Host: {host} -> Switch: {switch}\n")
            if(host in VlanConfig):
                text_area.insert(tk.END, f"{host}: VLAN -> {VlanConfig[host]['vlan']}, ip -> {VlanConfig[host]['ip']}\n\n")
    else:
        text_area.insert(tk.END, "No host configurations available.\n")

def clear():
    VlanConfig.clear()
    HostToSwitchConfig.clear() 
    save_host_config()
    save_vlan_config()
    update_text_area()


if __name__ == "__main__":
    VlanConfig = load_vlan_config()
    HostToSwitchConfig = load_host_config()

    root = tk.Tk()
    root.title("VLAN Configurator")
    root.resizable(False, False)
    style = ttk.Style()
    style.theme_use('clam')

    frame1 = ttk.Frame(root)
    frame2 = ttk.Frame(root)
    frame3 = ttk.Frame(root)
    frame4 = ttk.Frame(root)

    for frame in (frame1, frame2, frame3, frame4):
        frame.grid(row=0, column=0, sticky='nsew')

    # ===== PAGE 1 =====
    lbl1 = ttk.Label(frame1, text="Click the button to select a topology file and add VLANs:")
    lbl1.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    btn1 = ttk.Button(frame1, text="Select File", command=select_file)
    btn1.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

    btn_to_frame3 = ttk.Button(frame1, text="Configure Hosts", command=lambda: show_frame(frame3))
    btn_to_frame3.grid(row=2, column=0, padx=20, pady=10)

    btn_to_frame2 = ttk.Button(frame1, text="Configure VLANs", command=lambda: show_frame(frame2))
    btn_to_frame2.grid(row=2, column=1, padx=20, pady=10)

    btn_to_frame4 = ttk.Button(frame1, text="View Host Config", command=lambda: show_frame(frame4))
    btn_to_frame4.grid(row=3, column=0, padx=20, pady=10)

    # ===== PAGE 2 =====
    lbl2 = ttk.Label(frame2, text="VLAN Configuration:")
    lbl2.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    host_var = tk.StringVar()
    hosts = list(HostToSwitchConfig.keys())
    if hosts:
        host_var.set(hosts[0])
    else:
        host_var.set('')

    host_menu_label = ttk.Label(frame2, text="Select Host:")
    host_menu_label.grid(row=1, column=0, padx=20, pady=5, sticky='E')
    host_menu = ttk.Combobox(frame2, textvariable=host_var, values=hosts, state='readonly')
    host_menu.grid(row=1, column=1, padx=20, pady=5)

    vlan_label = ttk.Label(frame2, text="VLAN:")
    vlan_label.grid(row=2, column=0, padx=20, pady=5, sticky='E')
    vlan_entry = ttk.Entry(frame2)
    vlan_entry.grid(row=2, column=1, padx=20, pady=5)

    ip_label = ttk.Label(frame2, text="IP Address (e.g., 10.0.2.1/24):")
    ip_label.grid(row=3, column=0, padx=20, pady=5, sticky='E')
    ip_entry = ttk.Entry(frame2)
    ip_entry.grid(row=3, column=1, padx=20, pady=5)

    btn_save_vlan = ttk.Button(frame2, text="Save VLAN Configuration", command=lambda: apply_vlan_config(host_var.get(), vlan_entry.get(), ip_entry.get()))
    btn_save_vlan.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    btn_to_frame1 = ttk.Button(frame2, text="Back", command=lambda: show_frame(frame1))
    btn_to_frame1.grid(row=5, column=0, columnspan=2, padx=20, pady=10)

    # ===== PAGE 3 =====
    lbl3 = ttk.Label(frame3, text="Host Configuration:")
    lbl3.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    host_name_l = ttk.Label(frame3, text="Host Name:")
    host_name_l.grid(row=1, column=0, padx=20, pady=5, sticky='E')
    host_entry = ttk.Entry(frame3)
    host_entry.grid(row=1, column=1, padx=20, pady=5)

    switch_connected_l = ttk.Label(frame3, text="Switch Connected to:")
    switch_connected_l.grid(row=2, column=0, padx=20, pady=5, sticky='E')
    switch_connected_entry = ttk.Entry(frame3)
    switch_connected_entry.grid(row=2, column=1, padx=20, pady=5)

    btn_save_host = ttk.Button(frame3, text="Add Host", command=lambda: apply_host_config(host_entry.get(), switch_connected_entry.get()))
    btn_save_host.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

    btn_to_frame1 = ttk.Button(frame3, text="Back", command=lambda: show_frame(frame1))
    btn_to_frame1.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

    # ===== PAGE 4 =====
    lbl4 = ttk.Label(frame4, text="Current Host Configuration")
    lbl4.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

    text_area = tk.Text(frame4, width=40, height=10, wrap=tk.WORD)
    text_area.grid(row=1, column=0, columnspan=2, padx=20, pady=5)
    update_text_area()

    btn_to_frame1 = ttk.Button(frame4, text="Clear Config", command=clear)
    btn_to_frame1.grid(row=2, column=0, columnspan=2, padx=20, pady=5)

    btn_to_frame1 = ttk.Button(frame4, text="Back", command=lambda: show_frame(frame1))
    btn_to_frame1.grid(row=3, column=0, columnspan=2, padx=20, pady=5)

    show_frame(frame1)

    root.mainloop()
