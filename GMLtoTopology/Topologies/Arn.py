#!/usr/bin/python
# 30
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


class Arn(Topo):
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

        #adding hosts 
        h1 = self.addHost('h1', cls=VLANHost, vlan=1, ip='10.0.0.1/24') 
        h2 = self.addHost('h2') 

        #adding host to switch links
        self.addLink(h1, s2) 
        self.addLink(h2, s5) 

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
        self.addLink(s0, s22, **link0_conf)
        self.addLink(s1, s22, **link1_conf)
        self.addLink(s2, s22, **link1_conf)
        self.addLink(s3, s22, **link0_conf)
        self.addLink(s4, s7, **link0_conf)
        self.addLink(s5, s8, **link1_conf)
        self.addLink(s6, s7, **link0_conf)
        self.addLink(s7, s22, **link1_conf)
        self.addLink(s8, s9, **link0_conf)
        self.addLink(s8, s10, **link1_conf)
        self.addLink(s8, s12, **link1_conf)
        self.addLink(s8, s13, **link1_conf)
        self.addLink(s8, s14, **link0_conf)
        self.addLink(s8, s15, **link0_conf)
        self.addLink(s8, s18, **link0_conf)
        self.addLink(s8, s19, **link1_conf)
        self.addLink(s8, s22, **link0_conf)
        self.addLink(s11, s22, **link0_conf)
        self.addLink(s16, s22, **link1_conf)
        self.addLink(s17, s22, **link0_conf)
        self.addLink(s20, s24, **link1_conf)
        self.addLink(s21, s22, **link0_conf)
        self.addLink(s22, s23, **link0_conf)
        self.addLink(s22, s24, **link0_conf)
        self.addLink(s24, s25, **link0_conf)
        self.addLink(s24, s26, **link0_conf)
        self.addLink(s24, s27, **link0_conf)
        self.addLink(s24, s28, **link0_conf)
        self.addLink(s24, s29, **link1_conf)


topos = {"Arn": (lambda: Arn())}
