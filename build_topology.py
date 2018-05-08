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
from ripl.ripl.dctopo import JellyFishTop
from time import sleep, time
from tqdm import tqdm


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
