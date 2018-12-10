# Komoran 3 in Python

Komoran 은 Java 로 구현된 한국어 형태소 분석기입니다. 이 프로젝트는 Junsoo Shin 님의 [github](https://github.com/shin285/KOMORAN) 에 공개되어 있습니다. 

Komoran 에는 사용자 사전 추가 기능이 있습니다. 이 기능을 Python 환경에서도 이용할 수 있도록 하였습니다. [KoNLPy](http://konlpy.org/) 의 version 0.4.5 까지는 Komoran 2.x 기능을 제공하였습니다. 2018-08-01 이후 KoNLPy 는 0.5.1 로 버전이 올라갔으며, Komoran 에 한하여 사용자 사전의 추가 기능이 제공됩니다. KoNLPy 의 사용자 사전 추가 기능의 이용 방법은 README 의 하단을 참고하세요.

이 repository 역시 KoNLPy 처럼 Python 에서 Java 로 구현된 라이브러리를 이용하기 위한 방법을 포함하고 있습니다. jvm.py 파일의 형식은 KoNLPy 를 참고하였습니다. JPype 를 이용하여 Python 에서 Java 라이브러리들을 이용하기 위한 방법을 알고 싶다면 jvm.py 파일과 [블로그](https://lovit.github.io/nlp/2018/07/06/java_in_python/) 를 보시기 바랍니다.

## Requirements

Jpype1 >= 0.6.2

## Basic usage

KoNLPy 의 함수명을 따라갑니다.

```python
from komoran3py import KomoranPy
komoran = KomoranPy()

sent = '청하는아이오아이멤버입니다'
komoran.pos(sent)
```

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

```python
komoran.set_user_dictionary('./user_dictionary.txt')
komoran.pos(sent)
```

단어 '아이오아이'가 제대로 인식됩니다.

    [('청하', 'VV'),
     ('는', 'ETM'),
     ('아이오아이', 'NNP'),
     ('멤버', 'NNP'),
     ('이', 'VCP'),
     ('ㅂ니다', 'EC')]

komoran instance 를 새로 만들면, 사용자 사전의 정보는 초기화됩니다.

```python
komoran = KomoranPy()
komoran.pos(sent)
```

다시, 단어 '아이오아이'가 제대로 인식되지 않습니다.

    [('청하', 'VV'),
     ('는', 'ETM'),
     ('아이오', 'NNP'),
     ('아이', 'NNP'),
     ('멤버', 'NNP'),
     ('이', 'VCP'),
     ('ㅂ니다', 'EC')]


## Word position and flatten

flatten=False 로 설정하면 띄어쓰기 기준으로 nested list 형태의 결과를 return 합니다. 기본값은 flatten = True 입니다. 어절 단위의 단어를 확인할 수 있습니다.

```python
sent = '청하는 아이오아이 멤버입니다'
komoran.pos(sent, flatten=False)
```

    [[('청하', 'VV'), ('는', 'ETM')],
     [('아이오아이', 'NNP')],
     [('멤버', 'NNP'), ('이', 'VCP'), ('ㅂ니다', 'EC')]]

position = True 로 설정하면 각 단어의 position 을 알 수 있습니다. 기본값은 position = False 입니다.

```python
komoran.pos(sent, flatten=False, position=True)
```

    [[('청하', 'VV', 0, 2), ('는', 'ETM', 2, 3)],
     [('아이오아이', 'NNP', 4, 9)],
     [('멤버', 'NNP', 10, 12), ('이', 'VCP', 12, 13), ('ㅂ니다', 'EC', 12, 15)]]

flatten = True 로 설정하였을 때에도 position = True 설정이 가능합니다.

```python
komoran.pos(sent, flatten=True, position=True)
```

    [('청하', 'VV', 0, 2),
     ('는', 'ETM', 2, 3),
     ('아이오아이', 'NNP', 4, 9),
     ('멤버', 'NNP', 10, 12),
     ('이', 'VCP', 12, 13),
     ('ㅂ니다', 'EC', 12, 15)]


## KoNLPy update

KoNLPy 0.5.0 에 코모란3가 업데이트 되었습니다. 0.5.0 부터 사용자 사전 추가 기능이 제공됩니다. KoNLPy 의 Komoran 에 사용자 사전을 추가하는 예시코드입니다.

```python
from konlpy.tag import Komoran

dicpath = 'YOUR_DICPATH' # 텍스트 파일주소로, 사용자 사전의 구조는 위와 같습니다.
komoran = Komoran(userdic=dicpath)
komoran.pos(sent)
```
