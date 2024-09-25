#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sprint(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("cheyenne0", dpid="0000000000000002")
        s1 = self.addSwitch("atlanta1", dpid="0000000000000003")
        s2 = self.addSwitch("boulder2", dpid="0000000000000004")
        s3 = self.addSwitch("seattle3", dpid="0000000000000005")
        s4 = self.addSwitch("stockton4", dpid="0000000000000006")
        s5 = self.addSwitch("anaheim5", dpid="0000000000000007")
        s6 = self.addSwitch("fortwort6", dpid="0000000000000008")
        s7 = self.addSwitch("kansasci7", dpid="0000000000000009")
        s8 = self.addSwitch("chicago8", dpid="000000000000000a")
        s9 = self.addSwitch("newyork9", dpid="000000000000000b")
        s10 = self.addSwitch("washingt0", dpid="000000000000000c")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s4)
        self.addLink(s0, s7)
        self.addLink(s1, s10)
        self.addLink(s1, s6)
        self.addLink(s3, s8)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s4, s8)
        self.addLink(s4, s9)
        self.addLink(s4, s10)
        self.addLink(s5, s6)
        self.addLink(s6, s10)
        self.addLink(s6, s7)
        self.addLink(s7, s8)
        self.addLink(s7, s10)
        self.addLink(s8, s9)
        self.addLink(s9, s10)


topos = {"Sprint": (lambda: Sprint())}
