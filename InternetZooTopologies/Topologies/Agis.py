#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Agis(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("miami0", dpid="0000000000000002")
        s1 = self.addSwitch("houston1", dpid="0000000000000003")
        s2 = self.addSwitch("washingt2", dpid="0000000000000004")
        s3 = self.addSwitch("atlanta3", dpid="0000000000000005")
        s4 = self.addSwitch("mexicoci4", dpid="0000000000000006")
        s5 = self.addSwitch("phoenix5", dpid="0000000000000007")
        s6 = self.addSwitch("dallas6", dpid="0000000000000008")
        s7 = self.addSwitch("stlouis77", dpid="0000000000000009")
        s8 = self.addSwitch("sandiego8", dpid="000000000000000a")
        s9 = self.addSwitch("losangel9", dpid="000000000000000b")
        s10 = self.addSwitch("santacla0", dpid="000000000000000c")
        s11 = self.addSwitch("stockton1", dpid="000000000000000d")
        s12 = self.addSwitch("sacramen2", dpid="000000000000000e")
        s13 = self.addSwitch("fresno13", dpid="000000000000000f")
        s14 = self.addSwitch("sanfranc4", dpid="0000000000000010")
        s15 = self.addSwitch("newyork15", dpid="0000000000000011")
        s16 = self.addSwitch("boston16", dpid="0000000000000012")
        s17 = self.addSwitch("seattle17", dpid="0000000000000013")
        s18 = self.addSwitch("saltlake8", dpid="0000000000000014")
        s19 = self.addSwitch("chicago19", dpid="0000000000000015")
        s20 = self.addSwitch("minneapo0", dpid="0000000000000016")
        s21 = self.addSwitch("detroit21", dpid="0000000000000017")
        s22 = self.addSwitch("pittsbur2", dpid="0000000000000018")
        s23 = self.addSwitch("philadel3", dpid="0000000000000019")
        s24 = self.addSwitch("pennsauk4", dpid="000000000000001a")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s23)
        self.addLink(s3, s6)
        self.addLink(s3, s15)
        self.addLink(s4, s6)
        self.addLink(s5, s9)
        self.addLink(s5, s6)
        self.addLink(s6, s7)
        self.addLink(s7, s19)
        self.addLink(s8, s9)
        self.addLink(s9, s10)
        self.addLink(s9, s12)
        self.addLink(s9, s19)
        self.addLink(s9, s24)
        self.addLink(s10, s11)
        self.addLink(s10, s12)
        self.addLink(s10, s13)
        self.addLink(s10, s14)
        self.addLink(s14, s17)
        self.addLink(s15, s16)
        self.addLink(s15, s23)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s19, s20)
        self.addLink(s19, s21)
        self.addLink(s21, s22)
        self.addLink(s22, s23)
        self.addLink(s23, s24)


topos = {"Agis": (lambda: Agis())}
