#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################
# Paper Nalysis for Neurips 2024
# Working Directory : C:\Users\Admin\OneDrive\문서\Document\[001]_Reserach자료\[01] My_Research\[01_01] MyPapers\2024\Neurips_python_work
# 2024 10 24 by Jinwuk Seok
###########################################################################
_description = '''\
====================================================
predatory_j.py : Search a predatory journal with a journal name
                    Written by Jinwuk @ 2024-11-19
====================================================
Example :  python predatory_j.py -a Quantization 
'''

import pandas as pd
import argparse, textwrap
import my_debug as DBG
'''
def ArgumentParse(L_Param, _prog='predatory_j.py', _intro_msg=_description, bUseParam=False):
    parser = argparse.ArgumentParser(
        prog='predatory_j.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(_intro_msg))

    parser.add_argument('-jn', '--journal_name', help="(Partial) Journal Name",
                        type=str, default='')

    if bUseParam:
        args = parser.parse_args(L_Param)
    else:
        args = parser.parse_args()

    print(_intro_msg)
    return args
'''

import Interface_function as IF
class P_Journal_Search:
    def __init__(self):
        ArgumentParse           = IF.ArgumentParse
        self.args               = ArgumentParse(L_Param=[], _prog='predatory_j.py', _intro_msg=_description)
        self.debug_on           = True
        # ----------------------------------------------------------------
        # Path and File : example Journal name ; "International Journal of Biotechnology Research"
        #----------------------------------------------------------------
        self.source_excel_file  = "predatory_journal_20231106.xlsx"
        self.number_of_columns  = 6
        self.standard_sheet     = 1
        self.req_chk_sheet      = [0, -1, 1, -1, -1]
        self.column_index       =[['No', '저널명', '출판사', 'ISSN(온라인)', 'ISSN(인쇄물)', 'SCI급 여부', 'Web of Science 분야'], \
                                  ['No', '저널명', '출판사', 'ISSN(온라인)', 'ISSN(인쇄물)', 'SCI급 여부', '연구분야', 'Level']]
        # ----------------------------------------------------------------
        # Fundamental Parameters
        #----------------------------------------------------------------
        print("=================================================================")
        print(" Read the predatory journal list in EXCEL file")
        print("(%s) Please wait" %self.source_excel_file)
        print("=================================================================")
        self.df_sheet_all   = pd.read_excel(self.source_excel_file, sheet_name=None, engine='openpyxl')
        self.df_sheet_name  = list(self.df_sheet_all.keys())
        #self.df_column_axis = self.df_sheet_all[self.df_sheet_name[self.standard_sheet]].columns
        #self.df_row_axis    = self.df_sheet_all[self.df_sheet_name[self.standard_sheet]].index
    def __call__(self, *args, **kwargs):
        _sheet_result = []
        for _sh_idx, _sh_name in enumerate(self.df_sheet_name):
            print("-----------------------------------------------------------------")
            print("%s" %_sh_name)
            print("-----------------------------------------------------------------")
            _local_result = self.find_data_in_sheet(sh_idx=_sh_idx)
            _sheet_result.append(_local_result)
            if _local_result.empty :
                print("Nothing Matched")
            else:
                print("*******  %d Matches Found !! ********" %len(_local_result))
                print(_local_result.to_string(index=False, header=False))

        print("=================================================================")
        print("Final Result")
        print("=================================================================")
        self.printout_result(_sheet_result)

    def find_data_in_sheet(self, sh_idx):
        _jounal_name    = self.args.journal_name
        _sheet_name     = self.df_sheet_name[sh_idx]
        _sheet_df       = self.df_sheet_all[_sheet_name]

        _col_df         = _sheet_df[_sheet_df.isin([_jounal_name]).any(axis=1)]
        _col_data       = _col_df[:self.number_of_columns]

        return _col_data

    def printout_result(self, sh_result):
        for _k, _local_result in enumerate(sh_result):
            if _local_result.empty: pass
            else:
                if self.req_chk_sheet[_k] > 0:
                    _local_result.columns   = self.column_index[self.req_chk_sheet[_k]]
                else: pass
                print(_local_result)

                #print(_local_result.to_string(index=False, header=False))


# =================================================================
# Main Routine
# =================================================================
# For Module processing
if __name__ == '__main__':

    c_work = P_Journal_Search()
    try :
        c_work()
    except Exception as e:
        print("Error Occur!! Error Message : %s" %e)
        exit()