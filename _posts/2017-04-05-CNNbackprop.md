---
title: Convolutional Neural Networks의 역전파(backpropagation)
category: Machine Learning
tag: Convolutional Neural Networks
html header: <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_SVG"></script>
---

이번 포스팅에서는 **Convolutional Neural Networks(CNN)**의 **역전파(backpropagation)**를 살펴보도록 하겠습니다. 많이 쓰는 아키텍처이지만 그 내부 작동에 대해서는 제대로 알지 못한다는 생각에 저 스스로도 정리해볼 생각으로 이번 글을 쓰게 됐습니다. 수학에 약한지라 최대한 수식은 배제하고 직관적으로 설명해볼까 합니다. 이번 글은 미국 스탠포드대학의 [CS231n 강의](http://cs231n.github.io/optimization-2/)와 [이곳](http://www.jefkine.com/general/2016/09/05/backpropagation-in-convolutional-neural-networks/)을 많이 참고하였습니다. 그런데 이들 설명도 저한테 확 와닿지 않아서 상당 부분은 제 스타일대로 그림을 다시 그리거나 해석했음을 미리 밝혀둡니다. 그럼 시작하겠습니다.



## CNN의 forward pass

이미 많이들 보셨겠지만 CNN은 필터가 입력데이터를 슬라이딩하면서 지역적 특징(feature)을 추출합니다. 이후 이 특징을 최대값(**Max Pooling**)이나 평균값(**Average Pooling**)으로 압축해 다음 레이어로 보냅니다. 이런 과정을 반복해 분류 등 원하는 결과를 만들어내는 것이 CNN의 일반적인 구조입니다. CNN의 forward pass에 대해서는 이미 많은 글에서 소개된 바 있으므로 이번 포스팅에서는 아래 그림을 인용하는 것으로 설명을 간단히 마치겠습니다.

<a href="http://imgur.com/OXwLhaf"><img src="http://i.imgur.com/OXwLhaf.gif" width="500px" title="source: imgur.com" /></a>

이번 포스팅에서는 아래와 같이 가장 간단한 구조의 CNN을 예시로 설명해보려고 합니다. (CNN은 마지막 레이어에 **Fully Connected Layer(FC)**가 붙는 경우가 많은데, FC에 대한 역전파에 대해서는 이미 잘 정리된 글이 많고 우리의 목적은 CNN의 역전파를 세밀히 살피는 것이므로 여기서는 생략하겠습니다)

<a href="http://imgur.com/OTRhYvV"><img src="http://i.imgur.com/OTRhYvV.png" width="600px" title="source: imgur.com" /></a>

보시다시피 입력값은 3x3 행렬입니다. Xij는 각각 입력값의 i번째 행, j번째 열의 요소를 뜻합니다. 필터(커널) 크기는 2x2입니다. CNN은 필터가 입력벡터를 슬라이딩을 하면서 지역정보를 추출하게 되는데, 스트라이드는 한칸으로 설정했습니다. 바꿔 말해 x11, x12, x21, x22가 필터와 합성곱이 되어서 conv 레이어의 1행 1열이 됩니다. 다음번엔 x12, x13, x22, x23이 필터와 합성곱이 되어서 conv 레이어의 1행 2열이 됩니다. 필터의 색깔과 위 계산그래프의 화살표 색깔을 맞춰서 보시면 어떻게 연산이 되는지 직관적으로 확인 가능하실 겁니다. 이후 conv 레이어에 최대값이나 평균값을 취해서 정보를 압축(pooling)합니다. 위 그림 기준으로는 2x2 행렬이 2x1 벡터로 바뀐 점을 확인할 수 잇습니다.



## CNN의 backward pass

### Average Pooling

이번 포스팅의 핵심인 역전파 과정을 살펴보도록 하겠습니다. 바로 뒤 레이어로부터 전파된 그래디언트가 d1, d2라고 칩시다. 그러면 Average Pooling 레이어의 그래디언트 전파 과정은 아래와 같습니다.

<a href="http://imgur.com/xaFjFuC"><img src="http://i.imgur.com/xaFjFuC.png" width="500px" title="source: imgur.com" /></a>

위 그림은 CS231n의 계산그래프 형태로 나타낸 것인데요. 현재 지점의 그래디언트는 **미분의 연쇄법칙(chain rule)**에 의해 흘러들어온 그래디언트에 로컬그래디언트를 곱한 것과 같습니다. 평균은 모든 값을 더한 뒤 개체수로 나누어 구하게 되는데요. 만약에 m개 요소로 구성돼 있다고 한다면 Average Pooling을 하는 지점의 로컬 그래디언트는 1/m이 됩니다. 이를 흘러들어온 그래디언트(d1)과 곱해주면 d11을 구할 수가 있습니다. d12, d21, d22도 같은 방식으로 구할 수 있습니다.



### Max Pooling

최대값으로 풀링을 했다고 하면 역전파 과정은 아래와 같습니다. 즉, 최대값이 속해 있는 요소의 로컬 그래디언트는 1, 나머지는 0이기 때문에 여기에 흘러들어온 그래디언트를 곱해 구하게 됩니다.

<a href="http://imgur.com/m9gOiuc"><img src="http://i.imgur.com/m9gOiuc.png" width="450px" title="source: imgur.com" /></a>



### conv layer

자, 이제 이번 글의 핵심인 conv layer의 역전파를 할 차례입니다. 우선 x11을 보겠습니다.

<a href="http://imgur.com/9oCYz8e"><img src="http://i.imgur.com/9oCYz8e.png" width="600px" title="source: imgur.com" /></a>

x11은 forward compute pass 과정에서 2x2필터 가운데 빨간색(w1) 가중치하고만 합성곱이 수행이 됐습니다. 그렇다면 역전파 때도 마찬가지로 딱 한번의 역전파가 일어나게 되겠네요. 이를 Kapathy의 계산그래프 형태로 나타내면 우측 상단 그림과 같습니다. 즉 x11의 그래디언트는 흘러들어온 그래디언트 d11에 로컬그래디언트(w1)를 곱해서 구할 수 있습니다. (곱셈 연산의 로컬그래디언트는 '상대방 변화량'입니다) 마찬가지로 w1의 그래디언트는 흘러들어온 그래디언트 d11에 로컬그래디언트(x11)를 곱해 계산합니다.

이런 식으로 모든 경우의 수에 대해 계산하면 conv layer의 역전파 수행이 완료됩니다. 아직 헷갈리실 수 있으니 하나 더 예를 들어보겠습니다. x22를 한번 보겠습니다. 아래 그림은 계산해야할 경우의 수가 x11에 비해 늘었을 뿐 본질적으로 달라진 것은 없습니다. 

<a href="http://imgur.com/lxTuzam"><img src="http://i.imgur.com/lxTuzam.png" width="600px" title="source: imgur.com" /></a>

그런데 다 이렇게 하나하나 따져가면서 구하려면 골치가 꽤나 아플 겁니다. conv layer의 역전파를 할 때 약간의 트릭을 쓰면 조금 더 간단히 그래디언트를 구할 수 있게 됩니다. 바로 아래 그림처럼요.

<a href="http://imgur.com/LLBkARW"><img src="http://i.imgur.com/LLBkARW.png" width="700px" title="source: imgur.com" /></a>

흘러들어온 그래디언트 행렬(2x2 크기)을 conv layer를 만들 때 썼던 필터가 슬라이딩하면서 값을 구한다는 겁니다! 대신 필터 요소의 순서를 정반대로 바꿔서요. 예컨대 빨-파-노-초 필터를 초-노-파-빨 필터로 바꿔서 그래디언트행렬에 합성곱을 수행해주면 입력벡터에 대한 그래디언트를 구할 수 있습니다. 가령 x11의 그래디언트는 w1(필터에서 빨간색 요소) x d11이라고 설명드린 바 있는데요, 위 그림 오른쪽에 좌측 상단을 보시면 이것과 정확히 일치하는 것을 알 수가 있습니다. 마찬가지로 x22의 그래디언트도 흘러들어온 그래디언트 행렬에 초-노-파-빨 필터 사이의 합성곱 결과와 동일합니다.

그럼 필터의 그래디언트는 어떻게 구하게 될까요? 그건 아래 그림과 같습니다.

<a href="http://imgur.com/FJAIFr7"><img src="http://i.imgur.com/FJAIFr7.png" width="700px" title="source: imgur.com" /></a>



위 그림의 좌측 forward pass 그래프와 우측 그림을 비교해가면서 보시면 좋을 것 같은데요. 흘러들어온 그래디언트 행렬의 첫번째 요소인 d11은 x11, x12, x21, x22와 연결되어 있는 걸 확인할 수 있습니다. 계산그래프를 그려서 설명드렸던 것처럼 필터의 그래디언트는 흘러들어온 그래디언트(d11, d12, d21, d22)에 로컬 그래디언트를 곱해서 구하게 되는데요. 각각의 로컬 그래디언트는 합성곱 필터 가중치로 연결된 입력값들입니다. 