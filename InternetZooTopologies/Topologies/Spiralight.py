#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Spiralight(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        milwauke = self.addSwitch("milwauke", dpid="0000000000000002")
        rockford = self.addSwitch("rockford", dpid="0000000000000003")
        janesvil = self.addSwitch("janesvil", dpid="0000000000000004")
        waukesha = self.addSwitch("waukesha", dpid="0000000000000005")
        chicago = self.addSwitch("chicago", dpid="0000000000000006")
        madison = self.addSwitch("madison", dpid="0000000000000007")
        campdoug = self.addSwitch("campdoug", dpid="0000000000000008")
        minneaop = self.addSwitch("minneaop", dpid="0000000000000009")
        eauclair = self.addSwitch("eauclair", dpid="000000000000000a")
        wausau = self.addSwitch("wausau", dpid="000000000000000b")
        greenbay = self.addSwitch("greenbay", dpid="000000000000000c")
        appleton = self.addSwitch("appleton", dpid="000000000000000d")
        oshkosh = self.addSwitch("oshkosh", dpid="000000000000000e")
        fondulac = self.addSwitch("fondulac", dpid="000000000000000f")
        beaverda = self.addSwitch("beaverda", dpid="0000000000000010")

        # Adding Links
        self.addLink(milwauke, waukesha)
        self.addLink(milwauke, chicago)
        self.addLink(rockford, janesvil)
        self.addLink(rockford, chicago)
        self.addLink(janesvil, madison)
        self.addLink(waukesha, madison)
        self.addLink(madison, campdoug)
        self.addLink(madison, beaverda)
        self.addLink(campdoug, eauclair)
        self.addLink(minneaop, eauclair)
        self.addLink(minneaop, wausau)
        self.addLink(wausau, greenbay)
        self.addLink(greenbay, appleton)
        self.addLink(appleton, oshkosh)
        self.addLink(oshkosh, fondulac)
        self.addLink(fondulac, beaverda)


topos = {"Spiralight": (lambda: Spiralight())}
