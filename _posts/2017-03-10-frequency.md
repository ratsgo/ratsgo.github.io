---
title: idea of statistical semantics
category: From frequency to semantics
tag: distributional hypothesis
---

이번 포스팅에서는 **자연언어처리(Natural Language Processing)**의 기본 가정 가운데 하나인 **distributional hypothesis**와 **벡터공간모델(Vector Space Models)**에 대해 알아보도록 하겠습니다. 그 핵심은 '빈도'를 '의미'로 진화시킬 수 있다는 아이디어인데요. 이와 아울러 NLP 분야에서 생각하는 **유사도(similarity)**와 NLP의 기본 절차에 대해서도 이야기해보겠습니다. 이와 관련해 괜찮은 [아티클](http://www.jair.org/media/2934/live-2934-4846-jair.pdf)이 있어 공부 겸 소개 겸 정리를 해볼까 합니다. 



## NLP의 기본 가정

NLP 분야의 기본 가정들을 소개합니다.

> VSMs : 문서 집합에 속하는 각각의 문서들을 벡터공간의 벡터로 표현(representation)할 수 있다. 벡터공간에 벡터로 표현된 문서들 사이의 거리가 가깝다면 의미가 유사하다(semantically similar).

> distributional hypothesis : 비슷한 맥락에 등장하는 단어들은 유사한 의미를 지니는 경향이 있다. (words that occur in similar contexts tend to have similar meanings)

> statistical semantics hypothesis : 언어 사용의 통계적 패턴은 사람들이 의미하는 바를 이해하는 데 쓰일 수 있다. (statistical patterns of human word usage can be used to figure out what people mean)

> bag of words hypothesis : 어떤 문서에 출현한 단어들의 빈도는 문서와 쿼리의 관련성을 나타내는 경향이 있다. (the frequencies of words in a document tend to indicate the relevance of the document to a query) 어떤 문서가 쿼리 문서와 유사한 벡터라면 그 의미도 비슷하다.

> Latent relation hypothesis : 비슷한 패턴으로 동시에 등장하는 단어쌍은 유사한 의미적 관계를 지니는 경향이 있다. (Pairs of words that co-occur in similar patterns tend to have similar semantic relations)

음, 뭔가 어렵죠? 사실 그 말이 그 말인 것 같고요. 위 내용을 종합해 저만의 언어로 풀어서 이야기하자면, 분석 대상 말뭉치 내 등장하는 단어들의 빈도를 세서 이를 벡터 형태로 바꿀 수 있고, 그 벡터들 간의 거리(유사도)를 잴 수 있으며, 이렇게 구한 거리는 언어학적인 의미를 내포한다는 이야기인 것 같습니다. 바꿔 말하면 컴퓨터는 그저 단어를 '숫자'로 바꿔서 '계산'할 뿐이지만 이 과정에서 자연언어의 '의미'도 '이해'할 수 있다는 가정인 셈이지요. 

뒤에서 설명드릴 **단어-문서행렬(Term-Document Matrix)**, **단어-문맥행렬(Word-Context Matrix)**,  **페어-패턴행렬(Pair-Pattern Matrix)** 등은 모두 위 가정을 전제로 한 분석 방법론입니다. [**Word2Vec, Glove, Fasttext**](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/11/embedding/) 또한 마찬가지인 것 같습니다. 이들 방법론은 문맥 단어가 주어졌을 때 분석 대상 단어가 등장할 조건부 확률, 혹은 동시에 등장하는 빈도 따위를 보존하는 방식으로 단어를 벡터화하는 데 이 방법론의 대전제가 위의 가정에서 크게 벗어난 것 같지는 않다는 생각에서입니다. 어쨌든 단어의 의미를 숫자로, 언어학을 컴퓨터 사이언스로 문제와 해결방식을 각각 근본적으로 바꿨다는 점에서 괜찮은 아이디어인 것 같습니다~~물론 이 가정이 틀렸다는 게 엄밀하게 증명된다면 다른 얘기겠지만~~.



## 단어-문서행렬

수학에서 **bag**은 **set**과 유사한 개념입니다. 예컨대 bag {a, a, b, c, c, c}와 bag {c, a, c, b, a, c}는 같습니다. 즉 빈도는 고려하지만 등장 순서는 무시한다는 거죠. 이 때문에 단어-문서행렬을 **bag of words** 기반의 방법론이라고도 합니다. 단어들을 일종의 주머니(bag)에 넣어 둔다는 의미 정도로 해석할 수 있겠는데, 한번 주머니에 들어가면 순서가 뒤죽박죽 섞이기 때문에 이런 용어가 생긴 것 같습니다. 예를 들어 다음과 같은 단어들로 이뤄진 문장이 있다고 칩시다. 그럼 우리는 다음과 같은 단어-문서행렬을 만들 수 있습니다.

> 나,는,학교,에,가,ㄴ,다

> 학교,에,가,는,영희

> 나,는,영희,는,좋,다

|  -   | doc1 | doc2 | doc3 |
| :--: | :--: | :--: | :--: |
|  나   |  1   |  0   |  0   |
|  는   |  1   |  1   |  2   |
|  학교  |  1   |  1   |  0   |
|  에   |  1   |  1   |  0   |
|  가   |  1   |  1   |  0   |
|  ㄴ   |  1   |  0   |  0   |
|  다   |  1   |  0   |  1   |
|  영희  |  0   |  1   |  1   |
|  가   |  0   |  0   |  0   |
|  좋   |  0   |  0   |  1   |





## 단어-문맥행렬

주변 단어를 몇 개 볼 지(window size)를 정하고 동시에 등장하는 단어의 빈도수를 세어서 행렬로 바꾸는 방법입니다. window 개념이 있기 때문에 단어-문서행렬과 달리 단어 등장 순서를 약간 고려하긴 합니다. 이 방법론은 **distributional hypothesis**와 밀접한 관련이 있습니다. 예시는 다음과 같습니다(window size = 1).

> I enjoy flying

> I like NLP

> I like deep learning

|    -     |  I   | like | enjoy | deep | learing | NLP  | flying |
| :------: | :--: | :--: | :---: | :--: | :-----: | :--: | :----: |
|    I     |  0   |  2   |   1   |  0   |    0    |  0   |   0    |
|   like   |  2   |  0   |   0   |  1   |    0    |  1   |   0    |
|  enjoy   |  1   |  0   |   0   |  0   |    0    |  0   |   0    |
|   deep   |  0   |  1   |   0   |  0   |    1    |  0   |   1    |
| learning |  0   |  0   |   0   |  1   |    0    |  0   |   0    |
|   NLP    |  0   |  1   |   0   |  0   |    0    |  0   |   0    |
|  flying  |  0   |  0   |   1   |  0   |    0    |  1   |   0    |





## 페어-패턴행렬

페어-패턴행렬의 행 벡터는 단어쌍(pairs of words)을 의미합니다. 예컨대 mason:stone, carpenter:word 따위가 되겠죠. 단어쌍에 대응되는 열 벡터는 해당 단어쌍과 함께 나타나는 패턴(patterns)을 뜻합니다. "X cuts Y", "X works with Y" 등입니다. 이 행렬을 제대로 구축해놓으면 특정 패턴(예컨대 X solves Y)와 비슷한 패턴(Y is solved by Y)을 가려낼 수 있습니다.





## 유사도?

**'단어 뜻이 비슷하다'**는 어떤 의미를 지니는 걸까요. 생각해보면 볼수록 알쏭달쏭한 개념입니다. 우선 제가 지금 설명드리고 있는 아티클을 기본으로 해서 제 생각을 정리해 말씀드려 보겠습니다. 단어들끼리는 어떤 관련을 맺고 있습니다. 엄밀히 얘기하면 이 세상에 완벽한 동의어는 없다고 말할 수 있을 정도로요. 심지어 **반의어(antonyms)**들조차 단어 사이의 관련성이 높습니다. 

예를 들어 보죠. '춥다'와 '따뜻하다'는 반대되는 말이지 않습니까? 그렇다면 이 둘은 관계가 전혀 없을까요? '기온'을 언급한다는 점에 있어서는 비교적 강한 관계를 지닌다고 말할 수 있겠습니다. '흑'과 '백', '크다'와 '작다'도 마찬가지로 '색상', '크기' 등과 관련해 관계를 맺고 있습니다.

지금 소개해드리고 있는 아티클은 단어 유사성과 관련해 다양한 개념들이 설명하고 있습니다. 우선 **relational similarity**와 **attributional similarity**가 있습니다.'개:멍멍', '개:늑대'가 각각 전자와 후자의 대표 사례입니다. 전자는 단어 사이의 '관계'에, 후자는 '속성'에 방점을 둔 유사성 개념이라고 합니다. **유의어(synonyms)**, **부분어(meronyms)**, **반의어(antonyms)** 등에서 알 수 있듯 모든 단어는 서로 밀접한 관계를 맺고 있습니다.

NLP 분야에서는 **상위어(hypernym)**를 공유하는 단어들이 **의미적 유사성(semantic simliarity)**을 지닌다고 정의한다고 합니다. 이 기준에 따르면 '자동차'와 '자전거'는 의미가 비슷한 단어입니다. '교통수단'이라는 상위어를 공유하기 때문입니다. 이 의미적 유사성이라는 개념은 앞서 언급한 attributional simliarity의 특수한 사례입니다. 또한 '벌'과 '꿀'처럼 동시에 빈번하게 같이 등장하는 단어들은 의미적으로 연관이 있을 가능성이 높다는 것이 이 분야의 대표적인 가정입니다.
