#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Padi(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("aqsa0", dpid="0000000000000002")
        s1 = self.addSwitch("iug1", dpid="0000000000000003")
        s2 = self.addSwitch("hu2", dpid="0000000000000004")
        s3 = self.addSwitch("ppu3", dpid="0000000000000005")
        s4 = self.addSwitch("azhr4", dpid="0000000000000006")
        s5 = self.addSwitch("arij5", dpid="0000000000000007")
        s6 = self.addSwitch("icb6", dpid="0000000000000008")
        s7 = self.addSwitch("geant7", dpid="0000000000000009")
        s8 = self.addSwitch("annajahn8", dpid="000000000000000a")
        s9 = self.addSwitch("aauj9", dpid="000000000000000b")
        s10 = self.addSwitch("bzu10", dpid="000000000000000c")
        s11 = self.addSwitch("padi211", dpid="000000000000000d")
        s12 = self.addSwitch("qou12", dpid="000000000000000e")
        s13 = self.addSwitch("aqu13", dpid="000000000000000f")
        s14 = self.addSwitch("bu14", dpid="0000000000000010")

        # Adding Links
        self.addLink(s3, s11)
        self.addLink(s7, s11)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s11, s13)
        self.addLink(s11, s14)


topos = {"Padi": (lambda: Padi())}
