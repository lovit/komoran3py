# Komoran 3 in Python

Komoran 은 Java 로 구현된 한국어 형태소 분석기입니다. 이 프로젝트는 Junsoo Shin 님의 [github](https://github.com/shin285/KOMORAN) 에 공개되어 있습니다. 

[KoNLPy](http://konlpy.org/) 에서도 Komoran 2.x 를 포함하고 있습니다. 

Komoran 에는 사용자 사전 추가 기능이 있습니다. 이 기능을 Python 환경에서도 이용할 수 있도록 하였습니다.

## Usage

KoNLPy 의 함수명을 따라갑니다.

    from komoran3py import Komoran
    komoran = Komoran()
    
    sent = '청하는아이오아이멤버입니다'
    komoran.pos(sent)

단어 '아이오아이'는 미등록단어로, 제대로 인식이 되지 않습니다.

    [('청하', 'VV'),
     ('는', 'ETM'),
     ('아이오', 'NNP'),
     ('아이', 'NNP'),
     ('멤버', 'NNP'),
     ('이', 'VCP'),
     ('ㅂ니다', 'EC')]

사용자 사전을 만듭니다. 사용자 사전은 tap separated 텍스트 파일입니다. <단어, 품사> 형식으로 입력합니다. 만약 품사를 입력하지 않으면 명사 취급이 됩니다.

    아이오아이	NNP

사전을 추가하여 다시 형태소 분석을 수행합니다.

    komoran.set_user_dictionary('./user_dictionary.txt')
    komoran.pos(sent)

단어 '아이오아이'가 제대로 인식됩니다.

    [('청하', 'VV'),
     ('는', 'ETM'),
     ('아이오아이', 'NNP'),
     ('멤버', 'NNP'),
     ('이', 'VCP'),
     ('ㅂ니다', 'EC')]

komoran instance 를 새로 만들면, 사용자 사전의 정보는 초기화됩니다.

    komoran = Komoran()
    komoran.pos(sent)

다시, 단어 '아이오아이'가 제대로 인식되지 않습니다.

    [('청하', 'VV'),
     ('는', 'ETM'),
     ('아이오', 'NNP'),
     ('아이', 'NNP'),
     ('멤버', 'NNP'),
     ('이', 'VCP'),
     ('ㅂ니다', 'EC')]

## KoNLPy update

KoNLPy 0.4.5 에 코모란3가 업데이트 되었습니다. 0.4.5 부터 사용자 사전 추가 기능이 제공됩니다. KoNLPy 의 Komoran 에 사용자 사전을 추가하는 예시코드입니다.

    from konlpy.tag import Komoran

    dicpath = 'YOUR_DICPATH' # 텍스트 파일주소로, 사용자 사전의 구조는 위와 같습니다.
    komoran = Komoran(userdic=dicpath)
    komoran.pos(sent)