#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Spiralight(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("milwauke0", dpid="0000000000000002")
        s1 = self.addSwitch("rockford1", dpid="0000000000000003")
        s2 = self.addSwitch("janesvil2", dpid="0000000000000004")
        s3 = self.addSwitch("waukesha3", dpid="0000000000000005")
        s4 = self.addSwitch("chicago4", dpid="0000000000000006")
        s5 = self.addSwitch("madison5", dpid="0000000000000007")
        s6 = self.addSwitch("campdoug6", dpid="0000000000000008")
        s7 = self.addSwitch("minneaop7", dpid="0000000000000009")
        s8 = self.addSwitch("eauclair8", dpid="000000000000000a")
        s9 = self.addSwitch("wausau9", dpid="000000000000000b")
        s10 = self.addSwitch("greenbay0", dpid="000000000000000c")
        s11 = self.addSwitch("appleton1", dpid="000000000000000d")
        s12 = self.addSwitch("oshkosh12", dpid="000000000000000e")
        s13 = self.addSwitch("fondulac3", dpid="000000000000000f")
        s14 = self.addSwitch("beaverda4", dpid="0000000000000010")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s4)
        self.addLink(s1, s2)
        self.addLink(s1, s4)
        self.addLink(s2, s5)
        self.addLink(s3, s5)
        self.addLink(s5, s6)
        self.addLink(s5, s14)
        self.addLink(s6, s8)
        self.addLink(s7, s8)
        self.addLink(s7, s9)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s13, s14)


topos = {"Spiralight": (lambda: Spiralight())}
