#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Oxford(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("portsmou0", dpid="0000000000000002")
        s1 = self.addSwitch("dover1", dpid="0000000000000003")
        s2 = self.addSwitch("biddefor2", dpid="0000000000000004")
        s3 = self.addSwitch("sanford3", dpid="0000000000000005")
        s4 = self.addSwitch("boston4", dpid="0000000000000006")
        s5 = self.addSwitch("framingh5", dpid="0000000000000007")
        s6 = self.addSwitch("manchest6", dpid="0000000000000008")
        s7 = self.addSwitch("keene7", dpid="0000000000000009")
        s8 = self.addSwitch("worceste8", dpid="000000000000000a")
        s9 = self.addSwitch("springfi9", dpid="000000000000000b")
        s10 = self.addSwitch("bangor10", dpid="000000000000000c")
        s11 = self.addSwitch("portland1", dpid="000000000000000d")
        s12 = self.addSwitch("turner12", dpid="000000000000000e")
        s13 = self.addSwitch("bethel13", dpid="000000000000000f")
        s14 = self.addSwitch("norway14", dpid="0000000000000010")
        s15 = self.addSwitch("standish5", dpid="0000000000000011")
        s16 = self.addSwitch("buckfiel6", dpid="0000000000000012")
        s17 = self.addSwitch("augusta17", dpid="0000000000000013")
        s18 = self.addSwitch("lewiston8", dpid="0000000000000014")
        s19 = self.addSwitch("augusta19", dpid="0000000000000015")

        # Adding Links
        self.addLink(s0, s11)
        self.addLink(s0, s3)
        self.addLink(s0, s6)
        self.addLink(s1, s11)
        self.addLink(s1, s7)
        self.addLink(s2, s11)
        self.addLink(s2, s3)
        self.addLink(s4, s5)
        self.addLink(s4, s6)
        self.addLink(s5, s8)
        self.addLink(s7, s9)
        self.addLink(s8, s9)
        self.addLink(s10, s18)
        self.addLink(s10, s19)
        self.addLink(s11, s18)
        self.addLink(s11, s15)
        self.addLink(s12, s17)
        self.addLink(s12, s13)
        self.addLink(s13, s14)
        self.addLink(s14, s16)
        self.addLink(s14, s15)
        self.addLink(s15, s16)
        self.addLink(s16, s17)
        self.addLink(s17, s18)
        self.addLink(s17, s19)
        self.addLink(s18, s19)


topos = {"Oxford": (lambda: Oxford())}
