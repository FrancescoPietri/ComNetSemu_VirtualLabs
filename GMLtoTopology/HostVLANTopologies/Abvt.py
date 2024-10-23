#!/usr/bin/python
# 23
from mininet.node import Host
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class VLANHost( Host ):
        "Host connected to VLAN interface"

        # pylint: disable=arguments-differ
        def config( self, vlan=100, **params ):

            print("test")

            r = super( VLANHost, self ).config( **params )

            intf = self.defaultIntf()
            # remove IP from default, "physical" interface
            self.cmd( 'ifconfig %s inet 0' % intf )
            # create VLAN interface
            self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
            # assign the host's IP to the VLAN interface
            self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
            # update the intf name and host's intf map
            newName = '%s.%d' % ( intf, vlan )
            # update the (Mininet) interface to refer to VLAN interface name
            intf.name = newName
            # add VLAN interface to host's name to intf map
            self.nameToIntf[ newName ] = intf

            return r


class Abvt(Topo):
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

        #adding hosts 
        h4 = self.addHost('h4', cls=VLANHost, vlan=20, ip='10.0.2.2/24') 
        h2 = self.addHost('h2', cls=VLANHost, vlan=20, ip='10.0.2.1/24') 
        h3 = self.addHost('h3', cls=VLANHost, vlan=10, ip='10.0.1.2/24') 
        h1 = self.addHost('h1', cls=VLANHost, vlan=10, ip='10.0.1.1/24') 

        #adding host to switch links
        self.addLink(h4, s12) 
        self.addLink(h3, s18) 
        self.addLink(h2, s10) 
        self.addLink(h1, s1) 

        # Adding Links
        link0_conf = {
            "bw": 100.0,
            "delay": 10.0,
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
        self.addLink(s0, s2, **link0_conf)
        self.addLink(s0, s4, **link0_conf)
        self.addLink(s0, s5, **link0_conf)
        self.addLink(s0, s7, **link0_conf)
        self.addLink(s1, s8, **link0_conf)
        self.addLink(s1, s6, **link0_conf)
        self.addLink(s1, s4, **link0_conf)
        self.addLink(s1, s5, **link0_conf)
        self.addLink(s1, s22, **link0_conf)
        self.addLink(s2, s10, **link0_conf)
        self.addLink(s2, s3, **link0_conf)
        self.addLink(s3, s10, **link0_conf)
        self.addLink(s5, s12, **link0_conf)
        self.addLink(s5, s8, **link0_conf)
        self.addLink(s6, s7, **link0_conf)
        self.addLink(s8, s9, **link0_conf)
        self.addLink(s9, s12, **link0_conf)
        self.addLink(s10, s20, **link0_conf)
        self.addLink(s10, s13, **link0_conf)
        self.addLink(s10, s14, **link0_conf)
        self.addLink(s11, s13, **link0_conf)
        self.addLink(s11, s22, **link0_conf)
        self.addLink(s11, s21, **link0_conf)
        self.addLink(s13, s14, **link0_conf)
        self.addLink(s15, s16, **link0_conf)
        self.addLink(s15, s22, **link0_conf)
        self.addLink(s16, s18, **link0_conf)
        self.addLink(s17, s18, **link0_conf)
        self.addLink(s18, s19, **link0_conf)
        self.addLink(s18, s21, **link0_conf)
        self.addLink(s19, s20, **link0_conf)


topos = {"Abvt": (lambda: Abvt())}
