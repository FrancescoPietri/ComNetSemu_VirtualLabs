#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Istar(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("montreal0", dpid="0000000000000002")
        s1 = self.addSwitch("quebec1", dpid="0000000000000003")
        s2 = self.addSwitch("london2", dpid="0000000000000004")
        s3 = self.addSwitch("internet3", dpid="0000000000000005")
        s4 = self.addSwitch("moncton4", dpid="0000000000000006")
        s5 = self.addSwitch("halifax5", dpid="0000000000000007")
        s6 = self.addSwitch("sherbroo6", dpid="0000000000000008")
        s7 = self.addSwitch("saintjoh7", dpid="0000000000000009")
        s8 = self.addSwitch("sydney8", dpid="000000000000000a")
        s9 = self.addSwitch("yarmouth9", dpid="000000000000000b")
        s10 = self.addSwitch("anscore0", dpid="000000000000000c")
        s11 = self.addSwitch("internet1", dpid="000000000000000d")
        s12 = self.addSwitch("victoria2", dpid="000000000000000e")
        s13 = self.addSwitch("toronto13", dpid="000000000000000f")
        s14 = self.addSwitch("hamilton4", dpid="0000000000000010")
        s15 = self.addSwitch("vancouve5", dpid="0000000000000011")
        s16 = self.addSwitch("anscore6", dpid="0000000000000012")
        s17 = self.addSwitch("calgary17", dpid="0000000000000013")
        s18 = self.addSwitch("edmonton8", dpid="0000000000000014")
        s19 = self.addSwitch("lethbrid9", dpid="0000000000000015")
        s20 = self.addSwitch("winnipeg0", dpid="0000000000000016")
        s21 = self.addSwitch("ottawa21", dpid="0000000000000017")
        s22 = self.addSwitch("kitchene2", dpid="0000000000000018")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s4)
        self.addLink(s0, s13)
        self.addLink(s0, s6)
        self.addLink(s0, s21)
        self.addLink(s2, s13)
        self.addLink(s3, s13)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s10, s13)
        self.addLink(s11, s15)
        self.addLink(s12, s15)
        self.addLink(s13, s14)
        self.addLink(s13, s21)
        self.addLink(s13, s22)
        self.addLink(s15, s16)
        self.addLink(s15, s17)
        self.addLink(s15, s21)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s20, s21)


topos = {"Istar": (lambda: Istar())}
