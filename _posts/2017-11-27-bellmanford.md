---
title: 벨만-포드 알고리즘
category: Data structure&Algorithm
tag: [Bellman-Ford's algorithm, Shortest path, Graph]
---

이번 글에서는 [최단 경로(Shortest Path)](https://ratsgo.github.io/data%20structure&algorithm/2017/11/25/shortestpath/)를 찾는 대표적인 기법 가운데 하나인 **벨만-포드 알고리즘(Bellman-Ford's algorithm)**을 살펴보도록 하겠습니다. 이 글은 고려대 김선욱 교수님과 역시 같은 대학의 김황남 교수님 강의와 위키피디아를 정리했음을 먼저 밝힙니다. 그럼 시작하겠습니다.





## concept

최단경로 문제의 *[optimal substructure](https://ratsgo.github.io/data%20structure&algorithm/2017/11/25/shortestpath/)*를 확장하면 최단경로를 다음과 같이 분해(decompostion)할 수 있습니다. 시작노드 $s$에서 $v$에 이르는 최단경로는 $s$에서 $u$까지의 최단경로에 $u$에서 $v$ 사이의 가중치(거리)를 더한 값이라는 겁니다.

 
$$
D\left( s,v \right) =D\left( s,u \right) +w\left( u,v \right)
$$


벨만-포드 알고리즘은 $s,u$ 사이의 최단경로를 구할 때 그래프 내 모든 엣지에 대해 *[edge relaxation](https://ratsgo.github.io/data%20structure&algorithm/2017/11/25/shortestpath/)*을 수행해 줍니다. 그러면 이를 몇 번 수행해야 할까요? 생각해 보면 $s,u$ 사이의 최단경로는 $s$와 $u$뿐일 수 있고, $u$를 제외한 그래프의 모든 노드(\|$V$\|$-1$개)가 $s,u$ 사이의 최단경로를 구성할 수도 있습니다. 따라서 벨만-포드 알고리즘은 모든 엣지에 대한 *edge-relaxation*을 \|$V$\|$-1$회 수행합니다.





## 수행예시1

하단 좌측 그림과 같은 그래프에 벨만-포드 알고리즘을 적용해 보겠습니다. 우선 시작노드 $A$를 제외한 모든 노드의 거리를 무한대로 초기화합니다. *edge relaxation* 순서는 *order*와 같습니다(예시를 위해 정해놓은 것일 뿐입니다).



<a href="https://imgur.com/JGvQFVi"><img src="https://i.imgur.com/JGvQFVi.png" title="source: imgur.com" /></a>



우선 ($B,E$)를 보겠습니다. `무한대-2=무한대`이므로 업데이트할 필요가 없습니다. ($C,E$), ($F,C$), ($D,F$), ($C,B$) 또한 마찬가지입니다. ($A,B$)의 경우 시작노드 $A$에서 $B$에 이르는 거리가 8이고, 이는 기존 거리(무한대)보다 작으므로 8을 $B$에 기록해 둡니다. 마찬가지로 $C,D$도 각각 -2, 4로 기록해 둡니다. 이로써 그래프 모든 엣지에 대한 첫번째 *edge relaxation*이 끝났습니다.



<a href="https://imgur.com/01Be9h5"><img src="https://i.imgur.com/01Be9h5.png" title="source: imgur.com" /></a>



상단 좌측 그림 차례입니다. ($B,E$)의 경우 `8-2=6`이고 이는 기존 거리(무한대)보다 작으므로 6을 $E$에 기록해 둡니다. ($C,E$)의 경우 `-2+3=1`이고 이는 기존 거리(6)보다 작으므로 1을 $E$에 기록해 둡니다. ($F,C$)의 경우 `무한대+9=무한대`이므로 업데이트할 필요가 없습니다. ($D,F$)의 경우 `4+5=9`이고 이는 기존 거리(무한대)보다 작으므로 9를 $F$에 기록해 둡니다. ($C,B$)의 경우 `-2+7=5`이고 이는 기존 거리(8)보다 작으므로 5를 $B$에 기록해 둡니다. ($C,D$)의 경우 `-2+1=-1`이고 이는 기존 거리(4)보다 작으므로 -1을 $D$에 기록해 둡니다. 

($A,B$)의 경우 `0+8=8`이고 이는 기존 거리(5)보다 크므로 업데이트할 필요가 없습니다. ($A,C$)의 경우 `0-2=-2`이고 이는 기존 거리(-2)와 같으므로 업데이트할 필요가 없습니다. ($A,D$)의 경우 `0+4=4`이고 이는 기존 거리(-1)보다 크므로 업데이트할 필요가 없습니다. 이로써 그래프 모든 엣지에 대한 두번째 *edge relaxation*이 끝났습니다.

이번엔 상단 우측 그림 차례입니다. ($B,E$)의 경우 `5-2=3`이고 이는 기존 거리(1)보다 크므로 업데이트할 필요가 없습니다. 이는 ($C,E$), ($F,C$) 또한 마찬가지입니다. ($D,F$)의 경우 `-1+5=4`이고 이는 기존 거리(9)보다 작으므로 4를 $F$에 기록해 둡니다. ($C,B$), ($C,D$), ($A,B$), ($A,C$), ($A,D$)는 모두 기존 거리보다 크므로 업데이트할 필요가 없습니다. 이로써 그래프 모든 엣지에 대한 세번째 *edge relaxation*이 끝났습니다.

벨만-포드 알고리즘은 시작노드를 제외한 전체 노드수 만큼의 *edge relaxation*을 수행해야 합니다. 위 예시의 경우 총 5회 반복 수행해야 합니다. 그런데 네번째 *edge relaxation*부터는 거리 정보가 바뀌지 않으므로 생략했습니다.





## 수행예시2

벨만-포드 알고리즘의 또다른 수행 예시입니다. 그래프 모든 엣지에 대한 *edge relaxation*을 1회 수행한 것입니다. *edge relaxtion*을 수행할 때 거리정보뿐 아니라 최단경로(음영 표시) 또한 업데이트한다는 걸 알 수 있습니다.



<a href="https://imgur.com/hcWT22F"><img src="https://i.imgur.com/hcWT22F.png" title="source: imgur.com" /></a>





## negative cycle

[다익스트라 알고리즘(Dijkstra's algorithm)]()과 달리 벨만-포드 알고리즘은 가중치가 음수인 경우에도 적용 가능합니다. 그러나 다음과 같이 음수 가중치가 사이클(cycle)을 이루고 있는 경우에는 작동하지 않습니다.



<a href="https://imgur.com/46tJqd7"><img src="https://i.imgur.com/46tJqd7.png" width="400px" title="source: imgur.com" /></a>



위 그림에서 $c,d$ 그리고 $e,f$가 사이클을 이루고 있는 걸 확인할 수 있습니다. $c,d$의 경우 사이클을 돌 수록 거리가 커져서 최단경로를 구할 때 문제가 되지 않습니다. 반면 $e,f$의 경우 사이클을 돌면 돌수록 그 거리가 작아져 벨만-포드 알고리즘으로 최단경로를 구하는 것 자체가 의미가 없어집니다.

따라서 그래프 모든 엣지에 대해 *edge relaxation*을 시작노드를 제외한 전체 노드수 만큼 반복 수행한 뒤, 마지막으로 그래프 모든 엣지에 대해 *edge relaxation*을 1번 수행해 줍니다. 이때 한번이라도 업데이트가 일어난다면 위와 같은 *negative cycle*이 존재한다는 뜻이 되어서 결과를 구할 수 없다는 의미의 *false*를 반환하고 함수를 종료하게 됩니다. 벨만-포드 알고리즘 전체의 의사코드는 다음과 같습니다.



<a href="https://imgur.com/Co6NVQ8"><img src="https://i.imgur.com/Co6NVQ8.png" width="300px" title="source: imgur.com" /></a>





## 계산복잡성

벨만-포드 알고리즘은 그래프 모든 엣지에 대해 *edge relaxation*을 시작노드를 제외한 전체 노드수 만큼 반복 수행하고, 마지막으로 그래프 모든 엣지에 대해 *edge relaxation*을 1번 수행해 주므로, 그 계산복잡성은 $O($\|$V$\|\|$E$\|$)$이 됩니다. 그런데 *dense graph*는 엣지 수가 대개 노드 수의 제곱에 근사하므로 간단하게 표현하면 $O($\|$V$\|$^3)$이 됩니다. 이는 다익스트라 알고리즘($O($\|$V$\|$^2)$보다 더 큰데, 벨만-포드 알고리즘은 음수인 가중치까지 분석할 수 있기 때문에 일종의 *trade-off*라고 생각해도 될 것 같다는 생각이 듭니다.ㄴ