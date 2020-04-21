#!/home/xianglin/.virtualenvs/angr/bin/ python
# -*- coding: utf-8 -*-
__Auther__ = 'xianglin'

import angr
import capstone
from tools.image import Image
from tools.util.asm import is_jump

"""
it is based on ARM64 instruction set, might add more CPU arch in the future
"""
######################################################################
# numeric feature
######################################################################
def cal_const(img, insn, offset):
    """
    get const from an instrcution

    Args:
        insn:(capstone.insn) an instuction
        offset(int): the i-th operand

    Returns:
        string_consts(list):
        numeric_consts(list):
    """
    string_consts = []
    numeric_consts = []
    insn = insn.insn
    arm64_CI = {'b', 'bl', 'cbz', 'cbnz', 'tbz', 'tbnz'}
    op_imm = {'ARM_OP_IMM', 'ARM64_OP_IMM', 'X86_OP_IMM', 'MIPS_OP_IMM'}
    op_mnemonic = insn.mnemonic
    # if mnemonic is in call functions, return
    if check_type(op_mnemonic, arm64_CI):
        return string_consts, numeric_consts

    base_pointer = {'pc'}
    operand = insn.operands[offset]
    op_type = operand.type
    # if it is an immediate value, output the value
    # contingent across all arch
    if op_type == capstone.arm64.ARM64_OP_IMM:
        # if adr, then string/numeric?, else numeric
        if check_type(op_mnemonic, {'adr'}):
            addr = operand.value.imm
            string_const = get_string(img, addr)
            if string_const is None:
                numeric_const = get_numeric(img, addr)
                numeric_consts.append(numeric_const)
            else:
                string_consts.append(string_const)
        else:
            numeric_consts.append(operand.value.imm)
    # [mem]
    elif op_type == capstone.arm64.ARM64_OP_MEM:
        if operand.value.mem.base != 0:
            base_reg = insn.reg_name(operand.value.mem.base)
            if base_reg in base_pointer:
                disp = operand.value.mem.disp
                addr = insn.address + disp
                imm_value = img.project.loader.memory.load(addr, 4)
                numeric_consts.append(imm_value)

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
    return block.instructions


def cal_transfer_insts(block):
    num = 0
    return num


def cal_call_insts(block):
    num = 0
    return num


def cal_arithmetic_insts(block):
    num = 0
    return num


######################################################################
# other functions
######################################################################
def check_type(t, t_set):
    """
    Args:
        t(str): operator or register
        t_set(set): check type set

    Returns:
        states(boolean): true if t is in t_set

    """
    for t_type in t_set:
        if t.startswith(t_type):
            return True
    return False


def get_string(img, addr):
    string = ""
    for i in range(1000):
        c = img.project.loader.memory.load(addr + i * 8, 1)
        if c == 0:
            break
        elif 40 <= ord(c) < 128:
            string += ord(c)
        else:
            return None
    return string


def get_numeric(img, addr):
    num = img.project.loader.memory.load(addr, 4)
    return num
