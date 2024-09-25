#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Kreonet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("jeonju0", dpid="0000000000000002")
        s1 = self.addSwitch("jeju1", dpid="0000000000000003")
        s2 = self.addSwitch("kwangju2", dpid="0000000000000004")
        s3 = self.addSwitch("busan3", dpid="0000000000000005")
        s4 = self.addSwitch("changwon4", dpid="0000000000000006")
        s5 = self.addSwitch("seoul5", dpid="0000000000000007")
        s6 = self.addSwitch("incheon6", dpid="0000000000000008")
        s7 = self.addSwitch("suwon7", dpid="0000000000000009")
        s8 = self.addSwitch("cheonan8", dpid="000000000000000a")
        s9 = self.addSwitch("ochang9", dpid="000000000000000b")
        s10 = self.addSwitch("daejeon10", dpid="000000000000000c")
        s11 = self.addSwitch("pohang11", dpid="000000000000000d")
        s12 = self.addSwitch("daegu12", dpid="000000000000000e")

        # Adding Links
        self.addLink(s0, s10)
        self.addLink(s1, s2)
        self.addLink(s2, s10)
        self.addLink(s3, s10)
        self.addLink(s4, s10)
        self.addLink(s5, s10)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s8, s10)
        self.addLink(s9, s10)
        self.addLink(s10, s11)
        self.addLink(s10, s12)


topos = {"Kreonet": (lambda: Kreonet())}
