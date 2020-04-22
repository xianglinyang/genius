#!/home/xianglin/.virtualenvs/angr/bin/ python
# -*- coding: utf-8 -*-
__Auther__ = 'xianglin'


import angr
import capstone
import claripy
from tools.image import Image
from tools.util.asm import is_jump
import numpy as np
from sklearn.cluster import spectral_clustering
from sklearn.metrics import jaccard_score
import CodebookGenerator
import heapq
import codebook


def feature_encode(graph, cb, codebook_dim=16, nn=10):
    """encode raw feature vector to high-level numeric vector"""
    scores = [0 for i in range(codebook_dim)]
    scores_h = []
    for i in range(len(cb)):
        score = CodebookGenerator.normalized_ACFG_similarity(graph, cb[i])
        heapq.heappush(scores_h, (score, i))
    # pop codebook_dim - nn elements
    for i in range(codebook_dim - nn):
        heapq.heappop(scores_h)
    while len(scores_h) > 0:
        score, index = heapq.heappop(scores_h)
        scores[index] = score
    return scores



