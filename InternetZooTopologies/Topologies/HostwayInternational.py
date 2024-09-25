#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class HostwayInternational(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("seattle0", dpid="0000000000000002")
        s1 = self.addSwitch("tampa1", dpid="0000000000000003")
        s2 = self.addSwitch("chicago2", dpid="0000000000000004")
        s3 = self.addSwitch("vancouve3", dpid="0000000000000005")
        s4 = self.addSwitch("miami4", dpid="0000000000000006")
        s5 = self.addSwitch("austin5", dpid="0000000000000007")
        s6 = self.addSwitch("newyork66", dpid="0000000000000008")
        s7 = self.addSwitch("atlanta7", dpid="0000000000000009")
        s8 = self.addSwitch("buchares8", dpid="000000000000000a")
        s9 = self.addSwitch("seoul9", dpid="000000000000000b")
        s10 = self.addSwitch("sydney10", dpid="000000000000000c")
        s11 = self.addSwitch("hannover1", dpid="000000000000000d")
        s12 = self.addSwitch("amsterda2", dpid="000000000000000e")
        s13 = self.addSwitch("antwerp13", dpid="000000000000000f")
        s14 = self.addSwitch("frankfur4", dpid="0000000000000010")
        s15 = self.addSwitch("london15", dpid="0000000000000011")

        # Adding Links
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s5)
        self.addLink(s1, s4)
        self.addLink(s1, s7)
        self.addLink(s2, s5)
        self.addLink(s2, s7)
        self.addLink(s4, s10)
        self.addLink(s4, s6)
        self.addLink(s4, s7)
        self.addLink(s6, s10)
        self.addLink(s6, s7)
        self.addLink(s6, s15)
        self.addLink(s8, s9)
        self.addLink(s8, s14)
        self.addLink(s9, s10)
        self.addLink(s11, s12)
        self.addLink(s11, s14)
        self.addLink(s12, s13)
        self.addLink(s12, s15)
        self.addLink(s13, s14)


topos = {"HostwayInternational": (lambda: HostwayInternational())}
