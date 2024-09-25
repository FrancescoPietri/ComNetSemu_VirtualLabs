#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class GtsRomania(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("craiova0", dpid="0000000000000002")
        s1 = self.addSwitch("plaiesti1", dpid="0000000000000003")
        s2 = self.addSwitch("brasov2", dpid="0000000000000004")
        s3 = self.addSwitch("targovis3", dpid="0000000000000005")
        s4 = self.addSwitch("constant4", dpid="0000000000000006")
        s5 = self.addSwitch("bucarest5", dpid="0000000000000007")
        s6 = self.addSwitch("galati6", dpid="0000000000000008")
        s7 = self.addSwitch("focsani7", dpid="0000000000000009")
        s8 = self.addSwitch("budapest8", dpid="000000000000000a")
        s9 = self.addSwitch("budapest9", dpid="000000000000000b")
        s10 = self.addSwitch("targumur0", dpid="000000000000000c")
        s11 = self.addSwitch("timisoar1", dpid="000000000000000d")
        s12 = self.addSwitch("sibiu12", dpid="000000000000000e")
        s13 = self.addSwitch("iasi13", dpid="000000000000000f")
        s14 = self.addSwitch("piatrane4", dpid="0000000000000010")
        s15 = self.addSwitch("bacau15", dpid="0000000000000011")
        s16 = self.addSwitch("deva16", dpid="0000000000000012")
        s17 = self.addSwitch("cluj17", dpid="0000000000000013")
        s18 = self.addSwitch("oradea18", dpid="0000000000000014")
        s19 = self.addSwitch("bors19", dpid="0000000000000015")
        s20 = self.addSwitch("arad20", dpid="0000000000000016")

        # Adding Links
        self.addLink(s0, s11)
        self.addLink(s0, s5)
        self.addLink(s1, s5)
        self.addLink(s2, s17)
        self.addLink(s2, s5)
        self.addLink(s3, s5)
        self.addLink(s4, s5)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s5, s10)
        self.addLink(s5, s13)
        self.addLink(s5, s15)
        self.addLink(s5, s18)
        self.addLink(s7, s14)
        self.addLink(s8, s19)
        self.addLink(s9, s20)
        self.addLink(s11, s16)
        self.addLink(s11, s20)
        self.addLink(s12, s18)
        self.addLink(s13, s18)
        self.addLink(s15, s18)
        self.addLink(s17, s18)
        self.addLink(s18, s19)
        self.addLink(s18, s20)


topos = {"GtsRomania": (lambda: GtsRomania())}
