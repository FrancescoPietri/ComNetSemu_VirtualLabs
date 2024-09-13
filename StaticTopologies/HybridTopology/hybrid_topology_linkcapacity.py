#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from sys import exit  
from mininet.node import Host
from mininet.util import quietRun
from mininet.log import error
import random

class HybridTopologyLink(Topo):
    "HybridTopology with custom link capacities"

    def __init__(self):
        Topo.__init__(self)

        # Define switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')  
        s2 = self.addSwitch('s2', dpid='0000000000000002')
        s3 = self.addSwitch('s3', dpid='0000000000000003')
        s4 = self.addSwitch('s4', dpid='0000000000000004') 
        s5 = self.addSwitch('s5', dpid='0000000000000005')
        s6 = self.addSwitch('s6', dpid='0000000000000006')  
        s7 = self.addSwitch('s7', dpid='0000000000000007')
        s8 = self.addSwitch('s8', dpid='0000000000000008')
        s9 = self.addSwitch('s9', dpid='0000000000000009')
        s10 = self.addSwitch('s10', dpid='000000000000000a')
        s11 = self.addSwitch('s11', dpid='000000000000000b')
        s12 = self.addSwitch('s12', dpid='000000000000000c')

        # Define hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')

        # Link configurations
        queue_length = 10
        host_link_config = dict()  # Default host links
        weakbb_link_config = dict(delay='20ms', use_tbf=True, bw=20, max_queue_size=queue_length, latency_ms=10000000, burst=1000000)  # Weak backbone links (low bandwidth)
        strongbb_link_config = dict(delay='25ms', use_tbf=True, bw=50, max_queue_size=queue_length, latency_ms=10000000, burst=1000000)  # Strong backbone links (high bandwidth)

        # Add links between hosts and switches
        self.addLink(h1, s1, **host_link_config)
        self.addLink(h2, s9, **host_link_config)
        self.addLink(h3, s10, **host_link_config)
        self.addLink(h4, s11, **host_link_config)
        self.addLink(h5, s12, **host_link_config)
        self.addLink(h6, s6, **host_link_config)

        # Add links between switches with explicit random "weak" or "strong" configurations
        self.addLink(s1, s2, **weakbb_link_config)
        self.addLink(s1, s3, **strongbb_link_config)
        self.addLink(s2, s4, **weakbb_link_config)
        self.addLink(s3, s4, **weakbb_link_config)
        self.addLink(s4, s5, **strongbb_link_config)
        self.addLink(s5, s6, **strongbb_link_config)
        self.addLink(s5, s7, **weakbb_link_config)
        self.addLink(s5, s8, **strongbb_link_config)
        self.addLink(s7, s9, **strongbb_link_config)
        self.addLink(s7, s10, **weakbb_link_config)
        self.addLink(s8, s11, **strongbb_link_config)
        self.addLink(s8, s12, **strongbb_link_config)


topos = { 'hybridtopologylink': ( lambda: HybridTopologyLink() ) }
