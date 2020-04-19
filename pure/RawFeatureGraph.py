#!/home/xianglin/.virtualenvs/angr/bin/ python
# -*- coding: utf-8 -*-
__Auther__ = 'xianglin'

import angr
import networkx as nx
from NumericFeatureExtractor import *
from tools.image import Image
from tools.util.asm import is_jump


class RawFeatureGraph:
    """a graph to extract raw features of a cfg

    Attributes:
        func_name(string)
        cfg
        raw_feature(list):[numerice_features, structual_features]
        _graph(nx.Digraph)
    """
    def __init__(self, func_name, cfg):
        self.func_name = func_name
        self.cfg = cfg
        self.raw_features = []

    ######################################################################
    # structual features
    ######################################################################
    @property
    def graph(self):
        """the networkx graph of cfg"""
        if not hasattr(self, '_graph'):
            g = nx.DiGraph()
            # TODO
            self._graph = g
        return self._graph

    @property
    def betweeness(self):
        """the betweeness centrality of a node in graph"""
        if not hasattr(self, '_betweeness'):
            betweenness = nx.betweenness_centrality(self.graph)
            self._betweeness = betweenness
        return self._betweeness

    @property
    def offspring(self):
        """the outdegree of every node in graph"""
        return []




def get_a_BB():
    bin = "/home/xianglin/PycharmProjects/genius/testcase/2423496af35d94a87156b063ea5cedffc10a70a1/vmlinux"
    # bin = "/home/xianglin/Graduation/executables/string_constant"
    img = Image(bin)
    # func_name = "main"
    func_name = "dccp_rcv_state_process"
    entry = 66664
    func_cfg = img.get_cfg(func_name)
    # img.project.loader.memory.load()
    # bb = bin.factory.block(bin.entry)
    gra = RawFeatureGraph(func_name, func_cfg)
    print(1)


if __name__ == "__main__":
    get_a_BB()
