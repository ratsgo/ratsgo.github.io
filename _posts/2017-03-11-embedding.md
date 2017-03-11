---
html header: <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
title: 빈도수 세기의 놀라운 마법 Word2Vec, Glove, Fasttext 
category: From frequency to semantics
tag: embedding methods
---

안녕하세요. 이번 포스팅에서는 단어를 벡터화하는 **임베딩(embedding)** 방법론인 **Word2Vec, Glove, Fasttext**에 대해 알아보고자 합니다. 세 방법론이 크고 작은 차이점을 갖고 있지만 '단어 빈도수 세기'라는 점에서 본질적으로 같다는 점을 이야기해보려고 합니다. 저는 이 사실을 처음 깨닫고 나서 놀라움을 금치 못했었는데요. 자, 이제 시작해 볼까요.



## Word2vec

Word2Vec은 지난번 [포스트](https://ratsgo.github.io/natural%20language%20processing/2017/03/08/word2vec/)에서 언급한 것처럼 단어를 벡터로 바꾸는 방법론입니다. 크게 **CBOW(Continous Bag of Words)**와 **Skip-Gram** 두 가지 방식이 있습니다. 전자는 주변에 있는 단어들을 가지고 중심에 있는 단어를 맞추는 방식이고, 후자는 중심에 있는 단어로 주변 단어를 예측하는 방법입니다. 예를 들어 보겠습니다.

> 나는 ______에 간다.

위 문장에 들어갈 수 있는 단어는 다양합니다. '학교'일 수도, '집'일 수도 있죠. '회사'일 수도 있습니다. 이렇듯 주변 단어를 가지고 중심에 있는 단어를 맞춤으로써 단어 벡터들을 만들어 내는 방법이 CBOW입니다. 반대로 아래처럼 '슈퍼파월' 앞뒤로 어떤 단어가 올지 예측하는 방법은 Skip-Gram입니다.

> ______  슈퍼파월 ______

'슈퍼파월' 앞에는 어떤 단어가 올 가능성이 높을까요? 유행어를 아시는 분이라면 '힘을 내요'를 떠올리시겠지요. 실제로 말뭉치에서 '슈퍼파월' 앞에 '힘을 내요'라는 표현이 등장했다고 칩시다. 그러면 Word2Vec은 '슈퍼파월'이 '힘을 내요'와 어떤 연관이 있다고 보고 이를 감안해서 단어를 벡터로 만들게 됩니다.

여기서 하나 같이 고민해볼 문제가 있습니다. '슈퍼파월'은 '힘을 내요'와 비슷한 표현(단어)라고 볼 수 있을까요? 정답이 없는 문제입니다만, 제 생각엔 그렇다고 볼 수도 있을 것 같습니다. 두 표현은 동시에 같이 쓰이는 일종의 **연어(collocation)**로써 대체로 격려하는 상황에 자주 사용되기 때문입니다. (물론 의미가 엄밀하게 같지는 않습니다) 

Word2Vec은 **자연언어처리(Natural Language Processing)**의 대표적인 가정인 **[Distributional Hypothesis](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/frequency/)**(비슷한 맥락이나 위치에 등장하는 단어들은 그 의미도 유사하다)에 근거한 방법론입니다. Word2Vec은 어떤 방식으로 학습하고, 단어 벡터들을 만들어내는 걸까요? 최대한 직관적으로 설명해보려고 합니다. Word2Vec은 아래 식을 최대화하는 걸 목표로 합니다.

\\( p(o|c)=\frac { exp({ u }_{ o }^{ T }{ v }_{ c }) }{ \sum _{ w=1 }^{ W }{ exp({ u }_{ w }^{ T }{ v }_{ c } } ) } \\)