#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Rhnet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("solborg0", dpid="0000000000000002")
        s1 = self.addSwitch("fjarski1", dpid="0000000000000003")
        s2 = self.addSwitch("fsaakur2", dpid="0000000000000004")
        s3 = self.addSwitch("dstakur3", dpid="0000000000000005")
        s4 = self.addSwitch("rix4", dpid="0000000000000006")
        s5 = self.addSwitch("nordunet5", dpid="0000000000000007")
        s6 = self.addSwitch("hvanneyr6", dpid="0000000000000008")
        s7 = self.addSwitch("bifrost7", dpid="0000000000000009")
        s8 = self.addSwitch("grensas8", dpid="000000000000000a")
        s9 = self.addSwitch("skulagat9", dpid="000000000000000b")
        s10 = self.addSwitch("taekniga0", dpid="000000000000000c")
        s11 = self.addSwitch("sturluga1", dpid="000000000000000d")
        s12 = self.addSwitch("hringbra2", dpid="000000000000000e")
        s13 = self.addSwitch("bustaoav3", dpid="000000000000000f")
        s14 = self.addSwitch("ofanleit4", dpid="0000000000000010")
        s15 = self.addSwitch("keldhaho5", dpid="0000000000000011")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s1, s10)
        self.addLink(s1, s3)
        self.addLink(s2, s3)
        self.addLink(s4, s10)
        self.addLink(s5, s10)
        self.addLink(s5, s11)
        self.addLink(s6, s7)
        self.addLink(s6, s15)
        self.addLink(s8, s9)
        self.addLink(s8, s15)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s14, s15)


topos = {"Rhnet": (lambda: Rhnet())}
