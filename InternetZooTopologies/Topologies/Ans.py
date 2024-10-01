#!/usr/bin/python
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink


class Ans(Topo):
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
            "bw": 2.0,
            "delay": 2.0,
            "jitter": None,
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
        link3_conf = {
            "bw": 2.0,
            "delay": 2.0,
            "jitter": 67.0,
            "loss": 24.0,
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
        self.addLink(s0, s1, **link3_conf)
        self.addLink(s0, s3, **link2_conf)
        self.addLink(s1, s3, **link2_conf)
        self.addLink(s1, s6, **link1_conf)
        self.addLink(s1, s7, **link2_conf)
        self.addLink(s2, s3, **link1_conf)
        self.addLink(s2, s9, **link3_conf)
        self.addLink(s2, s11, **link1_conf)
        self.addLink(s4, s5, **link2_conf)
        self.addLink(s4, s6, **link3_conf)
        self.addLink(s5, s17, **link0_conf)
        self.addLink(s6, s7, **link2_conf)
        self.addLink(s7, s8, **link0_conf)
        self.addLink(s7, s9, **link1_conf)
        self.addLink(s8, s9, **link0_conf)
        self.addLink(s8, s13, **link0_conf)
        self.addLink(s8, s17, **link0_conf)
        self.addLink(s10, s11, **link1_conf)
        self.addLink(s10, s12, **link1_conf)
        self.addLink(s11, s12, **link3_conf)
        self.addLink(s12, s13, **link2_conf)
        self.addLink(s12, s14, **link0_conf)
        self.addLink(s14, s15, **link2_conf)
        self.addLink(s15, s16, **link3_conf)
        self.addLink(s15, s17, **link3_conf)


topos = {"Ans": (lambda: Ans())}
