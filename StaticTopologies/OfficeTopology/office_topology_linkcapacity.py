#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class OfficeTopologyLink(Topo):
    "OfficeTopology with custom link configurations"

    def __init__(self):
        
        Topo.__init__(self)

        sof1 = self.addSwitch('sof1', dpid='0000000000000002')  # Switch office 1
        sof2 = self.addSwitch('sof2', dpid='0000000000000003')
        sof3 = self.addSwitch('sof3', dpid='0000000000000004')
        sbb1 = self.addSwitch('sbb1', dpid='0000000000000005')  # Switch backbone 1
        sbb2 = self.addSwitch('sbb2', dpid='0000000000000006')
        smo1 = self.addSwitch('smo1', dpid='0000000000000007')  # Switch main office 1
        spr1 = self.addSwitch('spr1', dpid='0000000000000008')        # Switch print room 1

        # Define hosts
        h1of1 = self.addHost('h1of1')
        h2of1 = self.addHost('h2of1')
        h1of2 = self.addHost('h1of2')
        h2of2 = self.addHost('h2of2')
        h1of3 = self.addHost('h1of3')
        h2of3 = self.addHost('h2of3')
        h1mo1 = self.addHost('h1mo1')
        h1pr1 = self.addHost('h1pr1')

        # Link configurations
        queue_lenght = 10
        host_link_config = dict()             # Default host links
        weakbb_link_config = dict(delay='20ms', use_tbf=True, bw=20, max_queue_size=queue_lenght, latency_ms=10000000, burst=1000000)     # Weak backbone links (low bandwidth)
        strongbb_link_config = dict(delay='25ms', use_tbf=True, bw=50, max_queue_size=queue_lenght, latency_ms=10000000, burst=1000000)     # Strong backbone links (high bandwidth)

        # Add links between hosts and switches
        self.addLink(h1of1, sof1, **host_link_config)
        self.addLink(h2of1, sof1, **host_link_config)
        self.addLink(h1of2, sof2, **host_link_config)
        self.addLink(h2of2, sof2, **host_link_config)
        self.addLink(h1of3, sof3, **host_link_config)
        self.addLink(h2of3, sof3, **host_link_config)
        self.addLink(h1mo1, smo1, **host_link_config)
        self.addLink(h1pr1, spr1, **host_link_config)

        # Add links between switches with custom bandwidths
        self.addLink(sof1, sof2, **weakbb_link_config)
        self.addLink(sof2, sof3, **strongbb_link_config)
        self.addLink(sof1, sbb1, **strongbb_link_config)
        self.addLink(sof2, sbb1, **weakbb_link_config)
        self.addLink(sof3, sbb1, **strongbb_link_config)
        self.addLink(sof1, spr1, **weakbb_link_config)
        self.addLink(sof3, smo1, **strongbb_link_config)
        self.addLink(smo1, sbb2, **weakbb_link_config)
        self.addLink(spr1, sbb2, **strongbb_link_config)
        self.addLink(sbb1, sbb2, **strongbb_link_config)

topos = { 'officetopologylink': ( lambda: OfficeTopologyLink() ) }
