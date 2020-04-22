#!/home/xianglin/.virtualenvs/angr/bin/ python
# -*- coding: utf-8 -*-
__Auther__ = 'xianglin', 'Zhang_JX'


import angr
import capstone
import claripy
from tools.image import Image
from tools.util.asm import is_jump
import numpy as np
from sklearn.cluster import spectral_clustering
from sklearn.metrics import jaccard_score
import CodebookGenerator
import RawFeatureGraph
import codebook


def processing_grouping(res, matrix): # grouping res and similarity matrix
    # return center for each group
    center = []
    # for each group, find the one that is most similar to other points
    for group in res:
        now_center = group[0]
        now_sim = -1
        for inner_center in group:
            inner_similarity_sum = 0
            for other in group:
                inner_similarity_sum += matrix[inner_center, other]
            if inner_similarity_sum > now_sim:
                now_sim = inner_similarity_sum
                now_center = inner_center
            center.append(now_center)
    return center


def gen_codebook(graphs, group_num=16):
    m = len(graphs)
    # similarity socre matrix
    W_matrix = np.zeros((m, m))
    for i in range(m):
        for j in range(m):
            if i >= j:
                W_matrix[i, j] = W_matrix[j, i]
            else:
                W_matrix[i, j] = CodebookGenerator.normalized_ACFG_similarity(graphs[i], graphs[j])
    res = spectral_clustering(W_matrix, n_clusters=group_num)
    group_res = []
    for i in range(group_num):
        group_res.append([])
    for i in range(m):
        group_res[res[i]].append(i)
    centers = processing_grouping(group_res, W_matrix)
    codebook = []
    for i in centers:
        codebook.append(graphs[i])
    return codebook


if __name__ == "__main__":
    # debug_vmlinux = "../testcase/2423496af35d94a87156b063ea5cedffc10a70a1/vmlinux"
    # img = Image(debug_vmlinux)
    # funcs = img.funcs
    # graphs = []
    # for i in range(32):
    #     func = funcs.pop()
    #     graphs.append(RawFeatureGraph.get_func_rfg(debug_vmlinux, func))
    # print(graphs)
    graphs = codebook.codebook8
    codebook = gen_codebook(graphs, group_num=4)
    print(codebook)

