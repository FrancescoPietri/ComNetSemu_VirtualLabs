#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Karen(Topo):
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
        link2_conf = {
            "bw": 3.0,
            "delay": 3.0,
            "jitter": 3.0,
            "loss": 3.0,
            "gro": False,
            "txo": True,
            "rxo": True,
            "speedup": 0,
            "use_hfsc": False,
            "use_tbf": False,
            "latency_ms": 33.0,
            "enable_ecn": False,
            "enable_red": False,
            "max_queue_size": 3,
        }
        link3_conf = {
            "bw": 3.0,
            "delay": None,
            "jitter": None,
            "loss": None,
            "gro": False,
            "txo": True,
            "rxo": True,
            "speedup": 0,
            "use_hfsc": False,
            "use_tbf": False,
            "latency_ms": 33.0,
            "enable_ecn": False,
            "enable_red": False,
            "max_queue_size": 3,
        }
        self.addLink(s0, s1, **link1_conf)
        self.addLink(s0, s2, **link1_conf)
        self.addLink(s0, s3, **link1_conf)
        self.addLink(s0, s5, **link3_conf)
        self.addLink(s0, s9, **link3_conf)
        self.addLink(s1, s4, **link1_conf)
        self.addLink(s1, s6, **link0_conf)
        self.addLink(s1, s7, **link1_conf)
        self.addLink(s2, s20, **link1_conf)
        self.addLink(s2, s14, **link1_conf)
        self.addLink(s3, s24, **link1_conf)
        self.addLink(s3, s12, **link2_conf)
        self.addLink(s3, s13, **link1_conf)
        self.addLink(s3, s14, **link3_conf)
        self.addLink(s4, s5, **link3_conf)
        self.addLink(s5, s8, **link0_conf)
        self.addLink(s5, s9, **link2_conf)
        self.addLink(s10, s24, **link3_conf)
        self.addLink(s11, s24, **link2_conf)
        self.addLink(s14, s21, **link1_conf)
        self.addLink(s15, s16, **link1_conf)
        self.addLink(s15, s24, **link3_conf)
        self.addLink(s17, s24, **link1_conf)
        self.addLink(s18, s22, **link2_conf)
        self.addLink(s19, s21, **link0_conf)
        self.addLink(s21, s22, **link2_conf)
        self.addLink(s22, s23, **link0_conf)
        self.addLink(s23, s24, **link3_conf)


topos = {"Karen": (lambda: Karen())}
