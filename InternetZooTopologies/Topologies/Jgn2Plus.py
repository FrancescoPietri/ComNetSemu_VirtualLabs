#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Jgn2Plus(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("chugoku0", dpid="0000000000000002")
        s1 = self.addSwitch("kinki1", dpid="0000000000000003")
        s2 = self.addSwitch("kyushu2", dpid="0000000000000004")
        s3 = self.addSwitch("shikoku3", dpid="0000000000000005")
        s4 = self.addSwitch("shinetsu4", dpid="0000000000000006")
        s5 = self.addSwitch("busan5", dpid="0000000000000007")
        s6 = self.addSwitch("tokai6", dpid="0000000000000008")
        s7 = self.addSwitch("hokuriku7", dpid="0000000000000009")
        s8 = self.addSwitch("hongkong8", dpid="000000000000000a")
        s9 = self.addSwitch("okinawa9", dpid="000000000000000b")
        s10 = self.addSwitch("hokkaido0", dpid="000000000000000c")
        s11 = self.addSwitch("tohoku11", dpid="000000000000000d")
        s12 = self.addSwitch("tokyo12", dpid="000000000000000e")
        s13 = self.addSwitch("chicago13", dpid="000000000000000f")
        s14 = self.addSwitch("losangel4", dpid="0000000000000010")
        s15 = self.addSwitch("none15", dpid="0000000000000011")
        s16 = self.addSwitch("singapor6", dpid="0000000000000012")
        s17 = self.addSwitch("bangkok17", dpid="0000000000000013")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s6)
        self.addLink(s2, s9)
        self.addLink(s2, s5)
        self.addLink(s4, s12)
        self.addLink(s6, s12)
        self.addLink(s7, s12)
        self.addLink(s8, s12)
        self.addLink(s10, s11)
        self.addLink(s11, s12)
        self.addLink(s12, s15)
        self.addLink(s12, s16)
        self.addLink(s12, s17)
        self.addLink(s13, s15)
        self.addLink(s14, s15)


topos = {"Jgn2Plus": (lambda: Jgn2Plus())}
