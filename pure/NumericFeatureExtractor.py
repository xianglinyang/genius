#!/home/xianglin/.virtualenvs/angr/bin/ python
# -*- coding: utf-8 -*-
__Auther__ = 'xianglin'

import angr
import capstone
from tools.image import Image
from tools.util.asm import is_jump


######################################################################
# numeric feature
######################################################################
def cal_const(insn):
    """
    get const from an instrcution

    Args:
        insn:(capstone.insn) an instuction

    Returns:
        string_consts(list):
        numeric_consts(list):
    """
    string_consts = []
    numeric_consts = []
    return string_consts, numeric_consts


def cal_BB_consts(block):
    """
    get string and numeric consts from a block
    Args:
        block: angr.block

    Returns:
        string_consts(list): string consts from a block
        numeric_consts(list): numeric consts from a block

    """
    string_consts = []
    numeric_consts = []

    return string_consts, numeric_consts


def cal_insts(block):
    num = 0
    return num


def cal_transfer_insts(block):
    num = 0
    return num


def cal_call_insts(block):
    num = 0
    return num


def cal_arithmetic_insts(block):
    num = 0
    return num
