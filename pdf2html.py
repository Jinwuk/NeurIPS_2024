#!/usr/bin/python
# -*- coding: utf-8 -*-
###########################################################################
# Paper Nalysis for Neurips 2024
# For the conversion of pdf to HTML
# I refer the web-site : https://medium.com/@alexaae9/convert-pdf-to-html-with-python-developer-guide-681fb98ba40d
# 2024 12 25 by Jinwuk Seok
###########################################################################
_description = '''\
====================================================
pdf2html.py : PDF to HTML 
                    Written by Jinwuk @ 2024-12-25
====================================================
Example :  python pdf2html.py -ip some.pdf 
'''
from spire.pdf.common import *
from spire.pdf import *
from bs4 import BeautifulSoup
import os, re
import Interface_function as IF
import my_debug as DBG

_basic_line = "----------------------------------------------------------------"
class pdf2html:
    def __init__(self):
        # ----------------------------------------------------------------
        # Path and File
        #----------------------------------------------------------------
        self.work_path  = os.getcwd()
        self.outfile    = ""
        # ----------------------------------------------------------------
        # Paeameters
        #----------------------------------------------------------------
        _ext_tag        = ['.html', '.txt']
        ArgumentParse   = IF.ArgumentParse
        self.args       = ArgumentParse(L_Param=[], _prog='paper_analysis.py', _intro_msg=_description)
        self.input_pdf  = self.args.input_file
        _output_html    = self.get_filename_without_extension() + _ext_tag[self.args.operation_mode]
        self.output_html=os.path.join("output", _output_html)
        # ----------------------------------------------------------------
        # _useEmbeddedSvg = True
        # _useEmbededImg  = True if _useEmbeddedSvg is False else True
        # _maxPageOneFile  = 1 if _useEmbeddedSvg is False else 1
        # _useHighQualityEmbeddedSvg = True if _useEmbeddedSvg is True else True
        # ----------------------------------------------------------------
        # Initilization and Load PDF file
        # ----------------------------------------------------------------
        # Create a Document object
        self.doc = PdfDocument()
        # Load a PDF document
        self.doc.LoadFromFile(self.input_pdf)
        # Operation Function
        self.l_op_func = [self.local_pdf_to_html, self.local_pdf_to_text]

        print("=================================================================")
        print(" Initialization ")
        print("  Input  PDF  File     : %s" %self.input_pdf)
        print("  Output HTML File     : %s" %self.output_html)
        print("=================================================================")

    def __call__(self, *args, **kwargs):
        self.l_op_func[self.args.operation_mode]()
    def __del__(self):
        self.doc.Dispose()
        return

    def get_filename_without_extension(self):
        # 파일 이름과 확장자를 분리
        file_name, file_extension = os.path.splitext(os.path.basename(self.input_pdf))
        if file_extension != '.pdf':
            print(_basic_line)
            print("The file extension of the input file is not pdf")
            print("The extension of the input file is %s" %(file_extension))
            print("please check the file extention carefully")
            print(_basic_line)
            exit(0)
        else: pass
        return file_name

    def local_pdf_to_html(self, _useEmbeddedSvg=True, _useEmbededImg=True, _useHighQualityEmbeddedSvg=True):
        # Set the conversion options to
        self.convertOptions = self.doc.ConvertOptions
        # Specify convert options
        self.convertOptions.SetPdfToHtmlOptions(_useEmbeddedSvg, _useEmbededImg, 1, _useHighQualityEmbeddedSvg)
        # Save the PDF document to HTML format
        self.doc.SaveToFile(self.output_html, FileFormat.HTML)
        # Extract and warning from Spire.PDF
        self.extract_warning(_operation=True)

    def local_pdf_to_text(self):
        # Iterate through the pages in the document
        for i in range(self.doc.Pages.Count):
            # Get a specific page
            page = self.doc.Pages[i]
            # Create a PdfTextExtractor object
            textExtractor = PdfTextExtractor(page)
            # Create a PdfTextExtractOptions object
            extractOptions = PdfTextExtractOptions()
            # Set IsExtractAllText to Ture
            extractOptions.IsExtractAllText = True
            # Extract text from the page keeping white spaces
            text = textExtractor.ExtractText(extractOptions)
            # Post Processing
            post_text_lines =[]
            text_lines = text.split("\r\n")
            for _test_line in text_lines:
                # Extract Spire.PDF
                if "Spire.PDF" in _test_line: pass
                else:
                    post_text_lines.append(re.sub(r'\s{2,}', '', _test_line))
                    #print(post_text_lines[-1])
            # Write text to a txt file
            with open('output/TextOfPage-{}.txt'.format(i + 1), 'w',encoding='UTF-8') as file:
                for line in post_text_lines:
                    if line != ',':
                        file.write(line + "\n")
                    else: pass

        self.doc.Close()

    def extract_warning(self, _operation=True):
        if _operation :
            # HTML File Read
            try:
                with open(self.output_html, "r", encoding='UTF-8') as f:
                    _html_txt = f.read()
            except Exception as e:
                print(e)
                exit()
            # Find <g> and other keywords
            _debug_cnt = 0
            soup = BeautifulSoup(_html_txt, 'html.parser')
            # 모든 <g> 태그를 찾고, 그 중 "Spire.pdf" 만 있는 <g> tag 추출
            for g_tag in soup.find_all('g'):
                for sub_g_tag in g_tag.find_all('g'):
                    if "Spire.PDF" in sub_g_tag.text:
                        _debug_cnt += 1
                        sub_g_tag.decompose()
                    else: pass
            # Save HTML File
            try:
                with open(self.output_html, "w", encoding='UTF-8') as file:
                    file.write(soup.prettify())
            except Exception as e:
                print(e)
                exit()

            print("Process Finished %d" %_debug_cnt)
        else:
            print("No Extract warnings")


# =================================================================
# Main Routine
# =================================================================
# For Module processing
if __name__ == '__main__':

    c_work = pdf2html()
    try :
        c_work()
    except Exception as e:
        print("Error Occur!! Error Message : %s" %e)
        exit()

    del c_work
