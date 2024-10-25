#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################
# Paper Analysis for Neurips 2024
# Working Directory : C:\Users\Admin\OneDrive\문서\Document\[001]_Reserach자료\[01] My_Research\[01_01] MyPapers\2024\Neurips_python_work
# 2024 10 24 by Jinwuk Seok
###########################################################################
_description = '''\
====================================================
translator.py : Translation Test
                    Written by Jinwuk @ 2022-01-11
====================================================
Example :  python translator.py -f original.txt 
'''
_abstrcat_msg = '''\
----------------------------------------------------
Original
----------------------------------------------------
'''
_translation_msg = '''\
----------------------------------------------------
Translated 
----------------------------------------------------
'''

from paper_analysis import neurips_paper
import os
import argparse, textwrap
import my_debug as DBG
def ArgumentParse(L_Param, _intro_msg=_description, bUseParam=False):
    parser = argparse.ArgumentParser(
        prog='paper_analysis.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(_intro_msg))

    parser.add_argument('-f', '--input_file', help="Input File (txt)",
                        type=str, default='source.txt')
    parser.add_argument('-dt', '--dest_lang', help="Destination Language (Default : 'kor')",
                        type=str, default='kor')
    parser.add_argument('-sr', '--sour_lang', help="Source Language (Default : 'eng')",
                        type=str, default='eng')
    parser.add_argument('-qt', '--quite_mode', help="Quite Mode (Default : 0)",
                        type=int, default=0)

    args = parser.parse_args(L_Param) if bUseParam else parser.parse_args()

    args.quite_mode    = True if args.quite_mode == 1 else False
    print(_intro_msg)
    return args

class translation_app:
    def __init__(self, L_Param, bUseParam=False):
        _app_class  = neurips_paper()
        self.args   = ArgumentParse(L_Param=L_Param, bUseParam=bUseParam)
        # ----------------------------------------------------------------
        # Path and File
        #----------------------------------------------------------------
        self.work_path  = _app_class.work_path
        self.work_file  = self.args.input_file
        self.outfile    = "translation.txt"
        self.work_fullpath = os.path.join(self.work_path, self.work_file)
        # ----------------------------------------------------------------
        # Parameters
        #----------------------------------------------------------------
        self.trans_func     = _app_class.translate_abstract
        self.abstract_msg   = textwrap.dedent(_abstrcat_msg)
        self.translated_msg = textwrap.dedent(_translation_msg)

    def get_source(self):
        with open(self.work_fullpath, 'r', encoding='utf-8') as _file:
            _contents = _file.read()
        return _contents
    def put_result(self, _contents):
        with open(self.outfile, 'w', encoding='utf-8') as _file:
             _file.write(_contents)

    def __call__(self, *args, **kwargs):
        d_source_str    = {'abstract': self.get_source()}
        _result_str     = self.trans_func(_dictionary=d_source_str, _active=True)
        self.put_result(_result_str)

        return d_source_str['abstract'], _result_str


# =================================================================
# Main Routine
# =================================================================
if __name__ == "__main__":
    c_op        = translation_app(L_Param=None)

    try :
        _src, _dst  = c_op()
    except Exception as e:
        print("Error Occur!! Error Message is")
        print("%s" %e)
        exit()

    if c_op.args.quite_mode:
        pass
    else:
        print(c_op.abstract_msg)
        print(_src, "\n")
        print(c_op.translated_msg)
        print(_dst, "\n")

    print("===================================================")
    print("Process Finished ")
    print("===================================================")


