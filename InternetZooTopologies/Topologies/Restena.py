#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Restena(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("walferda0", dpid="0000000000000002")
        s1 = self.addSwitch("ccrn1", dpid="0000000000000003")
        s2 = self.addSwitch("ettelbru2", dpid="0000000000000004")
        s3 = self.addSwitch("diekirch3", dpid="0000000000000005")
        s4 = self.addSwitch("geantpar4", dpid="0000000000000006")
        s5 = self.addSwitch("internet5", dpid="0000000000000007")
        s6 = self.addSwitch("adslvia6", dpid="0000000000000008")
        s7 = self.addSwitch("france7", dpid="0000000000000009")
        s8 = self.addSwitch("geantfra8", dpid="000000000000000a")
        s9 = self.addSwitch("restena9", dpid="000000000000000b")
        s10 = self.addSwitch("bce10", dpid="000000000000000c")
        s11 = self.addSwitch("adslvia1", dpid="000000000000000d")
        s12 = self.addSwitch("uniiu12", dpid="000000000000000e")
        s13 = self.addSwitch("rollinge3", dpid="000000000000000f")
        s14 = self.addSwitch("campusge4", dpid="0000000000000010")
        s15 = self.addSwitch("eschsur5", dpid="0000000000000011")
        s16 = self.addSwitch("bettembo6", dpid="0000000000000012")
        s17 = self.addSwitch("luxembou7", dpid="0000000000000013")
        s18 = self.addSwitch("limperts8", dpid="0000000000000014")

        # Adding Links
        self.addLink(s0, s9)
        self.addLink(s1, s9)
        self.addLink(s2, s10)
        self.addLink(s2, s3)
        self.addLink(s3, s9)
        self.addLink(s4, s10)
        self.addLink(s5, s10)
        self.addLink(s6, s9)
        self.addLink(s7, s15)
        self.addLink(s8, s10)
        self.addLink(s9, s10)
        self.addLink(s9, s16)
        self.addLink(s9, s17)
        self.addLink(s10, s11)
        self.addLink(s10, s18)
        self.addLink(s12, s18)
        self.addLink(s12, s14)
        self.addLink(s13, s14)
        self.addLink(s14, s17)
        self.addLink(s14, s15)
        self.addLink(s15, s16)


topos = {"Restena": (lambda: Restena())}
