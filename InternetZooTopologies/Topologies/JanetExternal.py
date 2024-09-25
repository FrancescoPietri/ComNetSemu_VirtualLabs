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
        heanet = self.addSwitch("heanet", dpid="0000000000000002")
        europeg = self.addSwitch("europeg", dpid="0000000000000003")
        peoples = self.addSwitch("peoples", dpid="0000000000000004")
        japanni = self.addSwitch("japanni", dpid="0000000000000005")
        belfast = self.addSwitch("belfast", dpid="0000000000000006")
        janet = self.addSwitch("janet", dpid="0000000000000007")
        usresear = self.addSwitch("usresear", dpid="0000000000000008")
        usresear = self.addSwitch("usresear", dpid="0000000000000009")
        linx = self.addSwitch("linx", dpid="000000000000000a")
        ukisps = self.addSwitch("ukisps", dpid="000000000000000b")
        privatep = self.addSwitch("privatep", dpid="000000000000000c")
        globaltr = self.addSwitch("globaltr", dpid="000000000000000d")

        # Adding Links
        self.addLink(heanet, belfast)
        self.addLink(europeg, peoples)
        self.addLink(europeg, japanni)
        self.addLink(europeg, janet)
        self.addLink(europeg, usresear)
        self.addLink(europeg, usresear)
        self.addLink(janet, linx)
        self.addLink(janet, privatep)
        self.addLink(janet, globaltr)
        self.addLink(linx, ukisps)


topos = {"JanetExternal": (lambda: JanetExternal())}
