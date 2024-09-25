#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class EliBackbone(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("lasvegas0", dpid="0000000000000002")
        s1 = self.addSwitch("losangel1", dpid="0000000000000003")
        s2 = self.addSwitch("dallas2", dpid="0000000000000004")
        s3 = self.addSwitch("phoenix3", dpid="0000000000000005")
        s4 = self.addSwitch("santacla4", dpid="0000000000000006")
        s5 = self.addSwitch("portland5", dpid="0000000000000007")
        s6 = self.addSwitch("sacramen6", dpid="0000000000000008")
        s7 = self.addSwitch("paloalto7", dpid="0000000000000009")
        s8 = self.addSwitch("tacoma8", dpid="000000000000000a")
        s9 = self.addSwitch("seattle9", dpid="000000000000000b")
        s10 = self.addSwitch("atlanta10", dpid="000000000000000c")
        s11 = self.addSwitch("houston11", dpid="000000000000000d")
        s12 = self.addSwitch("spokane12", dpid="000000000000000e")
        s13 = self.addSwitch("boise13", dpid="000000000000000f")
        s14 = self.addSwitch("saltlake4", dpid="0000000000000010")
        s15 = self.addSwitch("minneapo5", dpid="0000000000000011")
        s16 = self.addSwitch("chicago16", dpid="0000000000000012")
        s17 = self.addSwitch("rocheste7", dpid="0000000000000013")
        s18 = self.addSwitch("newark18", dpid="0000000000000014")
        s19 = self.addSwitch("washingt9", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s3)
        self.addLink(s0, s14)
        self.addLink(s1, s3)
        self.addLink(s1, s4)
        self.addLink(s2, s16)
        self.addLink(s2, s11)
        self.addLink(s2, s3)
        self.addLink(s2, s19)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s6)
        self.addLink(s6, s8)
        self.addLink(s6, s14)
        self.addLink(s6, s7)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        self.addLink(s9, s12)
        self.addLink(s9, s13)
        self.addLink(s9, s14)
        self.addLink(s9, s15)
        self.addLink(s10, s11)
        self.addLink(s10, s19)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s14, s16)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s18, s19)


topos = {"EliBackbone": (lambda: EliBackbone())}
