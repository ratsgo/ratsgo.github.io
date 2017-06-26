---
title: RNN과 Beam search
category: Deep Learning
tag: Recursive Neural Networks
---

이번 글에서는 Recursive Neural Network(RNN)의 학습 과정에서 트리 탐색 기법으로 쓰이는 **Beam seach**에 대해 살펴보도록 하겠습니다. beam search는 RNN 말고도 자연언어처리 분야에서 자주 쓰인다고 하니 이 참에 정리해 두면 유용할 듯합니다. 이번 글은 [Socher et al.(2011)](https://www.google.co.kr/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwi3zKy40drUAhUHW5QKHXkmDxAQFggoMAA&url=http%3A%2F%2Fai.stanford.edu%2F~ang%2Fpapers%2Ficml11-ParsingWithRecursiveNeuralNetworks.pdf&usg=AFQjCNGdAdKAKcsqIBm3eZ2GJzJ_16_lbQ)과 미국 스탠포드 대학 NLP 강의 자료를 참고해 만들었음을 먼저 밝힙니다. Beam Search 예시 부분은 제가 직접 만든 것이니 혹시 오류가 있다면 언제든 알려주시면 감사하겠습니다. 그럼 시작하겠습니다.



## RNN과 Tree

RNN은 응집성이 높은 입력값을 트리 형태로 결합해 가면서 입력값의 구조를 추상화하는 기법입니다. Simple RNN에 대해서는 [이곳](https://ratsgo.github.io/deep%20learning/2017/04/03/recursive/)을, 발전된 형태의 RNN 모델에 대해 살펴보시려면 [이곳](https://ratsgo.github.io/deep%20learning/2017/06/24/RNTN/)을 참고하면 좋을 것 같습니다. 

어쨌든 RNN과 트리는 뗄려야 뗄 수 없는 관계를 가집니다. 이미지와 텍스트에 대해 RNN을 적용해보고자 했던 Socher et al.(2011)에도 입력값이 주어졌을 때 트리를 구축하는 방안에 대해 논문의 상당 부분을 할애하고 있습니다. 다음 그림을 볼까요?



<a href="http://imgur.com/GdnUzyQ"><img src="http://i.imgur.com/GdnUzyQ.png" width="300px" title="source: imgur.com" /></a>



Socher et al.(2011)은 우선 입력값의 이웃끼리 결합해 트리를 만들기로 합니다. 이미지를 예로 들면 1번 영역의 이웃은 2번과 3번입니다. 이를 **인접행렬(Adjacency Matrix)**로 나타내면 (1,2), (2,1), (1,3), (3,1) 위치의 요소값이 1이 되어야 할 겁니다. 이렇게 이웃이 될 수 있는 가능한 모든 경우의 수를 고려해 행렬로 나타낸 것이 좌측 두번째 그림이 됩니다.

본 블로그의 관심 주제인 텍스트는 이미지보다는 간단한 편입니다. 어떤 단어의 이웃은 왼쪽 하나, 오른쪽 하나 두개뿐입니다. 예컨대 house의 이웃은 The, has이고 a의 이웃은 has, window입니다. 이를 인접행렬로 그리면 대각성분 위, 아래만 1이고 나머지는 0인 규칙적인 모양이 됩니다. 이웃이 될 수 있는 모든 경우의 수에서 그 가짓수를 하나씩 제거해 **정답 트리 구조(Correct Tree Structure)**로 나아가자는 것이 트리 탐색의 핵심이 됩니다.





## Greedy Search

트리 탐색의 범위를 이웃으로 한정하긴 했지만 Socher et al.(2011) 방식의 본질은 탐욕적인 탐색이라고 말할 수 있겠습니다. 논문의 예를 확장시켜 그림으로 나타내 보았습니다. 아래 그림에서 $a_i$는 i번째 단어(노드)를 의미합니다. 첫번째 단계에서의 인접행렬은 이웃이 될 수 있는 모든 경우의 수가 포함되어 있습니다. $C$는 이웃들의 쌍으로 이루어진 집합입니다.



<a href="http://imgur.com/CnaEfiQ"><img src="http://i.imgur.com/CnaEfiQ.png" width="350px" title="source: imgur.com" /></a>



RNN 모델이 내놓은 score가 $[a_4,a_5]$가 가장 높았다고 가정해보겠습니다. 다시 말해 모델이 a와 window라는 단어가 응집성이 가장 높다고 판단한 것이지요. 이 둘을 이어서 트리를 만드는 것이 첫번째 과정입니다. 다음 그림처럼요. 아래 그림을 보시면 $[a_4,a_5]$가 결합해 parent node $p_{(4,5)}$가 되었습니다. 여기에 맞춰서 인접행렬과 $C$가 업데이트된 것도 확인가능합니다.



<a href="http://imgur.com/gnPIp8h"><img src="http://i.imgur.com/gnPIp8h.png" width="350px" title="source: imgur.com" /></a>



이번엔 RNN 모델이 출력한 score가 The, house가 가장 높았다고 가정해보겠습니다. 그러면 인접행렬과 $C$는 다음과 같이 업데이트됩니다.



<a href="http://imgur.com/KrbcuPH"><img src="http://i.imgur.com/KrbcuPH.png" width="350px" title="source: imgur.com" /></a>



이번엔 RNN 모델이 has라는 단어와 'a, window'라는 구의 응집성이 가장 높다고 판단했다고 칩시다. 다음 그림과 같이 업데이트됩니다.



<a href="http://imgur.com/hxcl5f5"><img src="http://i.imgur.com/hxcl5f5.png" width="350px" title="source: imgur.com" /></a>



이제는 연결해야 하는 노드가 딱 두 개뿐이므로 이 둘만 연결해주면 아래 그림처럼 트리 탐색 과정이 종료됩니다.



<a href="http://imgur.com/btt5Lb1"><img src="http://i.imgur.com/btt5Lb1.png" width="350px" title="source: imgur.com" /></a>



## Beam Search

보시다시피 Socher et al.(2011)의 방식은 탐욕적입니다. 이게 찔려선지 Socher et al.(2011)은 텍스트에 대해서는 Beam Search를 적용할 수 있다고 언급했습니다. 논문의 일부를 인용해봤습니다.

> Since in a sentence each word only has 2 neighbors, less-greedy search algorithms such as a **bottom-up beam search** can be used.

Beam Search란 **최고우선탐색(Best-First Search)** 기법을 기본으로 하되 기억해야 하는 노드 수를 제한해 효율성을 높인 방식입니다. Socher et al.(2011)이 언급했듯 여전히 탐욕적이지만 기존 방식보다는 조금 나은 기법입니다. 다음 예제 그림을 볼까요?



<a href="http://imgur.com/zXpcLHB"><img src="http://i.imgur.com/zXpcLHB.png" width="350px" title="source: imgur.com" /></a>



사용자가 기억해야 하는 노드 수(Beam)를 3으로 정했다고 가정해 봅시다. 그러면 $i$번째 step에서 다음 step에 선택될 수 있는 가능한 모든 경우의 수를 계산해본 뒤 Beam Search의 기본이 되는 알고리즘(예컨대 RNN)이 내놓는 최상위 3개 결과만 취해서 $i+1$번째 step의 결과물로 반환하는 방식입니다. 위 그림의 예시는 상위 노드에서 하위 노드로 분기해 나가는 Top-Down Beam Search입니다.





## Bottom-Up Beam Search

파싱과 같은 자연언어처리 분야에서는 Top-Down보다는 Bottom-Up Beam Search 기법이 자주 쓰인다고 합니다. 이 기법은 하위 노드에서 상위 노드로 결합해 나가는 방식입니다. 임의의 7개 단어가 있고 이로부터 파싱 트리를 구축해야 하는 상황을 가정해보겠습니다. 사용자가 지정한 Beam은 2라고 두겠습니다.

초기 상태는 다음 그림과 같습니다. 각 단어들은 왼쪽과 오른쪽 이웃 두 개씩만 있기 때문에 다음 step에 선택될 수 있는 가능한 모든 경우의 수는 빨간색 점선과 같습니다. 이 가운데 첫번째-세번째 단어, 세번째-네번째 단어를 결합하는 것이 모델의 판단결과라고 가정해 보겠습니다.



<a href="http://imgur.com/58aA9z6"><img src="http://i.imgur.com/58aA9z6.png" width="300px" title="source: imgur.com" /></a>



두번째 step에선 이들을 잇고 나서 세번째 step에 선택될 수 있는 가능한 모든 경우의 수를 계산해 본 뒤 최적 두 개 결과를 선택합니다.





<a href="http://imgur.com/eK7tzbY"><img src="http://i.imgur.com/eK7tzbY.png" width="300px" title="source: imgur.com" /></a>



세번째 step에서도 지금까지 수행한 작업을 반복합니다.



<a href="http://imgur.com/8xNu0Pu"><img src="http://i.imgur.com/8xNu0Pu.png" width="300px" title="source: imgur.com" /></a>



그런데 다섯번째 단어는 왼쪽 트리, 오른쪽 트리 둘 모두에 속할 수는 없습니다. 이 가운데 score가 좀 더 높은 쪽에 할당되게 됩니다.



<a href="http://imgur.com/fR1DRhH"><img src="http://i.imgur.com/fR1DRhH.png" width="300px" title="source: imgur.com" /></a>



이제 남은 경우의 수는 단 하나뿐이므로 모델이 내놓는 score를 반영할 필요도 없이 트리를 완성하기만 하면 됩니다.



<a href="http://imgur.com/AV6i031"><img src="http://i.imgur.com/AV6i031.png" width="300px" title="source: imgur.com" /></a>