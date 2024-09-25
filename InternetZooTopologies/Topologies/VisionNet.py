#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class VisionNet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("glasgow0", dpid="0000000000000002")
        s1 = self.addSwitch("bainvill1", dpid="0000000000000003")
        s2 = self.addSwitch("glendive2", dpid="0000000000000004")
        s3 = self.addSwitch("culberts3", dpid="0000000000000005")
        s4 = self.addSwitch("lincoln4", dpid="0000000000000006")
        s5 = self.addSwitch("helena5", dpid="0000000000000007")
        s6 = self.addSwitch("dillion6", dpid="0000000000000008")
        s7 = self.addSwitch("missoula7", dpid="0000000000000009")
        s8 = self.addSwitch("bozeman8", dpid="000000000000000a")
        s9 = self.addSwitch("sheridan9", dpid="000000000000000b")
        s10 = self.addSwitch("dcnnetwo0", dpid="000000000000000c")
        s11 = self.addSwitch("fortbent1", dpid="000000000000000d")
        s12 = self.addSwitch("seattle12", dpid="000000000000000e")
        s13 = self.addSwitch("havre13", dpid="000000000000000f")
        s14 = self.addSwitch("forsyth14", dpid="0000000000000010")
        s15 = self.addSwitch("milescit5", dpid="0000000000000011")
        s16 = self.addSwitch("noxon16", dpid="0000000000000012")
        s17 = self.addSwitch("kalispel7", dpid="0000000000000013")
        s18 = self.addSwitch("ncutbank8", dpid="0000000000000014")
        s19 = self.addSwitch("fairfiel9", dpid="0000000000000015")
        s20 = self.addSwitch("greatfal0", dpid="0000000000000016")
        s21 = self.addSwitch("moore21", dpid="0000000000000017")
        s22 = self.addSwitch("bigtimbe2", dpid="0000000000000018")
        s23 = self.addSwitch("billings3", dpid="0000000000000019")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s13)
        self.addLink(s1, s10)
        self.addLink(s1, s3)
        self.addLink(s2, s15)
        self.addLink(s4, s19)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s6)
        self.addLink(s7, s16)
        self.addLink(s9, s14)
        self.addLink(s11, s20)
        self.addLink(s11, s13)
        self.addLink(s11, s21)
        self.addLink(s12, s16)
        self.addLink(s13, s18)
        self.addLink(s14, s15)
        self.addLink(s14, s23)
        self.addLink(s16, s17)
        self.addLink(s19, s20)
        self.addLink(s21, s22)
        self.addLink(s22, s23)


topos = {"VisionNet": (lambda: VisionNet())}
