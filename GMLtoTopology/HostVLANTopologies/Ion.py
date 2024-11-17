#!/usr/bin/python
# 125
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


class Ion(Topo):
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
        s82 = self.addSwitch("s82", dpid="0000000000000054")
        s83 = self.addSwitch("s83", dpid="0000000000000055")
        s84 = self.addSwitch("s84", dpid="0000000000000056")
        s85 = self.addSwitch("s85", dpid="0000000000000057")
        s86 = self.addSwitch("s86", dpid="0000000000000058")
        s87 = self.addSwitch("s87", dpid="0000000000000059")
        s88 = self.addSwitch("s88", dpid="000000000000005a")
        s89 = self.addSwitch("s89", dpid="000000000000005b")
        s90 = self.addSwitch("s90", dpid="000000000000005c")
        s91 = self.addSwitch("s91", dpid="000000000000005d")
        s92 = self.addSwitch("s92", dpid="000000000000005e")
        s93 = self.addSwitch("s93", dpid="000000000000005f")
        s94 = self.addSwitch("s94", dpid="0000000000000060")
        s95 = self.addSwitch("s95", dpid="0000000000000061")
        s96 = self.addSwitch("s96", dpid="0000000000000062")
        s97 = self.addSwitch("s97", dpid="0000000000000063")
        s98 = self.addSwitch("s98", dpid="0000000000000064")
        s99 = self.addSwitch("s99", dpid="0000000000000065")
        s100 = self.addSwitch("s100", dpid="0000000000000066")
        s101 = self.addSwitch("s101", dpid="0000000000000067")
        s102 = self.addSwitch("s102", dpid="0000000000000068")
        s103 = self.addSwitch("s103", dpid="0000000000000069")
        s104 = self.addSwitch("s104", dpid="000000000000006a")
        s105 = self.addSwitch("s105", dpid="000000000000006b")
        s106 = self.addSwitch("s106", dpid="000000000000006c")
        s107 = self.addSwitch("s107", dpid="000000000000006d")
        s108 = self.addSwitch("s108", dpid="000000000000006e")
        s109 = self.addSwitch("s109", dpid="000000000000006f")
        s110 = self.addSwitch("s110", dpid="0000000000000070")
        s111 = self.addSwitch("s111", dpid="0000000000000071")
        s112 = self.addSwitch("s112", dpid="0000000000000072")
        s113 = self.addSwitch("s113", dpid="0000000000000073")
        s114 = self.addSwitch("s114", dpid="0000000000000074")
        s115 = self.addSwitch("s115", dpid="0000000000000075")
        s116 = self.addSwitch("s116", dpid="0000000000000076")
        s117 = self.addSwitch("s117", dpid="0000000000000077")
        s118 = self.addSwitch("s118", dpid="0000000000000078")
        s119 = self.addSwitch("s119", dpid="0000000000000079")
        s120 = self.addSwitch("s120", dpid="000000000000007a")
        s121 = self.addSwitch("s121", dpid="000000000000007b")
        s122 = self.addSwitch("s122", dpid="000000000000007c")
        s123 = self.addSwitch("s123", dpid="000000000000007d")
        s124 = self.addSwitch("s124", dpid="000000000000007e")

        #adding hosts 
        h4 = self.addHost('h4', cls=VLANHost, vlan=20, ip='10.0.2.2/24') 
        h3 = self.addHost('h3', cls=VLANHost, vlan=10, ip='10.0.1.2/24') 
        h2 = self.addHost('h2', cls=VLANHost, vlan=20, ip='10.0.2.1/24') 
        h1 = self.addHost('h1', cls=VLANHost, vlan=10, ip='10.0.1.1/24')

        #adding host to switch links
        self.addLink(h4, s110) 
        self.addLink(h3, s100) 
        self.addLink(h2, s40) 
        self.addLink(h1, s10) 

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
        self.addLink(s0, s25, **link0_conf)
        self.addLink(s0, s9, **link2_conf)
        self.addLink(s1, s114, **link1_conf)
        self.addLink(s1, s70, **link2_conf)
        self.addLink(s2, s99, **link0_conf)
        self.addLink(s2, s3, **link1_conf)
        self.addLink(s3, s4, **link0_conf)
        self.addLink(s3, s5, **link2_conf)
        self.addLink(s3, s6, **link1_conf)
        self.addLink(s3, s6, **link1_conf)
        self.addLink(s3, s7, **link1_conf)
        self.addLink(s5, s103, **link1_conf)
        self.addLink(s8, s100, **link2_conf)
        self.addLink(s8, s92, **link1_conf)
        self.addLink(s9, s64, **link0_conf)
        self.addLink(s10, s58, **link1_conf)
        self.addLink(s10, s11, **link2_conf)
        self.addLink(s11, s18, **link1_conf)
        self.addLink(s12, s19, **link1_conf)
        self.addLink(s13, s18, **link2_conf)
        self.addLink(s13, s19, **link2_conf)
        self.addLink(s14, s17, **link2_conf)
        self.addLink(s14, s111, **link0_conf)
        self.addLink(s15, s114, **link1_conf)
        self.addLink(s15, s111, **link1_conf)
        self.addLink(s16, s112, **link1_conf)
        self.addLink(s16, s17, **link0_conf)
        self.addLink(s18, s39, **link2_conf)
        self.addLink(s19, s59, **link2_conf)
        self.addLink(s20, s64, **link1_conf)
        self.addLink(s20, s36, **link2_conf)
        self.addLink(s21, s80, **link1_conf)
        self.addLink(s21, s54, **link1_conf)
        self.addLink(s21, s79, **link2_conf)
        self.addLink(s22, s80, **link2_conf)
        self.addLink(s22, s54, **link1_conf)
        self.addLink(s22, s79, **link2_conf)
        self.addLink(s23, s26, **link0_conf)
        self.addLink(s23, s27, **link2_conf)
        self.addLink(s24, s35, **link2_conf)
        self.addLink(s24, s35, **link2_conf)
        self.addLink(s24, s36, **link0_conf)
        self.addLink(s25, s28, **link2_conf)
        self.addLink(s26, s107, **link1_conf)
        self.addLink(s26, s87, **link2_conf)
        self.addLink(s27, s28, **link1_conf)
        self.addLink(s28, s88, **link2_conf)
        self.addLink(s29, s32, **link2_conf)
        self.addLink(s29, s33, **link2_conf)
        self.addLink(s29, s101, **link0_conf)
        self.addLink(s29, s105, **link1_conf)
        self.addLink(s29, s106, **link1_conf)
        self.addLink(s29, s30, **link2_conf)
        self.addLink(s30, s31, **link2_conf)
        self.addLink(s31, s32, **link0_conf)
        self.addLink(s33, s34, **link0_conf)
        self.addLink(s34, s104, **link2_conf)
        self.addLink(s34, s103, **link1_conf)
        self.addLink(s35, s42, **link0_conf)
        self.addLink(s37, s40, **link1_conf)
        self.addLink(s37, s38, **link0_conf)
        self.addLink(s38, s43, **link0_conf)
        self.addLink(s39, s40, **link0_conf)
        self.addLink(s41, s42, **link1_conf)
        self.addLink(s41, s44, **link1_conf)
        self.addLink(s43, s44, **link2_conf)
        self.addLink(s44, s116, **link0_conf)
        self.addLink(s45, s93, **link2_conf)
        self.addLink(s45, s54, **link1_conf)
        self.addLink(s46, s93, **link1_conf)
        self.addLink(s46, s47, **link0_conf)
        self.addLink(s47, s48, **link0_conf)
        self.addLink(s48, s49, **link2_conf)
        self.addLink(s48, s123, **link2_conf)
        self.addLink(s48, s78, **link2_conf)
        self.addLink(s49, s109, **link1_conf)
        self.addLink(s50, s76, **link2_conf)
        self.addLink(s51, s76, **link2_conf)
        self.addLink(s51, s52, **link0_conf)
        self.addLink(s52, s109, **link2_conf)
        self.addLink(s53, s123, **link2_conf)
        self.addLink(s55, s56, **link0_conf)
        self.addLink(s55, s62, **link0_conf)
        self.addLink(s56, s57, **link2_conf)
        self.addLink(s57, s97, **link1_conf)
        self.addLink(s58, s97, **link1_conf)
        self.addLink(s58, s92, **link0_conf)
        self.addLink(s59, s124, **link2_conf)
        self.addLink(s59, s61, **link2_conf)
        self.addLink(s60, s124, **link0_conf)
        self.addLink(s60, s124, **link0_conf)
        self.addLink(s60, s109, **link2_conf)
        self.addLink(s61, s98, **link0_conf)
        self.addLink(s62, s98, **link2_conf)
        self.addLink(s63, s96, **link0_conf)
        self.addLink(s63, s66, **link2_conf)
        self.addLink(s64, s116, **link2_conf)
        self.addLink(s64, s65, **link0_conf)
        self.addLink(s65, s111, **link0_conf)
        self.addLink(s66, s87, **link2_conf)
        self.addLink(s67, s74, **link2_conf)
        self.addLink(s67, s68, **link1_conf)
        self.addLink(s67, s86, **link1_conf)
        self.addLink(s68, s95, **link0_conf)
        self.addLink(s69, s117, **link2_conf)
        self.addLink(s69, s70, **link1_conf)
        self.addLink(s71, s74, **link2_conf)
        self.addLink(s72, s74, **link1_conf)
        self.addLink(s72, s117, **link1_conf)
        self.addLink(s73, s124, **link0_conf)
        self.addLink(s73, s110, **link0_conf)
        self.addLink(s74, s112, **link2_conf)
        self.addLink(s74, s110, **link1_conf)
        self.addLink(s75, s76, **link2_conf)
        self.addLink(s75, s95, **link1_conf)
        self.addLink(s76, s110, **link2_conf)
        self.addLink(s77, s80, **link2_conf)
        self.addLink(s77, s78, **link1_conf)
        self.addLink(s79, s82, **link1_conf)
        self.addLink(s81, s82, **link1_conf)
        self.addLink(s81, s94, **link0_conf)
        self.addLink(s83, s86, **link1_conf)
        self.addLink(s83, s94, **link1_conf)
        self.addLink(s84, s94, **link1_conf)
        self.addLink(s85, s95, **link0_conf)
        self.addLink(s88, s91, **link0_conf)
        self.addLink(s89, s90, **link2_conf)
        self.addLink(s89, s115, **link0_conf)
        self.addLink(s89, s122, **link1_conf)
        self.addLink(s90, s96, **link0_conf)
        self.addLink(s91, s120, **link1_conf)
        self.addLink(s93, s123, **link0_conf)
        self.addLink(s96, s121, **link2_conf)
        self.addLink(s99, s105, **link1_conf)
        self.addLink(s100, s105, **link0_conf)
        self.addLink(s100, s107, **link2_conf)
        self.addLink(s101, s106, **link1_conf)
        self.addLink(s102, s103, **link2_conf)
        self.addLink(s102, s103, **link2_conf)
        self.addLink(s106, s108, **link0_conf)
        self.addLink(s107, s108, **link1_conf)
        self.addLink(s111, s113, **link0_conf)
        self.addLink(s112, s113, **link1_conf)
        self.addLink(s113, s114, **link2_conf)
        self.addLink(s115, s117, **link0_conf)
        self.addLink(s117, s118, **link0_conf)
        self.addLink(s118, s119, **link1_conf)
        self.addLink(s119, s120, **link2_conf)
        self.addLink(s120, s121, **link0_conf)
        self.addLink(s121, s122, **link1_conf)


topos = {"Ion": (lambda: Ion())}
