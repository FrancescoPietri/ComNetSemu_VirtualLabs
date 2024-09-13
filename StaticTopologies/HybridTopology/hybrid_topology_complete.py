#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from sys import exit  
from mininet.node import Host
from mininet.util import quietRun
from mininet.log import error

class VLANHost( Host ):
    "Host connected to VLAN interface"

    # pylint: disable=arguments-differ
    def config( self, vlan=100, **params ):
        """Configure VLANHost according to (optional) parameters:
           vlan: VLAN ID for default interface"""

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

class HybridTopologyComplete(Topo):
    "HybridTopologyComplete"

    def __init__(self):

        Topo.__init__(self)

        # Define switches
        s1 = self.addSwitch('s1', dpid='0000000000000001')  
        s2 = self.addSwitch('s2', dpid='0000000000000002')
        s3 = self.addSwitch('s3', dpid='0000000000000003')
        s4 = self.addSwitch('s4', dpid='0000000000000004') 
        s5 = self.addSwitch('s5', dpid='0000000000000005')
        s6 = self.addSwitch('s6', dpid='0000000000000006')  
        s7 = self.addSwitch('s7', dpid='0000000000000007')
        s8 = self.addSwitch('s8', dpid='0000000000000008')
        s9 = self.addSwitch('s9', dpid='0000000000000009')
        s10 = self.addSwitch('s10', dpid='000000000000000a')
        s11 = self.addSwitch('s11', dpid='000000000000000b')
        s12 = self.addSwitch('s12', dpid='000000000000000c')

        # Define Switches
        h1 = self.addHost('h1',  cls=VLANHost, vlan=1, ip='10.0.1.1/24')
        h2 = self.addHost('h2',  cls=VLANHost, vlan=2, ip='10.0.2.1/24') 
        h3 = self.addHost('h3',  cls=VLANHost, vlan=1, ip='10.0.1.2/24')
        h4 = self.addHost('h4',  cls=VLANHost, vlan=2, ip='10.0.2.2/24')
        h5 = self.addHost('h5',  cls=VLANHost, vlan=3, ip='10.0.3.1/24')
        h6 = self.addHost('h6',  cls=VLANHost, vlan=3, ip='10.0.3.2/24')

        # Link configurations
        queue_length = 10
        host_link_config = dict()  # Default host links
        weakbb_link_config = dict(delay='20ms', use_tbf=True, bw=20, max_queue_size=queue_length, latency_ms=10000000, burst=1000000)  # Weak backbone links (low bandwidth)
        strongbb_link_config = dict(delay='25ms', use_tbf=True, bw=50, max_queue_size=queue_length, latency_ms=10000000, burst=1000000)  # Strong backbone links (high bandwidth)

        # Add links between hosts and switches
        self.addLink(h1, s1, **host_link_config)
        self.addLink(h2, s9, **host_link_config)
        self.addLink(h3, s10, **host_link_config)
        self.addLink(h4, s11, **host_link_config)
        self.addLink(h5, s12, **host_link_config)
        self.addLink(h6, s6, **host_link_config)

        # Add links between switches with explicit random "weak" or "strong" configurations
        self.addLink(s1, s2, **weakbb_link_config)
        self.addLink(s1, s3, **strongbb_link_config)
        self.addLink(s2, s4, **weakbb_link_config)
        self.addLink(s3, s4, **weakbb_link_config)
        self.addLink(s4, s5, **strongbb_link_config)
        self.addLink(s5, s6, **strongbb_link_config)
        self.addLink(s5, s7, **weakbb_link_config)
        self.addLink(s5, s8, **strongbb_link_config)
        self.addLink(s7, s9, **strongbb_link_config)
        self.addLink(s7, s10, **weakbb_link_config)
        self.addLink(s8, s11, **strongbb_link_config)
        self.addLink(s8, s12, **strongbb_link_config)

topos = { 'hybridtopologycomplete': ( lambda: HybridTopologyComplete() ) }