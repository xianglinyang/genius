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
    """
    get instuctions num from a block
    :param block:
    :return: num(int)
    """
    num = 0
    return num


def cal_transfer_insts(block):
    num = 0
    return num


def cal_call_insts(block):
    num=0
    return num


def cal_arithmetic_insts(block):
    num = 0
    return num

######################################################################
# structual features
######################################################################


def get_a_BB():
    bin = angr.Project("/home/xianglin/PycharmProjects/genius/testcase/2423496af35d94a87156b063ea5cedffc10a70a1/vmlinux")
    # bin = "/home/xianglin/Graduation/executables/string_constant"
    # img = Image(bin)
    # func_name = "main"
    # entry = 66664
    # func_cfg = img.get_cfg(func_name)
    # img.project.loader.memory.load()
    bb = bin.factory.block(bin.entry)
    bb.capstone.pp()

if __name__ == "__main__":
    get_a_BB()
