---
title: Topological Sort
category: Data structure&Algorithm
tag: [Topological Sort, Graph]
---

이번 글에서는 [그래프(Graph)](https://ratsgo.github.io/data%20structure&algorithm/2017/11/18/graph/)라는 자료구조를 활용한 정렬 알고리즘 가운데 하나인 **Topological sort** 기법을 살펴보도록 하겠습니다. 이 글은 고려대 김황남 교수님과 역시 같은 대학의 김선욱 교수님 강의와 위키피디아를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## concept

`Topogical Sort`란 **Directed Acyclic Graph**(방향을 가지면서 [사이클](https://ratsgo.github.io/data%20structure&algorithm/2017/11/18/graph/)이 없는 그래프)를 활용해 노드들 사이에 선후관계를 중심으로 정렬하는 알고리즘입니다. 이때 사용되는 기법이 [깊이우선탐색(DFS)](https://ratsgo.github.io/data%20structure&algorithm/2017/11/20/DFS/)입니다. 옷입기 예시를 보겠습니다. 우선 아래 그래프를 깊이우선탐색으로 모든 노드를 탐색하고, 노드들에 방문시점/방문종료시점을 기록해 둡니다.



<a href="https://imgur.com/WMmHq96"><img src="https://i.imgur.com/WMmHq96.png" width="500px" title="source: imgur.com" /></a>



이후 방문종료시점의 내림차순으로 정렬합니다.



<a href="https://imgur.com/21g4yY5"><img src="https://i.imgur.com/21g4yY5.png" title="source: imgur.com" /></a>



`Topological Sort`의 계산복잡성은 깊이우선탐색에 비례합니다. 따라서 $O($\|$V$\|$+$\|$E$\|$)$가 됩니다.





## DAG 최단거리

`Topological Sort`와 *[edge relaxation](https://ratsgo.github.io/data%20structure&algorithm/2017/11/25/shortestpath/)* 기법을 활용해 **Directed Acyclic Graph(DAG)**의 최단거리를 구할 수 있습니다. 그 과정은 다음과 같습니다.

- 주어진 DAG에 대해 `Topological Sort`를 수행한다.
- 시작노드를 0, 나머지의 거리를 무한대로 초기화한다.
- 각 노드별 모든 엣지에 대해 *edge relaxation*을 수행한다.



<a href="https://imgur.com/Vh4U9rD"><img src="https://i.imgur.com/Vh4U9rD.png" title="source: imgur.com" /></a>

