#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class JanetExternal(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("heanet0", dpid="0000000000000002")
        s1 = self.addSwitch("europeg1", dpid="0000000000000003")
        s2 = self.addSwitch("peoples2", dpid="0000000000000004")
        s3 = self.addSwitch("japanni3", dpid="0000000000000005")
        s4 = self.addSwitch("belfast4", dpid="0000000000000006")
        s5 = self.addSwitch("janet5", dpid="0000000000000007")
        s6 = self.addSwitch("usresear6", dpid="0000000000000008")
        s7 = self.addSwitch("usresear7", dpid="0000000000000009")
        s8 = self.addSwitch("linx8", dpid="000000000000000a")
        s9 = self.addSwitch("ukisps9", dpid="000000000000000b")
        s10 = self.addSwitch("privatep0", dpid="000000000000000c")
        s11 = self.addSwitch("globaltr1", dpid="000000000000000d")

        # Adding Links
        self.addLink(s0, s4)
        self.addLink(s1, s2)
        self.addLink(s1, s3)
        self.addLink(s1, s5)
        self.addLink(s1, s6)
        self.addLink(s1, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s10)
        self.addLink(s5, s11)
        self.addLink(s8, s9)


topos = {"JanetExternal": (lambda: JanetExternal())}
