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

Recursive Neural Networks(RNN)은 입력값으로 주어지는 몇 개 단어를 묶어서 분석한다는 점에 있어서는 CNN과 유사합니다. 하지만 CNN이 모든 지역정보를 생략없이 반영하는 데 비해 RNN은 일부 정보는 스킵한다는 점에 큰 차이를 보입니다. 예컨대 위 예시에서 'the country'는 'of my birth'의 수식을 받는 구조입니다. 또 'the country', 'my birth'는 'country of'나 'of my'보다는 응집성이 높은 표현입니다. CNN의 방식처럼 'the country', 'country of', 'of my'... 이렇게 모두 분석할 필요가 없다는 것이지요. RNN은 이러한 언어의 **hiarchy**한 성질을 네트워크 구조에 적극 차용한 모델이라고 볼 수 있습니다. 실제로 언어학에서는 문장을 아래와 같이 계층적으로 나누어 분석하고 있습니다.

<a href="http://imgur.com/Himmgu4"><img src="http://i.imgur.com/Himmgu4.png" width="500px" title="source: imgur.com" /></a>

다만 RNN은 Recurrent Neural Networks나 CNN과 달리 트리 구조의 입력값을 반드시 필요로 합니다. 예컨대 아래와 같은데요. 이런 구조의 데이터를 생성하려면 대단히 많은 시간과 비용을 들여야 하기 때문에 RNN이 CNN이나 Recurrent Neural Networks에 비해 주목을 덜 받는 경향이 있는 것 같습니다.

> (4 (2 (2 The) (2 actors)) (3 (4 (2 are) (3 fantastic)) (2 .)))



## RNN의 기본 구조

단어의 연쇄(=문장)를 입력으로 받아 감성점수를 내는 RNN을 만든다고 칩시다. 그러면 가장 간단한 형태의 구조는 아래 그림처럼 나타낼 수 있습니다.

<a href="http://imgur.com/2InLlzA"><img src="http://i.imgur.com/2InLlzA.png" width="600px" title="source: imgur.com" /></a>

위 그림을 천천히 살펴보면 **자식노드(child node)** 단어 c1과 c2에 대응하는 벡터 두 개가 **부모노드(parent node)** p1으로 합쳐지고, 단어 c3는 p1과 합쳐지는 모습을 확인할 수 있습니다. RNN은 단어 c3와 p1을 합쳐 p2를 만들 때 그에 해당하는 감성점수(1.3)도 함께 만듭니다. 만약 큰 문장 안에 a, b, c라는 단어가 포함되어 있을 경우 p2는 또 다른 부모노드와 합쳐지기 위해 또 다시 분석대상이 됩니다. 이를 도식화한 것이 우측 상단의 그림인데요, 실선 방향은 계산그래프의 **forward pass**, 점선 방향은 **backward pass**로 이해하시면 좋을 것 같습니다. 

i번째 부모노드인 pi의 값은 아래처럼 정의됩니다. 각 파라메터의 차원수 또한 아래처럼 정의됩니다. 아래 식에서 pleft와 pright는 각각 i번째 부모노드의 좌측, 우측 자식노드입니다. 위 그림 기준으로 하면 p2의 pleft는 c3, pright는 p1이 되는 셈이죠. pi를 계산할 때 pleft와 pright를 단순히 합친(더하는 것이 아님에 주의) 다음 여기에 가중치 W와 bias b의 선형결합을 합니다. d는 은닉층의 차원수로서 사용자가 지정해주는 하이퍼파라메터입니다.

$${ p }_{ i }=\tanh { (W\cdot \begin{bmatrix} { p }_{ left } \\ { p }_{ right } \end{bmatrix}+b) } \\ { p }_{ i }\in { R }^{ d },\quad b\in { R }^{ d },\quad W\in { R }^{ d\times 2d }\quad  $$

사실 헷갈리실까봐 별도로 그려놓지는 않았는데요. CS224d에 소개된 아키텍처는 모든 부모노드에 스코어값들이 계산되는 구조입니다. 바꿔 말하면 p2뿐 아니라 p1에도 스코어가 출력됩니다. (물론 맨 마지막에만 스코어값들을 계산하게 만들 수도 있겠죠, 충분히 변형 가능합니다) i번째 부모노드의 스코어를 구하는 식은 다음과 같습니다.

$${ s }_{ i }={ W }_{ s }{ p }_{ i }+{ b }_{ s }$$

RNN은 이렇게 부모노드로부터 계산된 스코어와 문장의 부분에 해당하는 감성(정답레이블)과 비교한 후 오차를 최소화하는 방향으로 **역전파(backpropagation)**를 수행해 파라메터(W, b, Ws, bs)를 업데이트하는 방식으로 학습을 합니다. 



## RNN의 forward pass

지금까지 이야기한 내용을 다시 그림으로 그리면 아래와 같습니다. 방향이 바뀌어서 헷갈리실 수도 있는데요, 계산그래프를 좀 더 예쁘게 그리려고 회전한 것이지 본질적으론 같은 그림이니 너무 놀라지 마셔요. 어쨌든 부모노드마다 스코어값이 모두 나온다는 점에 유의해서 보시면 좋을 것 같은데요, p1에서 나오는 스코어는 s1, 마찬가지로 p2는 s2입니다.

<a href="http://imgur.com/Dh2lAP4"><img src="http://i.imgur.com/Dh2lAP4.png" width="600px" title="source: imgur.com" /></a>

