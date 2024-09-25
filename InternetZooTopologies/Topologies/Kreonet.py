#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Kreonet(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        jeonju = self.addSwitch("jeonju", dpid="0000000000000002")
        jeju = self.addSwitch("jeju", dpid="0000000000000003")
        kwangju = self.addSwitch("kwangju", dpid="0000000000000004")
        busan = self.addSwitch("busan", dpid="0000000000000005")
        changwon = self.addSwitch("changwon", dpid="0000000000000006")
        seoul = self.addSwitch("seoul", dpid="0000000000000007")
        incheon = self.addSwitch("incheon", dpid="0000000000000008")
        suwon = self.addSwitch("suwon", dpid="0000000000000009")
        cheonan = self.addSwitch("cheonan", dpid="000000000000000a")
        ochang = self.addSwitch("ochang", dpid="000000000000000b")
        daejeon = self.addSwitch("daejeon", dpid="000000000000000c")
        pohang = self.addSwitch("pohang", dpid="000000000000000d")
        daegu = self.addSwitch("daegu", dpid="000000000000000e")

        # Adding Links
        self.addLink(jeonju, daejeon)
        self.addLink(jeju, kwangju)
        self.addLink(kwangju, daejeon)
        self.addLink(busan, daejeon)
        self.addLink(changwon, daejeon)
        self.addLink(seoul, daejeon)
        self.addLink(seoul, incheon)
        self.addLink(seoul, suwon)
        self.addLink(cheonan, daejeon)
        self.addLink(ochang, daejeon)
        self.addLink(daejeon, pohang)
        self.addLink(daejeon, daegu)


topos = {"Kreonet": (lambda: Kreonet())}
