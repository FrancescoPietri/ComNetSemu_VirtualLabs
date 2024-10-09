import os
import os.path as op
import tkinter as tk
from tkinter import filedialog, messagebox
import json

PATH_DATASET = 'DatasetGML/'
PATH_TOPOLOGIES = 'Topologies/'

VlanConfig = {}
HostToSwitchConfig = {}

def add_vlans(nameFile):
    try:
        with open('VlanConfig.json', 'r') as vlc:
            VlanConfig = json.load(vlc)

        with open('HostConfig.json', 'r') as htc:
            HostToSwitchConfig = json.load(htc)

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

        contents.insert(indexToWrite, f"\n        #adding host to switch links\n")

        for switch in HostToSwitchConfig:
            contents.insert(indexToWrite, f"        self.addLink({switch}, {HostToSwitchConfig[switch]}) \n")

        contents.insert(indexToWrite, f"\n        #adding hosts \n")

        for host in VlanConfig:
            contents.insert(indexToWrite, f"        {host} = self.addHost('{host}', cls=VLANHost, vlan={VlanConfig[host]['vlan']}, ip='{VlanConfig[host]['ip']}') \n")

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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("VLAN Configurator")

    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)

    lbl = tk.Label(frame, text="Click the button to select a topology file and add VLANs:")
    lbl.pack(pady=10)

    btn = tk.Button(frame, text="Select File", command=select_file)
    btn.pack(pady=10)

    root.mainloop()

