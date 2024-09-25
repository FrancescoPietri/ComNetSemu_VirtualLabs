#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Evolink(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("shumen0", dpid="0000000000000002")
        s1 = self.addSwitch("silistra1", dpid="0000000000000003")
        s2 = self.addSwitch("razgrad2", dpid="0000000000000004")
        s3 = self.addSwitch("turgovis3", dpid="0000000000000005")
        s4 = self.addSwitch("yambol4", dpid="0000000000000006")
        s5 = self.addSwitch("sliven5", dpid="0000000000000007")
        s6 = self.addSwitch("dobrich6", dpid="0000000000000008")
        s7 = self.addSwitch("burgas7", dpid="0000000000000009")
        s8 = self.addSwitch("stzagora8", dpid="000000000000000a")
        s9 = self.addSwitch("gabrovo9", dpid="000000000000000b")
        s10 = self.addSwitch("kurjiali0", dpid="000000000000000c")
        s11 = self.addSwitch("varna11", dpid="000000000000000d")
        s12 = self.addSwitch("plovdiv12", dpid="000000000000000e")
        s13 = self.addSwitch("frankfur3", dpid="000000000000000f")
        s14 = self.addSwitch("sofia14", dpid="0000000000000010")
        s15 = self.addSwitch("istanbul5", dpid="0000000000000011")
        s16 = self.addSwitch("kapandre6", dpid="0000000000000012")
        s17 = self.addSwitch("haskovo17", dpid="0000000000000013")
        s18 = self.addSwitch("karlovo18", dpid="0000000000000014")
        s19 = self.addSwitch("kiustend9", dpid="0000000000000015")
        s20 = self.addSwitch("pennik20", dpid="0000000000000016")
        s21 = self.addSwitch("sevlievo1", dpid="0000000000000017")
        s22 = self.addSwitch("vturnovo2", dpid="0000000000000018")
        s23 = self.addSwitch("pazardji3", dpid="0000000000000019")
        s24 = self.addSwitch("smolian24", dpid="000000000000001a")
        s25 = self.addSwitch("petrich25", dpid="000000000000001b")
        s26 = self.addSwitch("blagoevg6", dpid="000000000000001c")
        s27 = self.addSwitch("buchares7", dpid="000000000000001d")
        s28 = self.addSwitch("ruse28", dpid="000000000000001e")
        s29 = self.addSwitch("amsterda9", dpid="000000000000001f")
        s30 = self.addSwitch("vidin30", dpid="0000000000000020")
        s31 = self.addSwitch("kozloduj1", dpid="0000000000000021")
        s32 = self.addSwitch("montana32", dpid="0000000000000022")
        s33 = self.addSwitch("vraca33", dpid="0000000000000023")
        s34 = self.addSwitch("pleven34", dpid="0000000000000024")
        s35 = self.addSwitch("lovech35", dpid="0000000000000025")
        s36 = self.addSwitch("skopie36", dpid="0000000000000026")

        # Adding Links
        self.addLink(s0, s3)
        self.addLink(s0, s6)
        self.addLink(s1, s6)
        self.addLink(s2, s3)
        self.addLink(s2, s28)
        self.addLink(s4, s5)
        self.addLink(s4, s7)
        self.addLink(s5, s8)
        self.addLink(s6, s11)
        self.addLink(s7, s11)
        self.addLink(s7, s14)
        self.addLink(s8, s17)
        self.addLink(s8, s12)
        self.addLink(s8, s14)
        self.addLink(s8, s9)
        self.addLink(s10, s17)
        self.addLink(s11, s27)
        self.addLink(s11, s14)
        self.addLink(s12, s14)
        self.addLink(s12, s16)
        self.addLink(s12, s17)
        self.addLink(s12, s23)
        self.addLink(s12, s24)
        self.addLink(s13, s27)
        self.addLink(s13, s29)
        self.addLink(s13, s14)
        self.addLink(s14, s33)
        self.addLink(s14, s36)
        self.addLink(s14, s18)
        self.addLink(s14, s19)
        self.addLink(s14, s20)
        self.addLink(s14, s21)
        self.addLink(s14, s23)
        self.addLink(s14, s26)
        self.addLink(s14, s27)
        self.addLink(s14, s29)
        self.addLink(s15, s16)
        self.addLink(s22, s35)
        self.addLink(s22, s28)
        self.addLink(s25, s26)
        self.addLink(s30, s32)
        self.addLink(s31, s32)
        self.addLink(s32, s33)
        self.addLink(s32, s34)
        self.addLink(s34, s35)


topos = {"Evolink": (lambda: Evolink())}
