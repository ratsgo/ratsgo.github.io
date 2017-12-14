---
title: 최단 경로 문제
category: Data structure&Algorithm
tag: [Shortest path, Graph]
---

이번 글에서는 **최단 경로 문제(Shortest Path Problem)**를 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님과 역시 같은 대학의 김황남 교수님 강의와 위키피디아를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## 최단거리 문제

최단 경로 문제란 두 노드를 잇는 가장 짧은 경로를 찾는 문제입니다. 가중치가 있는 그래프(Weighted Graph)에서는 엣지 가중치의 합이 최소가 되도록 하는 경로를 찾으려는 것이 목적입니다. 최단 경로 문제엔 다음과 같은 변종들이 존재합니다.

- **단일 출발(single-source) 최단경로** : 단일 노드 $v$에서 출발하여 그래프 내의 모든 다른 노드에 도착하는 가장 짧은 경로를 찾는 문제.
- **단일 도착(single-destination) 최단경로** : 모든 노드들로부터 출발하여 그래프 내의 한 단일 노드 $v$로 도착하는 가장 짧은 경로를 찾는 문제. 그래프 내의 노드들을 거꾸로 뒤집으면 단일 출발 최단경로문제와 동일.
- **단일 쌍(single-pair) 최단 경로** : 주어진 꼭지점 $u$와 $v$에 대해 $u$에서 $v$까지의 최단 경로를 찾는 문제.
- **전체 쌍(all-pair) 최단 경로** : 그래프 내 모든 노드 쌍들 사이의 최단 경로를 찾는 문제.

[다익스트라 알고리즘](https://ratsgo.github.io/data%20structure&algorithm/2017/11/26/dijkstra/), [벨만-포드 알고리즘](https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/)은 여기서 단일 출발 최단경로 문제를 푸는 데 적합합니다. 하지만 여기에서 조금 더 응용하면 나머지 세 문제도 풀 수 있습니다. 





## optimal substructure

여기에서 최단거리의 중요한 속성을 하나 짚고 넘어가겠습니다. 다익스트라 알고리즘이나 벨만-포드 알고리즘이 최단 경로를 찾을 때 써먹는 핵심 정리이기도 합니다.

- 최단경로의 부분 경로는 역시 최단경로이다.

이를 나타낸 예시 그림이 다음 그림입니다. 아래 그림에서 직선은 엣지, 물결선은 경로를 나타냅니다. 각 숫자는 가중치를 나타냅니다. 

엣지 가중치 합이 최소인 최단경로는 굵게 표시된 상단 첫번째 경로임을 알 수 있습니다. 만약 그렇다면 시작노드로부터 중간에 있는 노드에 이르기까지의 경로(그 가중치는 5) 또한 최단경로라는 것이 위 정리의 핵심입니다.



<a href="https://imgur.com/4s5a0iz"><img src="https://i.imgur.com/4s5a0iz.png" width="300px" title="source: imgur.com" /></a>



위 정리를 증명한 내용은 다음과 같습니다.



<a href="https://imgur.com/Ldpb0WM"><img src="https://i.imgur.com/Ldpb0WM.png" width="380px" title="source: imgur.com" /></a>



위 정리를 확장하면 최단경로를 다음과 같이 분해(decompostion)할 수 있습니다. 시작노드 $s$에서 $v$에 이르는 최단경로는 $s$에서 $u$까지의 최단경로에 $u$에서 $v$ 사이의 가중치(거리)를 더한 값이라는 겁니다. 


$$
D\left( s,v \right) =D\left( s,u \right) +w\left( u,v \right)
$$
만약 위 식 우변의 값(현재 *step*에서 구한 새로운 경로의 거리)이 좌변(기존 최단경로의 거리)보다 작다면 최단경로를 업데이트해 줍니다. 이렇게 노드별로 하나씩 구해 확장해 나가면 $s$에서 $v$ 사이의 최단경로를 구할 수 있습니다.

이와 같이 어떤 문제의 최적해가 그 부분문제들의 최적해들로 구성(*construct*)될 수 있다면 해당 문제는 *optimal substructure*를 가진다고 말합니다. 이 속성을 가지고 [다이내믹 프로그래밍(dynamic programming)](https://ratsgo.github.io/data%20structure&algorithm/2017/11/15/dynamic/)이나 [탐욕 알고리즘](https://ratsgo.github.io/data%20structure&algorithm/2017/11/22/greedy/)을 적용해 문제를 효율적으로 풀 수 있습니다. 





## edge relaxation

최단경로를 구하는 알고리즘은 *edge relaxation*(변 경감)을 기본 연산으로 합니다. 이는 지금까지 이야기한 최단경로 문제의 *optimal structure*에서 파생된 것입니다.

우선 시작노드 $s$에서 임의의 노드 $z$로의 최단경로를 구한다고 칩시다. 그리고 현재 시점에서 우리가 알고 있는 $s,z$ 사이의 최단거리 $d(z)$는 75, $s,u$ 사이의 최단거리 $d(u)$는 50이라고 두겠습니다. 

그런데 탐색 과정에서 엣지 $e$를 경유하는 경로의 거리가 총 60이라고 한다면, 기존에 우리가 알고 있는 $d(z)$보다 짧아서 기존 $d(z)$가 최단경로라고 말할 수 없게 됩니다. 이에 최단경로를 구성하고 있는 노드와 엣지 정보, 그리고 거리의 합을 업데이트해줍니다. 이것이 바로 *edge relaxation*입니다. 



<a href="https://imgur.com/nqdnANR"><img src="https://i.imgur.com/nqdnANR.png" width="350px" title="source: imgur.com" /></a>



*edge relaxation*은 최단경로 알고리즘을 수행하는 과정에서 경로를 구성하고 있는 엣지 가중치의 합을 줄여나간다(relax)는 취지로 이런 이름이 붙은 것 같습니다.





## 알고리즘 특성별 비교

최단경로 알고리즘은 크게 [다익스트라](https://ratsgo.github.io/data%20structure&algorithm/2017/11/26/dijkstra/)와 [벨만-포드](https://ratsgo.github.io/data%20structure&algorithm/2017/11/27/bellmanford/) 알고리즘 두 가지가 있습니다. 다익스트라 알고리즘은 엣지 가중치가 음수일 경우 동작하지 않습니다. 벨만-포드 알고리즘의 경우 엣지 가중치가 음수여도 동작하나, *negative cycle*이 있을 경우 동작하지 않습니다. 다익스트라 알고리즘의 계산복잡성은 $O($\|$V$\|$^2+$\|$E$\|$)$이며, 벨만-포드는 $O($\|$V$\|\|$E$\|$)$입니다.





## 전체쌍 최단경로

전체쌍(All-pair) 최단경로 문제는 `Floyd-Warshall 알고리즘`이 널리 쓰인다고 합니다. 최단경로 문제의 *optimal substructure*를 활용한 것으로 의사코드는 다음과 같습니다.



<a href="https://imgur.com/AigMqRx"><img src="https://i.imgur.com/AigMqRx.png" width="400px" title="source: imgur.com" /></a>



작동 예시는 다음과 같습니다. 



<a href="https://imgur.com/WFAJSUW"><img src="https://i.imgur.com/WFAJSUW.png" width="400px" title="source: imgur.com" /></a>



다만 노드가 다르다면 단일쌍 최단경로 문제는 서로 독립적이기 때문에, 최근엔 단일쌍 문제에 적합한 다익스트라/벨만-포드 알고리즘을 GPU를 활용해 병렬처리하는 방식으로 전체쌍 최단경로를 푸는 경우가 많다고 합니다.