위 그림을 토대로 forward compute pass를 그리면 아래 그림과 같습니다. 우선 첫번째 부모노드 p1이 만들어지는 과정을 보시죠. 이전 챕터에서 소개드린 수식을 계산그래프로 바꿔놓은 것일 뿐입니다.

<a href="http://imgur.com/dBgYVFI"><img src="http://i.imgur.com/dBgYVFI.png" width="600px" title="source: imgur.com" /></a>

이어서 p2를 만드는 과정을 소개해드립니다. p2는 위 그림에서 만들어진 p1과 아무런 처리를 하지 않은 c3을 결합해 만듭니다.

<a href="http://imgur.com/Ja8GcTb"><img src="http://i.imgur.com/Ja8GcTb.png" width="600px" title="source: imgur.com" /></a>



## RNN의 backward pass

역전파 관련 내용이 생소하시거나 헷갈리시는 분은 미국 스탠포드대학의 [CS231n](http://cs231n.github.io/optimization-2/) 강의를 참고하시면 좋을 것 같습니다. 아시다시피 역전파는 계산과정의 맨 마지막 부분에서 시작되어야 합니다.

<a href="http://imgur.com/RYmfwBJ"><img src="http://i.imgur.com/RYmfwBJ.png" width="600px" title="source: imgur.com" /></a>

우선 forward pass 과정에서 산출된 s2와 정답을 비교해서 계산된 손실(Loss)값은 이미 구해졌다고 칩시다. 그렇다면 s2의 그래디언트, 즉 dL/ds2가 최초로 전파된 그래디언트값이 될 겁니다. 이를 편의상 ds2라고 적었습니다. 계산그래프에서 덧셈연산은 흘러들어온 그래디언트가 그대로 전파되므로 dL/dbs는 흘러들어온 그대로 ds2가 될 겁니다. 곱셈 연산은 [흘러들어온 그래디언트 * 로컬 그래디언트(상대방의 변화량)]이므로 dWs는 p2 * ds2가 됩니다. 마찬가지로 dp2는 Ws * ds2가 됩니다. **하이퍼볼릭탄젠트** tanh(x)의 로컬 그래디언트는 **1-tanh^2(x)**이므로 dp2raw는 여기에 흘러들어온 그래디언트 dp2를 곱해준 값이 됩니다. dp2raw는 덧셈 그래프를 타고 그대로 분배가 되기 때문에 db는 그대로 dp2raw가 됩니다. dW와 dp2concat의 로컬 그래디언트는 각각 p2concat, W이므로 여기에 흘러들어온 그래디언트 dp2raw를 곱해주면 dW와 dp2concat을 구할 수 있습니다. 

마지막 dc3와 dp1에 주의할 필요가 있는데요. c3(d차원 벡터)과 p1(d차원 벡터)은 사실 별도의 연산을 하지 않고 그냥 합치기만 한 후 (2d차원 x d차원) 크기의 가중치 행렬 W을 곱해 p2를 만들어 나가게 되는데요. 역전파를 할 때는 이 가중치 행렬의 절반이 c3의 그래디언트에, 나머지 절반이 p1의 그래디언트에 영향을 미치게 됩니다. 따라서 c3의 그래디언트는 dp2concat의 첫번째 절반, p1의 그래디언트는 dp2concat의 나머지 절반이 됩니다. 

그런데 제가 p1의 그래디언트, 즉 dp1은 별도로 **별표** 표시를 해두었는데요. Recursive Neural Networks는 이름 그대로 부모노드의 값을 재귀적으로 구해 나가는 구조이기 때문에 역전파 과정에서 그래디언트도 재귀적으로 반영되게 됩니다. 다음 그림에서 dp1이 어떻게 반영되는지를 살펴볼까요?

<a href="http://imgur.com/TswcLDq"><img src="http://i.imgur.com/TswcLDq.png" width="600px" title="source: imgur.com" /></a>

자, 이제 첫번째 부모노드 p1을 구하는 그래프로 왔습니다. 우선 p1을 통해서도 스코어 s1이 계산되기 때문에 여기에서 전파되어 들어오는 그래디언트가 있습니다. 이를 ■로 표시했습니다. 그리고 앞선 그림에서 설명드렸듯이 ★ 또한 역전파 과정에서 흘러들어오게 됩니다. 따라서 위 그림에서 dp1은 ■와 ★를 더해 만들어지게 되는 것이죠. 이후 역전파 과정은 이전에 설명했던 과정과 동일합니다. 지금은 이해를 돕기 위해 가장 단순한 구조의 RNN을 예로 들어서 설명을 드렸지만 이 구조가 깊어지면 각 층위마다 그래디언트가 재귀적으로 더해지면서 복잡한 양상을 띄게 됩니다.



## 마치며

이상으로 RNN과 Recurrent/Convolutional Neural Networks를 비교하고 RNN의 기본 구조와 foward/backward compute pass에 대해 살펴보았습니다. RNN 역시 다른 구조의 딥러닝 아키텍처와 마찬가지로 자연언어처리에 강점을 가진 구조로 널리 알려져 있는데요, 다음 기회엔 RNN의 발전된 모델들과 실험결과를 함께 이야기해 보려고 합니다. 이번 포스팅은 제가 공부할 목적으로 작성한 것이므로 오류가 얼마든지 있을 수 있습니다. 지적하실 내용이나 의견, 질문 있으시면 언제든지 댓글이나 이메일로 알려주시기 바랍니다. 여기까지 읽어주셔서 진심으로 감사드립니다.