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
        chugoku = self.addSwitch("chugoku", dpid="0000000000000002")
        kinki = self.addSwitch("kinki", dpid="0000000000000003")
        kyushu = self.addSwitch("kyushu", dpid="0000000000000004")
        shikoku = self.addSwitch("shikoku", dpid="0000000000000005")
        shinetsu = self.addSwitch("shinetsu", dpid="0000000000000006")
        busan = self.addSwitch("busan", dpid="0000000000000007")
        tokai = self.addSwitch("tokai", dpid="0000000000000008")
        hokuriku = self.addSwitch("hokuriku", dpid="0000000000000009")
        hongkong = self.addSwitch("hongkong", dpid="000000000000000a")
        okinawa = self.addSwitch("okinawa", dpid="000000000000000b")
        hokkaido = self.addSwitch("hokkaido", dpid="000000000000000c")
        tohoku = self.addSwitch("tohoku", dpid="000000000000000d")
        tokyo = self.addSwitch("tokyo", dpid="000000000000000e")
        chicago = self.addSwitch("chicago", dpid="000000000000000f")
        losangel = self.addSwitch("losangel", dpid="0000000000000010")
        none = self.addSwitch("none", dpid="0000000000000011")
        singapor = self.addSwitch("singapor", dpid="0000000000000012")
        bangkok = self.addSwitch("bangkok", dpid="0000000000000013")

        # Adding Links
        self.addLink(chugoku, kinki)
        self.addLink(chugoku, kyushu)
        self.addLink(kinki, shikoku)
        self.addLink(kinki, tokai)
        self.addLink(kyushu, okinawa)
        self.addLink(kyushu, busan)
        self.addLink(shinetsu, tokyo)
        self.addLink(tokai, tokyo)
        self.addLink(hokuriku, tokyo)
        self.addLink(hongkong, tokyo)
        self.addLink(hokkaido, tohoku)
        self.addLink(tohoku, tokyo)
        self.addLink(tokyo, none)
        self.addLink(tokyo, singapor)
        self.addLink(tokyo, bangkok)
        self.addLink(chicago, none)
        self.addLink(losangel, none)


topos = {"Jgn2Plus": (lambda: Jgn2Plus())}
