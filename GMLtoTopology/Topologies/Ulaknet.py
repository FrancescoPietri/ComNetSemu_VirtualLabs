#!/usr/bin/python
# 82
from mininet.node import Host
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ulaknet(Topo):
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
        s51 = self.addSwitch("s51", dpid="0000000000000035")
        s52 = self.addSwitch("s52", dpid="0000000000000036")
        s53 = self.addSwitch("s53", dpid="0000000000000037")
        s54 = self.addSwitch("s54", dpid="0000000000000038")
        s55 = self.addSwitch("s55", dpid="0000000000000039")
        s56 = self.addSwitch("s56", dpid="000000000000003a")
        s57 = self.addSwitch("s57", dpid="000000000000003b")
        s58 = self.addSwitch("s58", dpid="000000000000003c")
        s59 = self.addSwitch("s59", dpid="000000000000003d")
        s60 = self.addSwitch("s60", dpid="000000000000003e")
        s61 = self.addSwitch("s61", dpid="000000000000003f")
        s62 = self.addSwitch("s62", dpid="0000000000000040")
        s63 = self.addSwitch("s63", dpid="0000000000000041")
        s64 = self.addSwitch("s64", dpid="0000000000000042")
        s65 = self.addSwitch("s65", dpid="0000000000000043")
        s66 = self.addSwitch("s66", dpid="0000000000000044")
        s67 = self.addSwitch("s67", dpid="0000000000000045")
        s68 = self.addSwitch("s68", dpid="0000000000000046")
        s69 = self.addSwitch("s69", dpid="0000000000000047")
        s70 = self.addSwitch("s70", dpid="0000000000000048")
        s71 = self.addSwitch("s71", dpid="0000000000000049")
        s72 = self.addSwitch("s72", dpid="000000000000004a")
        s73 = self.addSwitch("s73", dpid="000000000000004b")
        s74 = self.addSwitch("s74", dpid="000000000000004c")
        s75 = self.addSwitch("s75", dpid="000000000000004d")
        s76 = self.addSwitch("s76", dpid="000000000000004e")
        s77 = self.addSwitch("s77", dpid="000000000000004f")
        s78 = self.addSwitch("s78", dpid="0000000000000050")
        s79 = self.addSwitch("s79", dpid="0000000000000051")
        s80 = self.addSwitch("s80", dpid="0000000000000052")
        s81 = self.addSwitch("s81", dpid="0000000000000053")

        # Adding Links
        link0_conf = {
            "bw": 100.0,
            "delay": "1ms",
            "jitter": "0ms",
            "loss": None,
            "gro": False,
            "txo": True,
            "rxo": True,
            "speedup": 0,
            "use_hfsc": False,
            "use_tbf": False,
            "latency_ms": None,
            "enable_ecn": False,
            "enable_red": False,
            "max_queue_size": None,
        }
        link1_conf = {
            "bw": 100.0,
            "delay": "5ms",
            "jitter": "0ms",
            "loss": None,
            "gro": False,
            "txo": True,
            "rxo": True,
            "speedup": 0,
            "use_hfsc": False,
            "use_tbf": False,
            "latency_ms": None,
            "enable_ecn": False,
            "enable_red": False,
            "max_queue_size": None,
        }
        link2_conf = {
            "bw": 100.0,
            "delay": "10ms",
            "jitter": "0ms",
            "loss": None,
            "gro": False,
            "txo": True,
            "rxo": True,
            "speedup": 0,
            "use_hfsc": False,
            "use_tbf": False,
            "latency_ms": None,
            "enable_ecn": False,
            "enable_red": False,
            "max_queue_size": None,
        }
        self.addLink(s0, s75, **link0_conf)
        self.addLink(s1, s75, **link2_conf)
        self.addLink(s2, s75, **link2_conf)
        self.addLink(s3, s75, **link0_conf)
        self.addLink(s4, s76, **link1_conf)
        self.addLink(s5, s76, **link1_conf)
        self.addLink(s6, s75, **link2_conf)
        self.addLink(s7, s76, **link2_conf)
        self.addLink(s8, s76, **link2_conf)
        self.addLink(s9, s76, **link1_conf)
        self.addLink(s10, s76, **link1_conf)
        self.addLink(s11, s74, **link0_conf)
        self.addLink(s12, s76, **link1_conf)
        self.addLink(s13, s76, **link1_conf)
        self.addLink(s14, s76, **link1_conf)
        self.addLink(s15, s76, **link1_conf)
        self.addLink(s16, s76, **link1_conf)
        self.addLink(s17, s76, **link2_conf)
        self.addLink(s18, s76, **link1_conf)
        self.addLink(s19, s76, **link2_conf)
        self.addLink(s20, s76, **link0_conf)
        self.addLink(s21, s76, **link2_conf)
        self.addLink(s22, s76, **link0_conf)
        self.addLink(s23, s76, **link1_conf)
        self.addLink(s24, s76, **link0_conf)
        self.addLink(s25, s76, **link0_conf)
        self.addLink(s26, s76, **link2_conf)
        self.addLink(s27, s76, **link0_conf)
        self.addLink(s28, s74, **link2_conf)
        self.addLink(s29, s76, **link1_conf)
        self.addLink(s30, s76, **link2_conf)
        self.addLink(s31, s76, **link1_conf)
        self.addLink(s32, s76, **link0_conf)
        self.addLink(s33, s76, **link1_conf)
        self.addLink(s34, s76, **link2_conf)
        self.addLink(s34, s39, **link0_conf)
        self.addLink(s35, s76, **link0_conf)
        self.addLink(s36, s76, **link2_conf)
        self.addLink(s37, s49, **link2_conf)
        self.addLink(s38, s72, **link0_conf)
        self.addLink(s40, s44, **link1_conf)
        self.addLink(s41, s76, **link2_conf)
        self.addLink(s42, s76, **link0_conf)
        self.addLink(s43, s76, **link0_conf)
        self.addLink(s44, s76, **link0_conf)
        self.addLink(s45, s76, **link2_conf)
        self.addLink(s46, s76, **link1_conf)
        self.addLink(s47, s76, **link1_conf)
        self.addLink(s48, s76, **link1_conf)
        self.addLink(s49, s76, **link0_conf)
        self.addLink(s50, s76, **link0_conf)
        self.addLink(s51, s74, **link2_conf)
        self.addLink(s52, s76, **link2_conf)
        self.addLink(s53, s76, **link0_conf)
        self.addLink(s54, s76, **link2_conf)
        self.addLink(s55, s76, **link0_conf)
        self.addLink(s56, s76, **link0_conf)
        self.addLink(s57, s74, **link0_conf)
        self.addLink(s58, s74, **link0_conf)
        self.addLink(s59, s76, **link0_conf)
        self.addLink(s60, s74, **link1_conf)
        self.addLink(s61, s76, **link0_conf)
        self.addLink(s62, s76, **link0_conf)
        self.addLink(s63, s76, **link0_conf)
        self.addLink(s64, s76, **link1_conf)
        self.addLink(s65, s76, **link0_conf)
        self.addLink(s66, s76, **link0_conf)
        self.addLink(s67, s74, **link1_conf)
        self.addLink(s68, s76, **link1_conf)
        self.addLink(s69, s76, **link1_conf)
        self.addLink(s70, s75, **link1_conf)
        self.addLink(s71, s75, **link0_conf)
        self.addLink(s72, s76, **link1_conf)
        self.addLink(s73, s76, **link1_conf)
        self.addLink(s74, s76, **link1_conf)
        self.addLink(s74, s77, **link0_conf)
        self.addLink(s74, s78, **link0_conf)
        self.addLink(s74, s79, **link0_conf)
        self.addLink(s74, s80, **link2_conf)
        self.addLink(s74, s75, **link1_conf)
        self.addLink(s75, s76, **link1_conf)
        self.addLink(s75, s81, **link2_conf)


topos = {"Ulaknet": (lambda: Ulaknet())}
