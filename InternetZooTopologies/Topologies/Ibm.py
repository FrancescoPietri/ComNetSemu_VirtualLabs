#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ibm(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("montreal0", dpid="0000000000000002")
        s1 = self.addSwitch("whitepla1", dpid="0000000000000003")
        s2 = self.addSwitch("detroit2", dpid="0000000000000004")
        s3 = self.addSwitch("toronto3", dpid="0000000000000005")
        s4 = self.addSwitch("columbus4", dpid="0000000000000006")
        s5 = self.addSwitch("bethesda5", dpid="0000000000000007")
        s6 = self.addSwitch("newyork66", dpid="0000000000000008")
        s7 = self.addSwitch("philadel7", dpid="0000000000000009")
        s8 = self.addSwitch("schaumbu8", dpid="000000000000000a")
        s9 = self.addSwitch("stlouis99", dpid="000000000000000b")
        s10 = self.addSwitch("vancouve0", dpid="000000000000000c")
        s11 = self.addSwitch("sanfranc1", dpid="000000000000000d")
        s12 = self.addSwitch("losangel2", dpid="000000000000000e")
        s13 = self.addSwitch("phoenix13", dpid="000000000000000f")
        s14 = self.addSwitch("dallas14", dpid="0000000000000010")
        s15 = self.addSwitch("atlanta15", dpid="0000000000000011")
        s16 = self.addSwitch("tampa16", dpid="0000000000000012")
        s17 = self.addSwitch("chicago17", dpid="0000000000000013")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s7)
        self.addLink(s1, s17)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s2, s9)
        self.addLink(s2, s3)
        self.addLink(s2, s4)
        self.addLink(s4, s8)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s15)
        self.addLink(s6, s16)
        self.addLink(s6, s7)
        self.addLink(s8, s12)
        self.addLink(s9, s17)
        self.addLink(s10, s11)
        self.addLink(s11, s17)
        self.addLink(s11, s12)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s14, s17)
        self.addLink(s14, s15)
        self.addLink(s15, s16)


topos = {"Ibm": (lambda: Ibm())}
