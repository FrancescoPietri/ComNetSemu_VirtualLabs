#!/usr/bin/python
# 73
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


class Intellifiber(Topo):
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

        #adding hosts 
        h4 = self.addHost('h4', cls=VLANHost, vlan=20, ip='10.0.2.2/24') 
        h2 = self.addHost('h2', cls=VLANHost, vlan=20, ip='10.0.2.1/24') 
        h3 = self.addHost('h3', cls=VLANHost, vlan=10, ip='10.0.1.2/24') 
        h1 = self.addHost('h1', cls=VLANHost, vlan=10, ip='10.0.1.1/24') 

        #adding host to switch links
        self.addLink(h4, s12) 
        self.addLink(h3, s18) 
        self.addLink(h2, s30) 
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
        self.addLink(s0, s1, **link0_conf)
        self.addLink(s0, s3, **link0_conf)
        self.addLink(s1, s6, **link0_conf)
        self.addLink(s1, s71, **link0_conf)
        self.addLink(s2, s64, **link0_conf)
        self.addLink(s2, s66, **link0_conf)
        self.addLink(s2, s3, **link0_conf)
        self.addLink(s3, s31, **link0_conf)
        self.addLink(s4, s41, **link0_conf)
        self.addLink(s4, s6, **link0_conf)
        self.addLink(s5, s42, **link0_conf)
        self.addLink(s5, s10, **link0_conf)
        self.addLink(s5, s6, **link0_conf)
        self.addLink(s6, s10, **link0_conf)
        self.addLink(s6, s7, **link0_conf)
        self.addLink(s6, s7, **link0_conf)
        self.addLink(s7, s41, **link0_conf)
        self.addLink(s7, s36, **link0_conf)
        self.addLink(s8, s26, **link0_conf)
        self.addLink(s9, s24, **link0_conf)
        self.addLink(s9, s29, **link0_conf)
        self.addLink(s10, s11, **link0_conf)
        self.addLink(s10, s55, **link0_conf)
        self.addLink(s11, s55, **link0_conf)
        self.addLink(s12, s37, **link0_conf)
        self.addLink(s12, s47, **link0_conf)
        self.addLink(s13, s32, **link0_conf)
        self.addLink(s13, s38, **link0_conf)
        self.addLink(s14, s46, **link0_conf)
        self.addLink(s14, s15, **link0_conf)
        self.addLink(s15, s32, **link0_conf)
        self.addLink(s15, s34, **link0_conf)
        self.addLink(s15, s27, **link0_conf)
        self.addLink(s15, s46, **link0_conf)
        self.addLink(s16, s17, **link0_conf)
        self.addLink(s16, s44, **link0_conf)
        self.addLink(s16, s23, **link0_conf)
        self.addLink(s17, s42, **link0_conf)
        self.addLink(s18, s19, **link0_conf)
        self.addLink(s18, s53, **link0_conf)
        self.addLink(s19, s20, **link0_conf)
        self.addLink(s19, s53, **link0_conf)
        self.addLink(s19, s22, **link0_conf)
        self.addLink(s19, s23, **link0_conf)
        self.addLink(s20, s49, **link0_conf)
        self.addLink(s21, s22, **link0_conf)
        self.addLink(s21, s55, **link0_conf)
        self.addLink(s22, s25, **link0_conf)
        self.addLink(s22, s23, **link0_conf)
        self.addLink(s23, s24, **link0_conf)
        self.addLink(s23, s25, **link0_conf)
        self.addLink(s24, s48, **link0_conf)
        self.addLink(s24, s61, **link0_conf)
        self.addLink(s24, s25, **link0_conf)
        self.addLink(s26, s29, **link0_conf)
        self.addLink(s26, s61, **link0_conf)
        self.addLink(s27, s28, **link0_conf)
        self.addLink(s28, s40, **link0_conf)
        self.addLink(s29, s69, **link0_conf)
        self.addLink(s30, s68, **link0_conf)
        self.addLink(s31, s62, **link0_conf)
        self.addLink(s33, s34, **link0_conf)
        self.addLink(s33, s51, **link0_conf)
        self.addLink(s34, s37, **link0_conf)
        self.addLink(s34, s47, **link0_conf)
        self.addLink(s35, s36, **link0_conf)
        self.addLink(s35, s62, **link0_conf)
        self.addLink(s38, s39, **link0_conf)
        self.addLink(s39, s40, **link0_conf)
        self.addLink(s41, s42, **link0_conf)
        self.addLink(s41, s44, **link0_conf)
        self.addLink(s43, s46, **link0_conf)
        self.addLink(s44, s46, **link0_conf)
        self.addLink(s45, s51, **link0_conf)
        self.addLink(s45, s60, **link0_conf)
        self.addLink(s45, s46, **link0_conf)
        self.addLink(s46, s48, **link0_conf)
        self.addLink(s46, s51, **link0_conf)
        self.addLink(s47, s60, **link0_conf)
        self.addLink(s49, s50, **link0_conf)
        self.addLink(s50, s56, **link0_conf)
        self.addLink(s52, s53, **link0_conf)
        self.addLink(s53, s59, **link0_conf)
        self.addLink(s53, s55, **link0_conf)
        self.addLink(s53, s55, **link0_conf)
        self.addLink(s54, s55, **link0_conf)
        self.addLink(s56, s57, **link0_conf)
        self.addLink(s57, s58, **link0_conf)
        self.addLink(s58, s59, **link0_conf)
        self.addLink(s63, s64, **link0_conf)
        self.addLink(s63, s72, **link0_conf)
        self.addLink(s65, s66, **link0_conf)
        self.addLink(s66, s67, **link0_conf)
        self.addLink(s67, s68, **link0_conf)
        self.addLink(s68, s70, **link0_conf)
        self.addLink(s70, s71, **link0_conf)
        self.addLink(s71, s72, **link0_conf)


topos = {"Intellifiber": (lambda: Intellifiber())}
