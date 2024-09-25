#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Quest(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        auckland2 = self.addSwitch("auckland2", dpid="0000000000000002")
        fiji = self.addSwitch("fiji", dpid="0000000000000003")
        sydney1 = self.addSwitch("sydney1", dpid="0000000000000004")
        auckland1 = self.addSwitch("auckland1", dpid="0000000000000005")
        sacramen = self.addSwitch("sacramen", dpid="0000000000000006")
        losangel = self.addSwitch("losangel", dpid="0000000000000007")
        hawaii1 = self.addSwitch("hawaii1", dpid="0000000000000008")
        hawaii2 = self.addSwitch("hawaii2", dpid="0000000000000009")
        taiwan = self.addSwitch("taiwan", dpid="000000000000000a")
        philippi2 = self.addSwitch("philippi2", dpid="000000000000000b")
        melbourn = self.addSwitch("melbourn", dpid="000000000000000c")
        sydney2 = self.addSwitch("sydney2", dpid="000000000000000d")
        korea = self.addSwitch("korea", dpid="000000000000000e")
        japan = self.addSwitch("japan", dpid="000000000000000f")
        guam = self.addSwitch("guam", dpid="0000000000000010")
        philippi1 = self.addSwitch("philippi1", dpid="0000000000000011")
        hongkong = self.addSwitch("hongkong", dpid="0000000000000012")
        singapor = self.addSwitch("singapor", dpid="0000000000000013")
        thailand = self.addSwitch("thailand", dpid="0000000000000014")
        perth = self.addSwitch("perth", dpid="0000000000000015")

        # Adding Links
        self.addLink(auckland2, sydney2)
        self.addLink(auckland2, auckland1)
        self.addLink(fiji, sydney1)
        self.addLink(fiji, hawaii1)
        self.addLink(sydney1, melbourn)
        self.addLink(sydney1, sydney2)
        self.addLink(sydney1, guam)
        self.addLink(auckland1, hawaii2)
        self.addLink(sacramen, japan)
        self.addLink(sacramen, hawaii1)
        self.addLink(sacramen, losangel)
        self.addLink(losangel, hawaii2)
        self.addLink(hawaii1, japan)
        self.addLink(hawaii1, guam)
        self.addLink(hawaii1, hawaii2)
        self.addLink(taiwan, hongkong)
        self.addLink(taiwan, korea)
        self.addLink(taiwan, philippi1)
        self.addLink(philippi2, hongkong)
        self.addLink(philippi2, guam)
        self.addLink(philippi2, philippi1)
        self.addLink(melbourn, perth)
        self.addLink(korea, japan)
        self.addLink(japan, hongkong)
        self.addLink(japan, guam)
        self.addLink(guam, philippi1)
        self.addLink(guam, singapor)
        self.addLink(philippi1, hongkong)
        self.addLink(hongkong, singapor)
        self.addLink(singapor, thailand)
        self.addLink(singapor, perth)


topos = {"Quest": (lambda: Quest())}
