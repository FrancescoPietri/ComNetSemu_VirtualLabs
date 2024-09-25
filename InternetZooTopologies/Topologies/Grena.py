#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Grena(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("cisco3640", dpid="0000000000000002")
        s1 = self.addSwitch("cisco2621", dpid="0000000000000003")
        s2 = self.addSwitch("cisco2512", dpid="0000000000000004")
        s3 = self.addSwitch("cisco3643", dpid="0000000000000005")
        s4 = self.addSwitch("cisco3644", dpid="0000000000000006")
        s5 = self.addSwitch("cisco3645", dpid="0000000000000007")
        s6 = self.addSwitch("cisco3646", dpid="0000000000000008")
        s7 = self.addSwitch("corecess7", dpid="0000000000000009")
        s8 = self.addSwitch("tbilisig8", dpid="000000000000000a")
        s9 = self.addSwitch("corecess9", dpid="000000000000000b")
        s10 = self.addSwitch("rustavic0", dpid="000000000000000c")
        s11 = self.addSwitch("cisco3641", dpid="000000000000000d")
        s12 = self.addSwitch("corecess2", dpid="000000000000000e")
        s13 = self.addSwitch("rustavic3", dpid="000000000000000f")
        s14 = self.addSwitch("cisco3644", dpid="0000000000000010")
        s15 = self.addSwitch("cisco3645", dpid="0000000000000011")

        # Adding Links
        self.addLink(s0, s4)
        self.addLink(s0, s15)
        self.addLink(s1, s4)
        self.addLink(s2, s3)
        self.addLink(s3, s7)
        self.addLink(s3, s15)
        self.addLink(s4, s5)
        self.addLink(s6, s14)
        self.addLink(s6, s15)
        self.addLink(s8, s11)
        self.addLink(s8, s13)
        self.addLink(s8, s14)
        self.addLink(s9, s10)
        self.addLink(s10, s13)
        self.addLink(s12, s13)


topos = {"Grena": (lambda: Grena())}
