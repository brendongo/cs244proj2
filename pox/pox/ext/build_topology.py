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
sys.path.append("../../")
sys.path.append("../../..")
from graph import Graph
from pox.ext.jelly_pox import JELLYPOX
from subprocess import Popen
from time import sleep, time
from tqdm import tqdm

class JellyFishTop(Topo):
    ''' TODO, build your topology here'''
    def build(self):
        #leftHost = self.addHost( 'h1' )
        #rightHost = self.addHost( 'h2' )
        #leftSwitch = self.addSwitch( 's3' )
        #rightSwitch = self.addSwitch( 's4' )
        #
        ## Add links
        #self.addLink( leftHost, leftSwitch )
        #self.addLink( leftSwitch, rightSwitch )
        #self.addLink( rightSwitch, rightHost )

        PORTS_PER_SWITCH = 3
        SERVERS_PER_SWITCH = 1
        NUM_SWITCHES = 10
        graph = Graph.rrg(NUM_SWITCHES, PORTS_PER_SWITCH - SERVERS_PER_SWITCH)
        for switch in tqdm(graph.vertices()):
            self.addSwitch("s{}".format(switch.uid))
            for i in xrange(SERVERS_PER_SWITCH):
                server = self.addHost("h{}".format(switch.uid))
                self.addLink(server, "s{}".format(switch.uid))

        for switch in tqdm(graph.vertices()):
            for neighbor in switch.neighbors:
                if switch.uid < neighbor.uid:
                    self.addLink(
                            "s{}".format(switch.uid), "s{}".format(neighbor.uid))

def experiment(net):
    net.start()
    sleep(3)
    #net.pingAll()
    CLI(net)
    net.stop()

def main():
    topo = JellyFishTop()
    net = Mininet(topo=topo, host=CPULimitedHost, link = TCLink, controller=JELLYPOX)
    experiment(net)

if __name__ == "__main__":
    main()

