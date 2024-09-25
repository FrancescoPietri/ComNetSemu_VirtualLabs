#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Navigata(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("newyork00", dpid="0000000000000002")
        s1 = self.addSwitch("montreal1", dpid="0000000000000003")
        s2 = self.addSwitch("halifax2", dpid="0000000000000004")
        s3 = self.addSwitch("losangel3", dpid="0000000000000005")
        s4 = self.addSwitch("toronto4", dpid="0000000000000006")
        s5 = self.addSwitch("vancouve5", dpid="0000000000000007")
        s6 = self.addSwitch("victoria6", dpid="0000000000000008")
        s7 = self.addSwitch("seattle7", dpid="0000000000000009")
        s8 = self.addSwitch("calgary8", dpid="000000000000000a")
        s9 = self.addSwitch("edmonton9", dpid="000000000000000b")
        s10 = self.addSwitch("saskatoo0", dpid="000000000000000c")
        s11 = self.addSwitch("regina11", dpid="000000000000000d")
        s12 = self.addSwitch("winnipeg2", dpid="000000000000000e")

        # Adding Links
        self.addLink(s0, s4)
        self.addLink(s1, s4)
        self.addLink(s2, s4)
        self.addLink(s3, s5)
        self.addLink(s4, s11)
        self.addLink(s4, s10)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s5, s10)
        self.addLink(s5, s11)
        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s11)
        self.addLink(s10, s12)
        self.addLink(s11, s12)


topos = {"Navigata": (lambda: Navigata())}
