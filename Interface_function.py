#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################
# Paper Nalysis for Neurips 2024
# Working Directory : C:\Users\Admin\OneDrive\문서\Document\[001]_Reserach자료\[01] My_Research\[01_01] MyPapers\2024\Neurips_python_work
# 2024 10 24 by Jinwuk Seok
###########################################################################
_description = '''\
====================================================
Interface_Function.py : Interface Functions for Neurips_2024 Project 
                    Written by Jinwuk @ 2024-11-20
====================================================
Example :  There is no Operation instruction. 
'''
import argparse, textwrap
def ArgumentParse(L_Param, _prog, _intro_msg=_description, bUseParam=False):
    parser = argparse.ArgumentParser(
        prog=_prog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(_intro_msg))

    parser.add_argument('-pn', '--paper_name', help="[Paper Analysis] (Partial) Paper Name",
                        type=str, default='')
    parser.add_argument('-tr', '--translation', help="[Paper Analysis] Translation (eng->kor) [Default : Use]",
                        action='store_false')
    parser.add_argument('-m', '--manual_op', help="[Paper Analysis] manual operation [Default : Not Use]",
                        action='store_true')
    parser.add_argument('-a', '--append_mode', help="[Paper Analysis] Append paper_summary.txt or not [Default : Not Use]",
                        action='store_true')
    parser.add_argument('-f', '--input_file', help="[Translator]Input File (txt)",
                        type=str, default='source.txt')
    parser.add_argument('-dt', '--dest_lang', help="[Translator] Destination Language (Default : 'kor')",
                        type=str, default='kor')
    parser.add_argument('-sr', '--sour_lang', help="[Translator] Source Language (Default : 'eng')",
                        type=str, default='eng')
    parser.add_argument('-qt', '--quite_mode', action='store_true', help="[Translator] Quite Mode (Default : 0)",
                        default=False)
    parser.add_argument('-jn', '--journal_name', help="[predatory] (Partial) Journal Name",
                        type=str, default='')

    args = parser.parse_args(L_Param) if bUseParam else parser.parse_args()

    print(_intro_msg)
    return args
