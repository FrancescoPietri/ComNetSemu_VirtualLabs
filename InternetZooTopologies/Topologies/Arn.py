#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Arn(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("djelfa0", dpid="0000000000000002")
        s1 = self.addSwitch("medea1", dpid="0000000000000003")
        s2 = self.addSwitch("internet2", dpid="0000000000000004")
        s3 = self.addSwitch("blida3", dpid="0000000000000005")
        s4 = self.addSwitch("eloued4", dpid="0000000000000006")
        s5 = self.addSwitch("msila5", dpid="0000000000000007")
        s6 = self.addSwitch("laghouat6", dpid="0000000000000008")
        s7 = self.addSwitch("ouargla7", dpid="0000000000000009")
        s8 = self.addSwitch("constant8", dpid="000000000000000a")
        s9 = self.addSwitch("biskra9", dpid="000000000000000b")
        s10 = self.addSwitch("batna10", dpid="000000000000000c")
        s11 = self.addSwitch("tiziouzo1", dpid="000000000000000d")
        s12 = self.addSwitch("annaba12", dpid="000000000000000e")
        s13 = self.addSwitch("guelma13", dpid="000000000000000f")
        s14 = self.addSwitch("tebessa14", dpid="0000000000000010")
        s15 = self.addSwitch("oumelbou5", dpid="0000000000000011")
        s16 = self.addSwitch("bejaia16", dpid="0000000000000012")
        s17 = self.addSwitch("setif17", dpid="0000000000000013")
        s18 = self.addSwitch("skikda18", dpid="0000000000000014")
        s19 = self.addSwitch("jijel19", dpid="0000000000000015")
        s20 = self.addSwitch("tiaret20", dpid="0000000000000016")
        s21 = self.addSwitch("geant21", dpid="0000000000000017")
        s22 = self.addSwitch("alger22", dpid="0000000000000018")
        s23 = self.addSwitch("chlef23", dpid="0000000000000019")
        s24 = self.addSwitch("oran24", dpid="000000000000001a")
        s25 = self.addSwitch("mostagan5", dpid="000000000000001b")
        s26 = self.addSwitch("tlemcen26", dpid="000000000000001c")
        s27 = self.addSwitch("sidibela7", dpid="000000000000001d")
        s28 = self.addSwitch("saida28", dpid="000000000000001e")
        s29 = self.addSwitch("mascara29", dpid="000000000000001f")

        # Adding Links
        self.addLink(s0, s22)
        self.addLink(s1, s22)
        self.addLink(s2, s22)
        self.addLink(s3, s22)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s7)
        self.addLink(s7, s22)
        self.addLink(s8, s9)
        self.addLink(s8, s10)
        self.addLink(s8, s12)
        self.addLink(s8, s13)
        self.addLink(s8, s14)
        self.addLink(s8, s15)
        self.addLink(s8, s18)
        self.addLink(s8, s19)
        self.addLink(s8, s22)
        self.addLink(s11, s22)
        self.addLink(s16, s22)
        self.addLink(s17, s22)
        self.addLink(s20, s24)
        self.addLink(s21, s22)
        self.addLink(s22, s23)
        self.addLink(s22, s24)
        self.addLink(s24, s25)
        self.addLink(s24, s26)
        self.addLink(s24, s27)
        self.addLink(s24, s28)
        self.addLink(s24, s29)


topos = {"Arn": (lambda: Arn())}
