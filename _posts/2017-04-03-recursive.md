---
title: Recursive Neural Networks
category: Deep Learning
tag: Recursive Neural Networks
html header: <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_SVG"></script>
---

이번 포스팅에선 **Recursive Neural Networks(RNN)**에 대해 다뤄보려고 합니다. RNN은 **Recurrent Neural Networks**와 더불어 최근 자연언어처리 분야에서 각광받고 있는 모델인데요. 두 모델 모두 음성, 문자 등 순차적 데이터 처리에 강점을 지니고 있고 이름마저 유사해서 헷갈릴 수 있겠습니다만, 조금 차이가 있는 모델입니다. Recurrent Neural Networks에 대한 자세한 내용은 [이곳](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/)을 참고하시기 바랍니다. 이번 글은 미국 스탠포드대학의 [CS224d](http://cs224d.stanford.edu/) 강의를 참고로 하되 순전파와 역전파 계산그래프는 제가 작성했음을 먼저 밝힙니다. 그럼 시작하겠습니다.



## recurrent vs convolutional vs recursive

<a href="http://imgur.com/MmQRH38"><img src="http://i.imgur.com/MmQRH38.png" width="500px" title="source: imgur.com" /></a>

Recurrent Neural Networks는 입력값을 순서대로 받아 하나씩 순차적으로 처리하는 네트워크 구조입니다. 위 그림처럼 'the country of my birth'라는 입력이 있을 때 첫 입력값은 'the'에 대응하는 단어벡터, 그 다음은 'country', 이후엔 각각 'of', 'my', 'birth'가 됩니다. 그림을 보시면 아시겠지만 입력값 중간에 건너뛰거나 하는 부분이 없고 등장순서대로 그대로 처리하는 구조입니다. 그리고 위 예시에선 은닉층이 하나인 구조를 띄고 있는데요, 마지막 히든 노드인 (2.5, 3.8)은 이전까지의 모든 맥락(the, country, of, my)과 함께 현재 입력값(birth) 정보가 모두 반영된 것을 알 수 있습니다.

<a href="http://imgur.com/lb6M5Ov"><img src="http://i.imgur.com/lb6M5Ov.png" width="500px" title="source: imgur.com" /></a>

이제 **Convolutional Neural Networks(CNN)**를 볼까요? 입력값을 생략없이 모두 반영한다는 점에서는 Recurrent Neural Networks와 큰 차이는 없습니다. 하지만 입력값을 하나씩(the, country...) 보는 Recurrent Neural Networks와 달리 CNN은 위 그림을 보면 2개 단어씩(the country, country of, of my...) 한번에 분석하고 있는 것을 알 수 있죠. 이건 **필터(filter)**라는 존재 때문입니다. 여기서는 필터의 크기가 단어 2개로 세팅되어 있는데, 이 필터가 한칸씩 슬라이딩하면서 문장을 단어 두개씩 읽어들여 분석하는 구조입니다. Recurrent Neural Networks는 입력값이 순차적으로 주어지는 데 반해 CNN은 입력값이 한번에 주어지고 필터가 슬라이딩하면서 문장의 지역적인 정보를 반영한다는 점도 조금 다른 점입니다. 위 그림에서 삼각형의 상단 꼭지점에 해당하는 (3,3.5)가 이 문장의 전체 정보가 모두 반영된 벡터입니다.

<a href="http://imgur.com/bfVzTm5"><img src="http://i.imgur.com/bfVzTm5.png" width="500px" title="source: imgur.com" /></a>

Recursive Neural Networks(RNN)은 입력값으로 주어지는 몇 개 단어를 묶어서 분석한다는 점에 있어서는 CNN과 유사합니다. 하지만 CNN이 모든 지역정보를 생략없이 반영하는 데 비해 RNN은 일부 정보는 스킵한다는 점에 큰 차이를 보입니다. 예컨대 위 예시에서 'the country'는 'of my birth'의 수식을 받는 구조입니다. 또 'the country', 'my birth'는 'country of'나 'of my'보다는 응집성이 높은 표현입니다. CNN의 방식처럼 'the country', 'country of', 'of my'... 이렇게 모두 분석할 필요가 없다는 것이지요. RNN은 이러한 언어의 **hiarchy**한 성질을 네트워크 구조에 적극 차용한 모델이라고 볼 수 있습니다. 

실제로 언어학에서는 문장을 아래와 같이 계층적으로 나누어 분석하고 있습니다. 한국어 파싱과 관련해서는 [이곳](https://ratsgo.github.io/korean%20linguistics/2017/04/29/parsing/)을 참고하면 좋을 것 같습니다.

<a href="http://imgur.com/Himmgu4"><img src="http://i.imgur.com/Himmgu4.png" width="500px" title="source: imgur.com" /></a>

다만 RNN은 Recurrent Neural Networks나 CNN과 달리 트리 구조의 입력값을 반드시 필요로 합니다. 예컨대 아래와 같은데요. 이런 구조의 데이터를 생성하려면 대단히 많은 시간과 비용을 들여야 하는데다 계산도 복잡하기 때문에 RNN이 CNN이나 Recurrent Neural Networks에 비해 주목을 덜 받는 경향이 있는 것 같습니다.

> ( ( ( The ) ( actors ) ) ( ( ( are ) ( fantastic ) ) ( . ) ) )

마지막으로 Recurrent Neural Networks는 Recursive Neural Networks의 특수 케이스라는 점을 짚어보겠습니다. 만약 Recursive Neural Networks가 모든 지역정보를 순서대로 빠짐없이 반영한다고 하면 아래와 같이 구조를 그릴 수 있는데요, 이를 각도 회전해놓고 보면 본질적으로 Recurrent Neural Networks와 같습니다.

<a href="http://imgur.com/AwJAPQ0"><img src="http://i.imgur.com/AwJAPQ0.png" width="500px" title="source: imgur.com" /></a>



## Simple RNN의 구조

RNN은 다음과 같이 여러 단어의 결합으로 이뤄진 표현을 벡터공간에 임베딩해 **파싱(parsing)**, **감성분석(sentiment analysis)** 등 특정과업을 수행하는 걸 목표로 합니다.

<a href="http://imgur.com/2Vz4mg0"><img src="http://i.imgur.com/2Vz4mg0.png" width="500px" title="source: imgur.com" /></a>

가장 간단한 형태의 Simple RNN 구조는 아래 그림처럼 나타낼 수 있습니다.

<a href="http://imgur.com/2InLlzA"><img src="http://i.imgur.com/2InLlzA.png" width="600px" title="source: imgur.com" /></a>

위 그림을 천천히 살펴보면 **자식노드(child node)**에 해당하는 단어벡터 $c_1$과 $c_2$가 1차적으로 **부모노드(parent node)** $p_1$으로 합쳐지고, $c_3$는 $p_1$과 함께 $p_2$를 만들고 있음 확인할 수 있습니다. RNN은 부모노드를 만들 때마다 점수(score)도 함께 생성합니다. 만약 파싱을 위한 RNN이라면 이 스코어는 합쳐진 단어들이 얼마나 말이 되는지를 나타내는 점수가 될 것이고, 감성분석을 위한 RNN이라면 해당 점수는 긍/부정 극성을 나타내는 지표가 됩니다.

한편 $p_2$는 또 다른 부모노드와 합쳐지기 위해 또 다시 분석대상이 됩니다. 이를 도식화한 것이 우측 상단의 그림인데요, 실선 방향은 계산그래프의 **forward pass**, 점선 방향은 그래디언트가 전파되는 **backward pass**로 이해하시면 좋을 것 같습니다. 

$i$번째 부모노드인 $p_i$의 값은 아래처럼 정의됩니다. 각 파라메터의 차원수 또한 아래처럼 정의됩니다. 아래 식에서 pleft와 pright는 각각 $i$번째 부모노드의 좌측, 우측 자식노드입니다. 위 그림 기준으로 하면 $p_2$의 pleft는 $c_3$, pright는 $p_1$이 되는 셈이죠. $d$는 은닉층의 차원수로서 사용자가 지정해주는 하이퍼파라메터입니다. 

$${ p }_{ i }=\tanh { (W\cdot \begin{bmatrix} { p }_{ left } \\ { p }_{ right } \end{bmatrix}+b) } \\ { p }_{ i }\in { R }^{ d },\quad b\in { R }^{ d },\quad W\in { R }^{ d\times 2d }\quad  $$

위 식에서 $W$와 pleft, pright의 결합은 아래와 같습니다.

$$W\cdot \begin{bmatrix} { p }_{ left } \\ { p }_{ right } \end{bmatrix}=\begin{bmatrix} { w }_{ 1 } & { w }_{ 2 } \end{bmatrix}\cdot \begin{bmatrix} { p }_{ left } \\ { p }_{ right } \end{bmatrix}={ w }_{ 1 }{ \times p }_{ left }+{ w }_{ 2 }{ \times p }_{ right }$$

$i$번째 부모노드의 스코어, $s_i$를 구하는 식은 다음과 같습니다.

$${ s }_{ i }={ W }_{ s }{ p }_{ i }+{ b }_{ s }$$

RNN은 이렇게 부모노드로부터 계산된 스코어와 해당 부분에 해당하는 정답 레이블과 비교한 후 오차를 최소화하는 방향으로 **역전파(backpropagation)**를 수행해 파라메터($W$, $b$, $W_s$, $b_s$)를 업데이트하는 방식으로 학습을 합니다. 이와 더불어 말단노드의 입력값들에도 그래디언트를 역전파해 학습시킨다면 벡터공간에 임베딩된 단어벡터를 얻어낼 수 있을 겁니다.

다만 여기서 주의할 것은 forward pass 수행 과정에서 경우의 수를 모두 고려해 스코어가 높은 선택지만을 뽑아 트리 구조를 만든다는 사실입니다. 아래 예시를 보면 처음 부모노드를 만들 때 그럭저럭 말이 되는 'The cat', 'the mat'만 결합시킵니다. 이후엔 'on the mat'을 만듭니다. 이런 식으로 반복 수행해서 전체 문장 'The cat sat on the mat'의 트리 구조를 구축하는데요. 학습 초기엔 이런 결합이 중구난방 이루어지다가 어느 정도 학습이 진행되면 정답과 유사하게 트리 구조가 만들어지게 됩니다.

<a href="http://imgur.com/6C4vXGq"><img src="http://i.imgur.com/6C4vXGq.png" width="800px" title="source: imgur.com" /></a>

그런데 학습 과정에서의 트리 탐색은 **탐욕적(greedy)**인 방식입니다. CS224d 강의에 따르면 트리 구조 탐색시 [Beam Search Algorithm](https://en.wikipedia.org/wiki/Beam_search) 등을 이용한다고 합니다. Beam Search 알고리즘은 **최고우선탐색(Best-First Search)** 기법을 기본으로 하되 기억해야 하는 노드 수를 제한해 효율성을 높인 방식입니다. Beam Search 알고리즘에 대해 좀 더 자세히 살펴보시려면 [이곳](https://ratsgo.github.io/deep%20learning/2017/06/26/beamsearch/)을 참고하시면 좋을 것 같습니다.



## Simple RNN의 forward pass

지금까지 이야기한 simple RNN 구조를 다시 그림으로 그리면 아래와 같습니다. 방향이 바뀌어서 헷갈리실 수도 있는데요, 계산그래프를 좀 더 예쁘게 그리려고 회전한 것이지 본질적으론 같은 그림이니 너무 놀라지 마셔요. 어쨌든 부모노드마다 스코어값이 모두 나온다는 점에 유의해서 보시면 좋을 것 같은데요. $p_1$에서 나오는 스코어는 $s_1$이고요, 마찬가지로 $p_2$에선 $s_2$가 나옵니다.

<a href="http://imgur.com/Dh2lAP4"><img src="http://i.imgur.com/Dh2lAP4.png" width="600px" title="source: imgur.com" /></a>

위 그림을 토대로 forward compute pass를 그리면 아래 그림과 같습니다. 우선 첫번째 부모노드 $p_1$이 만들어지는 과정을 보시죠. 이전 챕터에서 소개드린 수식을 계산그래프로 바꿔놓은 것일 뿐입니다.

<a href="http://imgur.com/dBgYVFI"><img src="http://i.imgur.com/dBgYVFI.png" width="600px" title="source: imgur.com" /></a>

이어서 $p_2$를 만드는 과정을 소개해드립니다. $p_2$는 $c_3$에 위 그림에서 만들어진 $p_1$을 결합해 만듭니다.

<a href="http://imgur.com/Ja8GcTb"><img src="http://i.imgur.com/Ja8GcTb.png" width="600px" title="source: imgur.com" /></a>



## Simple RNN의 backward pass

역전파 관련 내용이 생소하시거나 헷갈리시는 분은 미국 스탠포드대학의 [CS231n](http://cs231n.github.io/optimization-2/) 강의를 참고하시면 좋을 것 같습니다. 아시다시피 역전파는 계산과정의 맨 마지막 부분에서 시작되어야 합니다.

<a href="http://imgur.com/RYmfwBJ"><img src="http://i.imgur.com/RYmfwBJ.png" width="600px" title="source: imgur.com" /></a>

우선 forward pass 과정에서 산출된 $s_2$와 정답을 비교해서 계산된 손실(Loss)값은 이미 구해졌다고 칩시다. 그렇다면 $s_2$의 그래디언트, 즉 $dL/ds_2$가 최초로 전파된 그래디언트값이 될 겁니다. 이를 편의상 $ds_2$라고 적었습니다. 계산그래프에서 덧셈연산은 흘러들어온 그래디언트가 그대로 전파되므로 $dL/db_s$는 흘러들어온 그대로 $ds_2$가 될 겁니다. 

곱셈 연산은 [흘러들어온 그래디언트 * 로컬 그래디언트(상대방의 변화량)]이므로 $dW_s$는 $p_2 * ds_2$가 됩니다. 마찬가지로 $dp_2$는 $W_s * ds_2$가 됩니다. **하이퍼볼릭탄젠트** $tanh(x)$의 로컬 그래디언트는 $1-tanh^2(x)$이므로 $dp2raw$는 여기에 흘러들어온 그래디언트 $dp_2$를 곱해준 값이 됩니다. 

$dp2raw$는 덧셈 그래프를 타고 그대로 분배가 되기 때문에 $db$는 그대로 $dp2raw$가 됩니다. $dW$와 $dp2concat$의 로컬 그래디언트는 각각 $p2concat$, $W$이므로 여기에 흘러들어온 그래디언트 $dp2raw$를 곱해주면 $dW$와 $dp2concat$을 구할 수 있습니다. 

마지막 $dc_3$와 $dp_1$에 주의할 필요가 있는데요. $c_3$($d$차원 벡터)과 $p_1$($d$차원 벡터)은 사실 별도의 연산을 하지 않고 그냥 합치기만 한 후 ($2d$차원 x $d$차원) 크기의 가중치 행렬 $W$을 곱해 $p_2$를 만들어 나가게 되는데요. 역전파를 할 때는 이 가중치 행렬의 절반이 $c_3$의 그래디언트에, 나머지 절반이 $p_1$의 그래디언트에 영향을 미치게 됩니다. 

따라서 $c_3$의 그래디언트는 $dp2concat$의 첫번째 절반, $p_1$의 그래디언트는 $dp2concat$의 나머지 절반이 됩니다. 혹시 헷갈리신다면 RNN의 기본구조 챕터에서 $W$와 pleft, pright의 결합 부분을 별도로 설명한 식을 보시면 좋을 것 같습니다.

한편 $p_1$의 그래디언트, 즉 $dp_1$은 별도로 **별표** 표시를 해두었는데요. Recursive Neural Networks는 이름 그대로 부모노드의 값을 재귀적으로 구해 나가는 구조이기 때문에 역전파 과정에서 그래디언트도 재귀적으로 반영되게 됩니다. 다음 그림에서 $dp_1$이 어떻게 반영되는지를 살펴볼까요?

<a href="http://imgur.com/TswcLDq"><img src="http://i.imgur.com/TswcLDq.png" width="600px" title="source: imgur.com" /></a>

자, 이제 첫번째 부모노드 $p_1$을 구하는 그래프로 왔습니다. 우선 $p_1$을 통해서도 스코어 $s_1$이 계산되기 때문에 여기에서 전파되어 들어오는 그래디언트가 있습니다. 이를 ■로 표시했습니다. 그리고 앞선 그림에서 설명드렸듯이 ★ 또한 역전파 과정에서 흘러들어오게 됩니다. 따라서 위 그림에서 $dp_1$은 ■와 ★를 더해 만들어지게 되는 것이죠. 

이후 역전파 과정은 이전에 설명했던 과정과 동일합니다. 지금은 이해를 돕기 위해 가장 단순한 구조의 RNN을 예로 들어서 설명을 드렸지만 이 구조가 깊어지면 각 층위마다 그래디언트가 재귀적으로 더해지면서 복잡한 양상을 띄게 됩니다.



## Syntatically-Untied RNN

**Syntatically-Unitied RNN(SU-RNN)**은 동사구, 명사구 등 기능이 다른 표현에 각기 다른 가중치를 적용하는 RNN 구조입니다. 반면 Simple RNN은 품사 정보에 상관없이 모든 구(phrase)에 같은 가중치를 씁니다. 둘의 비교는 아래 그림과 같습니다.

<a href="http://imgur.com/3fZ2vDx"><img src="http://i.imgur.com/3fZ2vDx.png" width="500px" title="source: imgur.com" /></a>

아래는 학습이 잘 된 SU-RNN의 가중치를 시각화한 그림입니다. 붉은색일수록 그 가중치가 높은데요. DT(관사)-NP(명사구)를 맡은 가중치 $W$를 보시면 DT를 커버하는 $w_1$의 대각성분보다 NP를 담당하는 $w_2$의 대각성분의 값이 큰 걸 확인할 수 있습니다. 이는 SU-RNN이 과업을 수행할 때 관사보다는 명사구를 중요하게 취급했다는 반증인데요. 실제로 'a cat', 'the cat' 같은 표현에서 a, the보다는 cat이라는 명사가 중요한 의미를 가지니 직관적으로 납득할 만한 결과인 것 같습니다. 반면 VP(동사구)-NP(명사구)의 경우 둘 모두 중요하게 취급하고 있는 점을 볼 수 있습니다.

<a href="http://imgur.com/QFG8Piw"><img src="http://i.imgur.com/QFG8Piw.png" width="400px" title="source: imgur.com" /></a>

## 마치며

이상으로 RNN과 Recurrent/Convolutional Neural Networks를 비교하고 Simple RNN의 구조와 foward/backward compute pass에 대해 살펴보았습니다. RNN 역시 다른 구조의 딥러닝 아키텍처와 마찬가지로 자연언어처리에 강점을 가진 구조로 널리 알려져 있는데요. 발전된 RNN 모델에 대해 살펴보시려면 [이곳](https://ratsgo.github.io/deep%20learning/2017/06/24/RNTN/)을 참고하시면 좋을 것 같습니다. 여기까지 읽어주셔서 진심으로 감사드립니다.