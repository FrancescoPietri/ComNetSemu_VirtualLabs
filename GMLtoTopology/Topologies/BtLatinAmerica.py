#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class BtLatinAmerica(Topo):
    def __init__(self):
        Topo.__init__(self)
        # Adding Switches
        s0 = self.addSwitch("s0", dpid="0000000000000002")
        s1 = self.addSwitch("s1", dpid="0000000000000003")
        s2 = self.addSwitch("s2", dpid="0000000000000004")
        s3 = self.addSwitch("s3", dpid="0000000000000005")
        s4 = self.addSwitch("s4", dpid="0000000000000006")
        s5 = self.addSwitch("s5", dpid="0000000000000007")
        s6 = self.addSwitch("s6", dpid="0000000000000008")
        s7 = self.addSwitch("s7", dpid="0000000000000009")
        s8 = self.addSwitch("s8", dpid="000000000000000a")
        s9 = self.addSwitch("s9", dpid="000000000000000b")
        s10 = self.addSwitch("s10", dpid="000000000000000c")
        s11 = self.addSwitch("s11", dpid="000000000000000d")
        s12 = self.addSwitch("s12", dpid="000000000000000e")
        s13 = self.addSwitch("s13", dpid="000000000000000f")
        s14 = self.addSwitch("s14", dpid="0000000000000010")
        s15 = self.addSwitch("s15", dpid="0000000000000011")
        s16 = self.addSwitch("s16", dpid="0000000000000012")
        s17 = self.addSwitch("s17", dpid="0000000000000013")
        s18 = self.addSwitch("s18", dpid="0000000000000014")
        s19 = self.addSwitch("s19", dpid="0000000000000015")
        s20 = self.addSwitch("s20", dpid="0000000000000016")
        s21 = self.addSwitch("s21", dpid="0000000000000017")
        s22 = self.addSwitch("s22", dpid="0000000000000018")
        s23 = self.addSwitch("s23", dpid="0000000000000019")
        s24 = self.addSwitch("s24", dpid="000000000000001a")
        s25 = self.addSwitch("s25", dpid="000000000000001b")
        s26 = self.addSwitch("s26", dpid="000000000000001c")
        s27 = self.addSwitch("s27", dpid="000000000000001d")
        s28 = self.addSwitch("s28", dpid="000000000000001e")
        s29 = self.addSwitch("s29", dpid="000000000000001f")
        s30 = self.addSwitch("s30", dpid="0000000000000020")
        s31 = self.addSwitch("s31", dpid="0000000000000021")
        s32 = self.addSwitch("s32", dpid="0000000000000022")
        s33 = self.addSwitch("s33", dpid="0000000000000023")
        s34 = self.addSwitch("s34", dpid="0000000000000024")
        s35 = self.addSwitch("s35", dpid="0000000000000025")
        s36 = self.addSwitch("s36", dpid="0000000000000026")
        s37 = self.addSwitch("s37", dpid="0000000000000027")
        s38 = self.addSwitch("s38", dpid="0000000000000028")
        s39 = self.addSwitch("s39", dpid="0000000000000029")
        s40 = self.addSwitch("s40", dpid="000000000000002a")
        s41 = self.addSwitch("s41", dpid="000000000000002b")
        s42 = self.addSwitch("s42", dpid="000000000000002c")
        s43 = self.addSwitch("s43", dpid="000000000000002d")
        s44 = self.addSwitch("s44", dpid="000000000000002e")
        s45 = self.addSwitch("s45", dpid="000000000000002f")
        s46 = self.addSwitch("s46", dpid="0000000000000030")
        s47 = self.addSwitch("s47", dpid="0000000000000031")
        s48 = self.addSwitch("s48", dpid="0000000000000032")
        s49 = self.addSwitch("s49", dpid="0000000000000033")
        s50 = self.addSwitch("s50", dpid="0000000000000034")

        # Adding Links
        link0_conf = {
            "delay": "20ms",
            "use_tbf": True,
            "bw": 20,
            "max_queue_size": 10,
            "burst": 1000000,
        }
        link1_conf = {
            "delay": "25ms",
            "use_tbf": True,
            "bw": 50,
            "max_queue_size": 10,
            "burst": 1000000,
        }
        self.addLink(s0, s46, **link1_conf)
        self.addLink(s1, s22, **link0_conf)
        self.addLink(s1, s46, **link0_conf)
        self.addLink(s1, s7, **link1_conf)
        self.addLink(s2, s42, **link1_conf)
        self.addLink(s2, s3, **link0_conf)
        self.addLink(s2, s29, **link1_conf)
        self.addLink(s4, s5, **link0_conf)
        self.addLink(s4, s7, **link0_conf)
        self.addLink(s6, s8, **link1_conf)
        self.addLink(s6, s22, **link0_conf)
        self.addLink(s6, s47, **link0_conf)
        self.addLink(s7, s43, **link1_conf)
        self.addLink(s8, s48, **link1_conf)
        self.addLink(s9, s21, **link1_conf)
        self.addLink(s10, s37, **link0_conf)
        self.addLink(s10, s23, **link1_conf)
        self.addLink(s11, s20, **link1_conf)
        self.addLink(s12, s19, **link1_conf)
        self.addLink(s13, s37, **link0_conf)
        self.addLink(s13, s31, **link0_conf)
        self.addLink(s17, s18, **link0_conf)
        self.addLink(s18, s19, **link1_conf)
        self.addLink(s19, s24, **link0_conf)
        self.addLink(s19, s20, **link1_conf)
        self.addLink(s21, s36, **link0_conf)
        self.addLink(s22, s45, **link0_conf)
        self.addLink(s23, s37, **link1_conf)
        self.addLink(s23, s40, **link1_conf)
        self.addLink(s23, s24, **link0_conf)
        self.addLink(s23, s29, **link0_conf)
        self.addLink(s23, s31, **link1_conf)
        self.addLink(s25, s26, **link1_conf)
        self.addLink(s25, s28, **link0_conf)
        self.addLink(s27, s28, **link0_conf)
        self.addLink(s27, s30, **link1_conf)
        self.addLink(s29, s41, **link1_conf)
        self.addLink(s29, s50, **link1_conf)
        self.addLink(s29, s46, **link0_conf)
        self.addLink(s30, s37, **link0_conf)
        self.addLink(s33, s40, **link0_conf)
        self.addLink(s33, s34, **link1_conf)
        self.addLink(s33, s35, **link0_conf)
        self.addLink(s34, s35, **link1_conf)
        self.addLink(s35, s36, **link1_conf)
        self.addLink(s41, s50, **link0_conf)
        self.addLink(s41, s47, **link0_conf)
        self.addLink(s43, s44, **link1_conf)
        self.addLink(s46, s48, **link0_conf)
        self.addLink(s49, s50, **link1_conf)


topos = {"BtLatinAmerica": (lambda: BtLatinAmerica())}
