#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Uran(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        kherson = self.addSwitch("kherson", dpid="0000000000000002")
        mykolaiv = self.addSwitch("mykolaiv", dpid="0000000000000003")
        sevastop = self.addSwitch("sevastop", dpid="0000000000000004")
        simferop = self.addSwitch("simferop", dpid="0000000000000005")
        vinnitsa = self.addSwitch("vinnitsa", dpid="0000000000000006")
        khmelnit = self.addSwitch("khmelnit", dpid="0000000000000007")
        odessa = self.addSwitch("odessa", dpid="0000000000000008")
        kamianet = self.addSwitch("kamianet", dpid="0000000000000009")
        frankfur = self.addSwitch("frankfur", dpid="000000000000000a")
        poznang = self.addSwitch("poznang", dpid="000000000000000b")
        cherkass = self.addSwitch("cherkass", dpid="000000000000000c")
        odessai = self.addSwitch("odessai", dpid="000000000000000d")
        kharkiv = self.addSwitch("kharkiv", dpid="000000000000000e")
        uaix = self.addSwitch("uaix", dpid="000000000000000f")
        zaporizh = self.addSwitch("zaporizh", dpid="0000000000000010")
        dniprope = self.addSwitch("dniprope", dpid="0000000000000011")
        lviv = self.addSwitch("lviv", dpid="0000000000000012")
        lutsk = self.addSwitch("lutsk", dpid="0000000000000013")
        zhitomir = self.addSwitch("zhitomir", dpid="0000000000000014")
        kiev = self.addSwitch("kiev", dpid="0000000000000015")
        pereyasl = self.addSwitch("pereyasl", dpid="0000000000000016")
        poltava = self.addSwitch("poltava", dpid="0000000000000017")
        kharkiv = self.addSwitch("kharkiv", dpid="0000000000000018")
        donetsk = self.addSwitch("donetsk", dpid="0000000000000019")

        # Adding Links
        self.addLink(kherson, mykolaiv)
        self.addLink(kherson, simferop)
        self.addLink(mykolaiv, cherkass)
        self.addLink(mykolaiv, odessa)
        self.addLink(sevastop, simferop)
        self.addLink(vinnitsa, kiev)
        self.addLink(vinnitsa, khmelnit)
        self.addLink(khmelnit, lviv)
        self.addLink(odessa, odessai)
        self.addLink(kamianet, kiev)
        self.addLink(frankfur, kiev)
        self.addLink(poznang, lviv)
        self.addLink(cherkass, kiev)
        self.addLink(kharkiv, kharkiv)
        self.addLink(uaix, kiev)
        self.addLink(zaporizh, dniprope)
        self.addLink(dniprope, poltava)
        self.addLink(dniprope, donetsk)
        self.addLink(lviv, kiev)
        self.addLink(lutsk, zhitomir)
        self.addLink(zhitomir, kiev)
        self.addLink(kiev, pereyasl)
        self.addLink(kiev, poltava)
        self.addLink(poltava, kharkiv)


topos = {"Uran": (lambda: Uran())}
