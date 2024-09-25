#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Noel(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("spokane0", dpid="0000000000000002")
        s1 = self.addSwitch("coeurda1", dpid="0000000000000003")
        s2 = self.addSwitch("wenatche2", dpid="0000000000000004")
        s3 = self.addSwitch("othello3", dpid="0000000000000005")
        s4 = self.addSwitch("wallawal4", dpid="0000000000000006")
        s5 = self.addSwitch("pasco5", dpid="0000000000000007")
        s6 = self.addSwitch("pullman6", dpid="0000000000000008")
        s7 = self.addSwitch("lewiston7", dpid="0000000000000009")
        s8 = self.addSwitch("kennewic8", dpid="000000000000000a")
        s9 = self.addSwitch("yakima9", dpid="000000000000000b")
        s10 = self.addSwitch("ellensbu0", dpid="000000000000000c")
        s11 = self.addSwitch("vancouve1", dpid="000000000000000d")
        s12 = self.addSwitch("bellingh2", dpid="000000000000000e")
        s13 = self.addSwitch("mtvernon3", dpid="000000000000000f")
        s14 = self.addSwitch("everett14", dpid="0000000000000010")
        s15 = self.addSwitch("westins5", dpid="0000000000000011")
        s16 = self.addSwitch("tacoma16", dpid="0000000000000012")
        s17 = self.addSwitch("olympia17", dpid="0000000000000013")
        s18 = self.addSwitch("portland8", dpid="0000000000000014")

        # Adding Links
        self.addLink(s0, s1)
        self.addLink(s0, s2)
        self.addLink(s0, s3)
        self.addLink(s0, s6)
        self.addLink(s2, s10)
        self.addLink(s2, s15)
        self.addLink(s3, s9)
        self.addLink(s4, s8)
        self.addLink(s4, s5)
        self.addLink(s5, s8)
        self.addLink(s5, s9)
        self.addLink(s6, s7)
        self.addLink(s8, s9)
        self.addLink(s8, s18)
        self.addLink(s9, s10)
        self.addLink(s9, s15)
        self.addLink(s11, s12)
        self.addLink(s11, s15)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s15, s18)
        self.addLink(s16, s17)
        self.addLink(s17, s18)


topos = {"Noel": (lambda: Noel())}
