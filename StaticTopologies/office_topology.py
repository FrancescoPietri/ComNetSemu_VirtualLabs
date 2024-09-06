from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class OfficeTopology( Topo ):
    "OfficeTopology"

     net = Mininet(topo=None,
                  build=False,
                  ipBase='10.0.0.0/8', link=TCLink, switch=OVSKernelSwitch)


    controllerIP = '127.0.0.1'
    info('*** Adding controller\n')
    c0 = net.addController(name='c0',
                           controller=RemoteController,
                           ip=controllerIP,
                           protocol='tcp',
                           port=6633)
