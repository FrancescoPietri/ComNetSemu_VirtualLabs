#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class LabTopologyLink(Topo):
    "LabTopologyLink"

    def __init__(self):

        Topo.__init__(self)

        # Define switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')
        s2 = self.addSwitch('s2', dpid='0000000000000002')
        s3l1 = self.addSwitch('s3l1', dpid='0000000000000003')
        s4l2 = self.addSwitch('s4l2', dpid='0000000000000004')
        s5l3 = self.addSwitch('s5l3', dpid='0000000000000005')
        s6l4 = self.addSwitch('s6l4', dpid='0000000000000006')
        s7 = self.addSwitch('s7', dpid='0000000000000007')
        s8 = self.addSwitch('s8', dpid='0000000000000008')  
        

        # Define hosts with VLANs
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        
        # Link configurations
        queue_lenght = 10
        host_link_config = dict()             # Default host links
        weakbb_link_config = dict(delay='40ms', use_tbf=True, bw=10, max_queue_size=queue_lenght, burst=1000000)     # Weak backbone links (low bandwidth)
        strongbb_link_config = dict(delay='25ms', use_tbf=True, bw=50, max_queue_size=queue_lenght, burst=1000000)     # Strong backbone links (high bandwidth)

        # Add links between hosts and switches
        self.addLink(h1, s3l1,  **host_link_config)
        self.addLink(h2, s3l1,  **host_link_config)
        self.addLink(h3, s4l2,  **host_link_config)
        self.addLink(h4, s4l2,  **host_link_config)
        self.addLink(h5, s5l3,  **host_link_config)
        self.addLink(h6, s5l3,  **host_link_config)
        self.addLink(h7, s6l4,  **host_link_config)
        self.addLink(h8, s6l4,  **host_link_config)
        self.addLink(h9, s1,  **host_link_config)

        # Add links between switches
        self.addLink(s1, s2,  **strongbb_link_config)
        self.addLink(s2, s3l1, **strongbb_link_config)
        self.addLink(s2, s4l2, **strongbb_link_config)
        self.addLink(s2, s5l3, **strongbb_link_config)
        self.addLink(s2, s6l4, **strongbb_link_config)
        self.addLink(s5l3, s8, **weakbb_link_config)
        self.addLink(s6l4, s8, **weakbb_link_config)
        self.addLink(s3l1, s7, **weakbb_link_config)
        self.addLink(s4l2, s7, **weakbb_link_config)
        self.addLink(s7, s1, **weakbb_link_config)
        self.addLink(s8, s1, **weakbb_link_config)

topos = { 'labtopologylink': ( lambda: LabTopologyLink() ) }