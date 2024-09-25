#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Sago(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("ftpierc0", dpid="0000000000000002")
        s1 = self.addSwitch("melbourn1", dpid="0000000000000003")
        s2 = self.addSwitch("lakealfr2", dpid="0000000000000004")
        s3 = self.addSwitch("orlando3", dpid="0000000000000005")
        s4 = self.addSwitch("westpalm4", dpid="0000000000000006")
        s5 = self.addSwitch("tampa5", dpid="0000000000000007")
        s6 = self.addSwitch("miami6", dpid="0000000000000008")
        s7 = self.addSwitch("ftlaude7", dpid="0000000000000009")
        s8 = self.addSwitch("flovilla8", dpid="000000000000000a")
        s9 = self.addSwitch("atlanta9", dpid="000000000000000b")
        s10 = self.addSwitch("tarrytow0", dpid="000000000000000c")
        s11 = self.addSwitch("gordon11", dpid="000000000000000d")
        s12 = self.addSwitch("newell12", dpid="000000000000000e")
        s13 = self.addSwitch("surrency3", dpid="000000000000000f")
        s14 = self.addSwitch("staugus4", dpid="0000000000000010")
        s15 = self.addSwitch("jacksonv5", dpid="0000000000000011")
        s16 = self.addSwitch("titusvil6", dpid="0000000000000012")
        s17 = self.addSwitch("daytonab7", dpid="0000000000000013")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s4)
        self.addLink(s1, s16)
        self.addLink(s2, s3)
        self.addLink(s2, s5)
        self.addLink(s3, s17)
        self.addLink(s4, s7)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s8, s11)
        self.addLink(s10, s11)
        self.addLink(s10, s13)
        self.addLink(s12, s13)
        self.addLink(s12, s15)
        self.addLink(s14, s17)
        self.addLink(s14, s15)
        self.addLink(s16, s17)


topos = {"Sago": (lambda: Sago())}
