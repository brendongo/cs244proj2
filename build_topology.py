import os
import sys
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.node import OVSController
from mininet.node import Controller
from mininet.node import RemoteController
from mininet.cli import CLI
from graph import Graph
from jelly_pox import JELLYPOX
from subprocess import Popen
from time import sleep, time
from tqdm import tqdm

class ID(object):
    '''Fat Tree-specific node.'''
    def __init__(self, name=None, dpid=None):
        '''Create FatTreeNodeID object from custom params.
        Either (pod, sw, host) or dpid must be passed in.

        @param dpid optional dpid
        @param name optional name
        '''
        if dpid:
            self.host = dpid
            self.dpid = int(dpid)
        elif name:
            self.host = name
            self.dpid = int(name[1:])

    def __str__(self):
        return "(%i, %i, %i)" % (self.pod, self.sw, self.host)

    def name_str(self):
        '''Return name string'''
        return "s{}".format(self.host)

    def mac_str(self):
        '''Return MAC string'''
        return "00:00:00:%02x:%02x:%02x" % (self.pod, self.sw, self.host)

    def ip_str(self):
        '''Return IP string'''
        return "10.%i.%i.%i" % (self.pod, self.sw, self.host)

class JellyFishTop(Topo):
    ''' TODO, build your topology here'''
    def build(self):
        leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )

        self.id_gen = ID
        #PORTS_PER_SWITCH = 3
        #SERVERS_PER_SWITCH = 1
        #NUM_SWITCHES = 10
        #graph = Graph.rrg(NUM_SWITCHES, PORTS_PER_SWITCH - SERVERS_PER_SWITCH)
        #for switch in tqdm(graph.vertices()):
        #    self.addSwitch("s{}".format(switch.uid))
        #    for i in xrange(SERVERS_PER_SWITCH):
        #        server = self.addHost("h{}".format(switch.uid))
        #        self.addLink(server, "s{}".format(switch.uid))

        #for switch in tqdm(graph.vertices()):
        #    for neighbor in switch.neighbors:
        #        if switch.uid < neighbor.uid:
        #            self.addLink(
        #                    "s{}".format(switch.uid), "s{}".format(neighbor.uid))

def experiment(net):
    net.start()
    sleep(3)
    #net.pingAll()
    CLI(net)
    net.stop()

def main():
    topo = JellyFishTop()
    net = Mininet(
            topo=topo, host=CPULimitedHost, link=TCLink,
            controller=lambda name: RemoteController(name, port=6633))
    experiment(net)

if __name__ == "__main__":
    main()

topos = {'jelly': JellyFishTop}
