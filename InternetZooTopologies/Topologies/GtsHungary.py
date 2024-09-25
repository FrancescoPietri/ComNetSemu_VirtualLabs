#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class GtsHungary(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("none0", dpid="0000000000000002")
        s1 = self.addSwitch("miskolc1", dpid="0000000000000003")
        s2 = self.addSwitch("salgotar2", dpid="0000000000000004")
        s3 = self.addSwitch("godollo3", dpid="0000000000000005")
        s4 = self.addSwitch("szolnok4", dpid="0000000000000006")
        s5 = self.addSwitch("dunaujva5", dpid="0000000000000007")
        s6 = self.addSwitch("nyiregyh6", dpid="0000000000000008")
        s7 = self.addSwitch("debrecen7", dpid="0000000000000009")
        s8 = self.addSwitch("kecskeme8", dpid="000000000000000a")
        s9 = self.addSwitch("baja9", dpid="000000000000000b")
        s10 = self.addSwitch("pecs10", dpid="000000000000000c")
        s11 = self.addSwitch("none11", dpid="000000000000000d")
        s12 = self.addSwitch("szeged12", dpid="000000000000000e")
        s13 = self.addSwitch("siofok13", dpid="000000000000000f")
        s14 = self.addSwitch("kaposvar4", dpid="0000000000000010")
        s15 = self.addSwitch("szekszar5", dpid="0000000000000011")
        s16 = self.addSwitch("none16", dpid="0000000000000012")
        s17 = self.addSwitch("vienna17", dpid="0000000000000013")
        s18 = self.addSwitch("bratisla8", dpid="0000000000000014")
        s19 = self.addSwitch("bekescsa9", dpid="0000000000000015")
        s20 = self.addSwitch("budapest0", dpid="0000000000000016")
        s21 = self.addSwitch("vac21", dpid="0000000000000017")
        s22 = self.addSwitch("sopron22", dpid="0000000000000018")
        s23 = self.addSwitch("szombath3", dpid="0000000000000019")
        s24 = self.addSwitch("zalaeger4", dpid="000000000000001a")
        s25 = self.addSwitch("nagykani5", dpid="000000000000001b")
        s26 = self.addSwitch("szekesfe6", dpid="000000000000001c")
        s27 = self.addSwitch("veszprem7", dpid="000000000000001d")
        s28 = self.addSwitch("gyor28", dpid="000000000000001e")
        s29 = self.addSwitch("tatabany9", dpid="000000000000001f")

        # Adding Links
        self.addLink(s0, s20)
        self.addLink(s1, s20)
        self.addLink(s2, s20)
        self.addLink(s3, s20)
        self.addLink(s4, s20)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s5, s20)
        self.addLink(s6, s20)
        self.addLink(s7, s12)
        self.addLink(s8, s12)
        self.addLink(s9, s20)
        self.addLink(s10, s20)
        self.addLink(s11, s12)
        self.addLink(s12, s19)
        self.addLink(s13, s20)
        self.addLink(s14, s20)
        self.addLink(s15, s20)
        self.addLink(s16, s20)
        self.addLink(s17, s22)
        self.addLink(s18, s28)
        self.addLink(s20, s21)
        self.addLink(s20, s25)
        self.addLink(s20, s26)
        self.addLink(s20, s29)
        self.addLink(s22, s28)
        self.addLink(s22, s23)
        self.addLink(s23, s24)
        self.addLink(s24, s27)
        self.addLink(s26, s27)
        self.addLink(s28, s29)


topos = {"GtsHungary": (lambda: GtsHungary())}
