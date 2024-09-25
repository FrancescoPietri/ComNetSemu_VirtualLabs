#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Itnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("limerick0", dpid="0000000000000002")
        s1 = self.addSwitch("cork1", dpid="0000000000000003")
        s2 = self.addSwitch("tralee2", dpid="0000000000000004")
        s3 = self.addSwitch("galway3", dpid="0000000000000005")
        s4 = self.addSwitch("sligo4", dpid="0000000000000006")
        s5 = self.addSwitch("letterke5", dpid="0000000000000007")
        s6 = self.addSwitch("athlone6", dpid="0000000000000008")
        s7 = self.addSwitch("dundalk7", dpid="0000000000000009")
        s8 = self.addSwitch("blanchar8", dpid="000000000000000a")
        s9 = self.addSwitch("carlow9", dpid="000000000000000b")
        s10 = self.addSwitch("waterfor0", dpid="000000000000000c")

        # Adding Links
        self.addLink(s0, s8)
        self.addLink(s1, s8)
        self.addLink(s2, s8)
        self.addLink(s3, s8)
        self.addLink(s4, s8)
        self.addLink(s5, s8)
        self.addLink(s6, s8)
        self.addLink(s7, s8)
        self.addLink(s8, s9)
        self.addLink(s8, s10)


topos = {"Itnet": (lambda: Itnet())}
