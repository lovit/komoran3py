import os
import jpype
from komoran3py.jvm import init_jvm

class KomoranPy:

    def __init__(self, jvmpath=None, max_heap=1024):

        init_jvm(jvmpath=jvmpath, max_heap=max_heap)
        package = jpype.JPackage('kr.co.shineware.nlp.komoran.core')
        model_path = os.path.dirname(os.path.realpath(__file__)) + '/models/'
        self._komoran = package.Komoran(model_path)

    def set_user_dictionary(self, path):
        """
        Arguments
        ---------
        path : str
            dictionary file path
        """
        self._komoran.setUserDic(path)

    def pos(self, sent, flatten=True, position=False):
        """
        Arguments
        ---------
        sent : str
            Input sentence

        flatten : Boolean
            If True, pos function returns list of words
            Else, this function returns nested list. [[words in eojeol] for eojeol in sent]

                > komoran = KomoranPy()
                > komoran.pos('테스트 입니다', flatten=False)
                $ [[('테스트', 'NNP', 0, 3)],
                   [('이', 'VV', 4, 5), ('ㅂ니다', 'EC', 4, 6)]]

            Default is True

        position : Boolean
            If True, the result of pos function contains begin and end position of each word

                > komoran.pos('테스트 입니다', position=True)
                $ [('테스트', 'NNP', 0, 3), ('이', 'VV', 4, 5), ('ㅂ니다', 'EC', 4, 6)]]

                > komoran.pos('테스트 입니다', position=False)
                $ [('테스트', 'NNP'), ('이', 'VV'), ('ㅂ니다', 'EC')]]

            Default is False
        """

        try:
            tokens = self._komoran.analyze(sent).getTokenList()
        except Exception as e:
            print(e)
            return []

        tokens = [(token.getMorph(),
                   token.getPos(),
                   token.getBeginIndex(),
                   token.getEndIndex())
                  for token in tokens]

        if flatten:
            if not position:
                tokens = [token[:2] for token in tokens]
            return tokens

        tokens_ = []
        eojeol = []
        for i, token in enumerate(tokens):
            if i > 0 and token[2] > tokens[i-1][3] and eojeol:
                tokens_.append(eojeol)
                eojeol = []
            eojeol.append(token)
        tokens_.append(eojeol)

        if not position:
            tokens_ = [[token[:2] for token in tokens] for tokens in tokens_]

        return tokens_