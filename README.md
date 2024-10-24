READ ME
===

## 실행 방법

현재 윈도우즈 환경에서 conda 환경으로 실행할 수 있습니다.
Windows PowerShell에서 스크립트 실행 권한이 없을 경우: PowerShell을 관리자 권한으로 실행 후 `Set-ExecutionPolicy RemoteSigned` 명령어를 실행합니다.

### Windows에서 Conda 및 Miniconda로 실행

```ps1
# 환경 설치 스크립트 실행
./install_windows_conda.ps1

# 가상환경에서 실행
./python paper+analysis.py -pn multimodal -tr 1
```

**주의**: MiniConda를 사용하는 경우 conda 도구 경로가 Path에 추가되지 않을 수 있습니다. 이 경우 `Anaconda Powershell Prompt (miniconda3)`를 실행한 뒤 명령어를 실행해주세요.

### Help 
```ps1

usage: paper_analysis.py [-h] [-pn PAPER_NAME] [-tr TRANSLATION]

====================================================
paper_analysis.py : Classical Simulated Annealing Test
                    Written by Jinwuk @ 2022-01-11
====================================================
Example :  python paper_analysis.py -pn Quantization

options:
  -h, --help            show this help message and exit
  -pn PAPER_NAME, --paper_name PAPER_NAME
                        (Partial) Paper Name
  -tr TRANSLATION, --translation TRANSLATION
                        [0] No translation [1] Translation (eng->kor)
```

## Future Work 

이 프로그램을 발전시켜 다수의 논문에 대하여 TXT 파일을 만드는 법에 대하여 업그레드를 수행하겠음
프로그램은 차후 Github에 올리겠음

