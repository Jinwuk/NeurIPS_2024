#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################
# Paper Nalysis for Neurips 2024
# Working Directory : C:\Users\Admin\OneDrive\문서\Document\[001]_Reserach자료\[01] My_Research\[01_01] MyPapers\2024\Neurips_python_work
# 2024 10 24 by Jinwuk Seok
###########################################################################
_description = '''\
====================================================
paper_analysis.py : Classical Simulated Annealing Test
                    Written by Jinwuk @ 2022-01-11
====================================================
Example :  python paper_analysis.py -pn Quantization 
'''
from deep_translator import GoogleTranslator
import keyboard
import json
import os
import re
import argparse, textwrap
import my_debug as DBG

def ArgumentParse(L_Param, _intro_msg=_description, bUseParam=False):
    parser = argparse.ArgumentParser(
        prog='paper_analysis.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(_intro_msg))

    parser.add_argument('-pn', '--paper_name', help="(Partial) Paper Name",
                        type=str, default='')
    parser.add_argument('-tr', '--translation', help="[0] No translation [1] Translation (eng->kor)",
                        type=int, default=0)

    if bUseParam:
        args = parser.parse_args(L_Param)
    else:
        args = parser.parse_args()

    args.translation   = True if args.translation == 1 else False

    print(_intro_msg)
    return args

class   neurips_paper:
    def __init__(self, _work_file='neurips_2024_papers.json'):
        # ----------------------------------------------------------------
        # Path and File
        #----------------------------------------------------------------
        self.work_path  = os.getcwd()
        self.work_file  = _work_file
        self.work_fullpath = os.path.join(self.work_path, self.work_file)
        # ----------------------------------------------------------------
        # Paeameters
        #----------------------------------------------------------------
        self.args       = ArgumentParse(L_Param=[])
        with open(self.work_fullpath, 'r', encoding='utf-8') as file:
            self.data_dict = json.load(file)        #'count', 'next', 'previous' 'results'
        self.data_results  = self.data_dict['results']
        self.search_result = []
        self.use_dict      = {}
        self.generate_use_dictionary()


        print("=================================================================")
        print(" Initialization ")
        print("  Work File        : %s" %self.work_file)
        print("  Neumbe of Papers : %d" %self.data_dict['count'])
        print(" When you input 'ESC' Key and Enter, the program will be terminated.")
        print("=================================================================")

    def __call__(self):

        self.search_result = self.search_papers()

        print("=================================================================")
        print(" Search List : ")
        for _k, _search_result in enumerate(self.search_result):
            print("%4d : %s" % (_k, _search_result['name']))
        print("=================================================================")

        _process_go = True
        while(_process_go):
            _index          = int(input("Enter the Number of the above File list :"))
            d_target_paper  = self.search_result[_index]
            self.write_info_dictionary(_data_dict=d_target_paper)
            l_result_str    = self.generate_result_string()
            _translated_str = self.translate_abstract(_dictionary=d_target_paper, _active=self.args.translation)

            for _value in l_result_str:
                print(_value)

            l_abstract = []
            if self.args.translation:
                l_abstract.append("----------------------------------------------------------------")
                l_abstract.append("Abstract ")
                l_abstract.append("----------------------------------------------------------------")
                l_abstract.append("%s" %d_target_paper['abstract'])
                l_abstract.append("----------------------------------------------------------------")
                l_abstract.append("Translated Abstract ")
                l_abstract.append("----------------------------------------------------------------")
                l_abstract.append("%s" %_translated_str)
                l_abstract.append("----------------------------------------------------------------")

                for _value in l_abstract:
                    print(_value)
            else: pass


            if keyboard.is_pressed('esc'):
                print("ESC pressed Exit Program")
                break
            else: pass


        print("=================================================================")
        DBG.dbg("   Debugging ", _active=True)
        DBG.dbg("   Number of Search Results: %d" %len(self.search_result))
        print("=================================================================")

    def generate_use_dictionary(self):
        self.use_dict['id']         = 0
        self.use_dict['name']       = ''
        self.use_dict['abstract']   = ''
        self.use_dict['session']    = ''
        self.use_dict['eventtype']  = ''
        self.use_dict['starttime']  = ''
        self.use_dict['endtime']    = ''

    def write_info_dictionary(self, _data_dict):
        self.use_dict['id']         = _data_dict['id']
        self.use_dict['name']       = _data_dict['name']
        self.use_dict['abstract']   = _data_dict['abstract']
        self.use_dict['session']    = _data_dict['session']
        self.use_dict['eventtype']  = _data_dict['eventtype']
        self.use_dict['starttime']  = _data_dict['starttime']
        self.use_dict['endtime']    = _data_dict['endtime']

    def generate_result_string(self):
        l_result_str =[]
        l_result_str.append("Paper ID   : %4d" %self.use_dict['id'])
        l_result_str.append("Paper Name : %s" % self.use_dict['name'])
        l_result_str.append("Session    : %s" % self.use_dict['session'])
        l_result_str.append("Event Type : %s" % self.use_dict['eventtype'])
        l_result_str.append("Start Time : %s" % self.use_dict['starttime'])
        l_result_str.append("End Time   : %s" % self.use_dict['endtime'])
        return l_result_str

    def translate_abstract(self, _dictionary, _active=False):
        _return_val = ''
        _text = _dictionary['abstract']
        if _active :
            translator = GoogleTranslator(source='en', target='ko')
            translated = translator.translate(_text)
            _return_val= translated
        else: pass

        return _return_val

    def search_papers(self):
        _result = []
        _part_paper_name = self.args.paper_name
        for _num, _dict in enumerate(self.data_results):
            b_match = re.search(_part_paper_name, _dict['name'], re.IGNORECASE)
            if b_match : _result.append(_dict)
            else       : pass

        return _result


# =================================================================
# Main Routine
# =================================================================
# For Module processing
if __name__ == '__main__':

    c_work = neurips_paper()
    try :
        c_work()
    except Exception as e:
        print("Error Occur!! Error Message : %s" %e)
        exit()
