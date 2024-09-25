#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class BtAsiaPac(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("jakarta0", dpid="0000000000000002")
        s1 = self.addSwitch("perth1", dpid="0000000000000003")
        s2 = self.addSwitch("singapor2", dpid="0000000000000004")
        s3 = self.addSwitch("kualalum3", dpid="0000000000000005")
        s4 = self.addSwitch("sanjose44", dpid="0000000000000006")
        s5 = self.addSwitch("losangel5", dpid="0000000000000007")
        s6 = self.addSwitch("sydney6", dpid="0000000000000008")
        s7 = self.addSwitch("auckland7", dpid="0000000000000009")
        s8 = self.addSwitch("london8", dpid="000000000000000a")
        s9 = self.addSwitch("paloalto9", dpid="000000000000000b")
        s10 = self.addSwitch("newdelhi0", dpid="000000000000000c")
        s11 = self.addSwitch("mumbai11", dpid="000000000000000d")
        s12 = self.addSwitch("seoul12", dpid="000000000000000e")
        s13 = self.addSwitch("tokyo13", dpid="000000000000000f")
        s14 = self.addSwitch("taipei14", dpid="0000000000000010")
        s15 = self.addSwitch("hongkong5", dpid="0000000000000011")
        s16 = self.addSwitch("manila16", dpid="0000000000000012")
        s17 = self.addSwitch("bangkok17", dpid="0000000000000013")
        s18 = self.addSwitch("chenai18", dpid="0000000000000014")
        s19 = self.addSwitch("mumbai19", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s15)
        self.addLink(s1, s2)
        self.addLink(s1, s6)
        self.addLink(s1, s15)
        self.addLink(s2, s3)
        self.addLink(s2, s6)
        self.addLink(s2, s8)
        self.addLink(s2, s17)
        self.addLink(s2, s18)
        self.addLink(s2, s19)
        self.addLink(s4, s13)
        self.addLink(s4, s6)
        self.addLink(s4, s15)
        self.addLink(s5, s15)
        self.addLink(s5, s13)
        self.addLink(s5, s6)
        self.addLink(s5, s7)
        self.addLink(s6, s7)
        self.addLink(s8, s11)
        self.addLink(s8, s15)
        self.addLink(s9, s15)
        self.addLink(s10, s11)
        self.addLink(s11, s15)
        self.addLink(s12, s13)
        self.addLink(s12, s15)
        self.addLink(s13, s14)
        self.addLink(s13, s15)
        self.addLink(s13, s16)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s15, s17)


topos = {"BtAsiaPac": (lambda: BtAsiaPac())}
