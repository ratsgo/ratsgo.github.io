---
title: Convex Functions
category: Convex optimization
tag: [Convex Functions]
---

이번 글에서는 **Convex Function(볼록함수)**와 관련된 개념들을 살펴보도록 하겠습니다. 이 글은 미국 카네기멜런대학 [강의](http://www.stat.cmu.edu/~ryantibs/convexopt/)를 기본으로 하되 저희 연구실의 김해동 석사과정이 만든 자료를 정리했음을 먼저 밝힙니다. 영문 위키피디아 또한 참고하였습니다. 그럼 시작하겠습니다.





## convex function

*convex function*이란 임의의 두 점 $x$, $y$와 $[0,1]$ 사이의 값 $t$에 대해 다음이 항상 성립하는 함수 $f$를 가리킵니다.


$$
f\left( tx+\left( 1-t \right) y \right) \le tf\left( x \right)+\left( 1-t \right) f\left( y \right)
$$


이를 그림으로 도시하면 다음과 같습니다.



<a href="https://imgur.com/RQLtUko"><img src="https://i.imgur.com/RQLtUko.png" title="source: imgur.com" /></a>







## convex function 유형

**strict convex**란 임의의 두 점 $x$, $y$와 $[0,1]$ 사이의 값 $t$에 대해 다음이 항상 성립하는 함수 $f$를 가리킵니다. 다시 말해 $f$는 *convex function*이면서, 선형함수(linear function)보다 큰 곡률을 가집니다. (등호는 $f$가 선형함수일 때 성립하므로)


$$
f\left( tx+\left( 1-t \right) y \right) < tf\left( x \right)+\left( 1-t \right) f\left( y \right)
$$


**strong convex**란 *convex function* 가운데 0이 아닌 양수 $m$에 대해 다음이 항상 성립하는 함수 $f$를 가리킵니다. 다시 말해 $f$는 적어도 *quadratic function*만큼 *convex*하다는 걸 뜻합니다.


$$
f-\frac { m }{ 2 } { \left\| x \right\|  }_{ 2 }^{ 2 }\quad is\quad convex
$$


따라서 다음과 같은 포함관계가 성립합니다.



- *strong convex* ⊂ *strict convex* ⊂ *convex*


**concave function(오목함수)**란 *convex function*에 음수를 취한 함수를 가리킵니다. 따라서 우리는 *convex function*에 집중해서 분석합니다.





## convex function의 예시

*convex function*의 대표적 예시는 다음과 같습니다.



<a href="https://imgur.com/A55z9iF"><img src="https://i.imgur.com/A55z9iF.png" width="500px" title="source: imgur.com" /></a>

<a href="https://imgur.com/8ssp0YF"><img src="https://i.imgur.com/8ssp0YF.png" width="500px" title="source: imgur.com" /></a>

<a href="https://imgur.com/3K0g3O3"><img src="https://i.imgur.com/3K0g3O3.png" width="500px" title="source: imgur.com" /></a>





## convexity를 보존하는 연산

*convex function*에 대해 다음 연산은 *convexity*를 보존합니다.



<a href="https://imgur.com/grqWYO0"><img src="https://i.imgur.com/grqWYO0.png" width="500px" title="source: imgur.com" /></a>

<a href="https://imgur.com/RL6OArO"><img src="https://i.imgur.com/RL6OArO.png" width="500px" title="source: imgur.com" /></a>

<a href="https://imgur.com/Mlg0oh8"><img src="https://i.imgur.com/Mlg0oh8.png" width="500px" title="source: imgur.com" /></a>





## convex function의 특성

*convex function*은 다음 세 가지 중요한 특성이 있습니다. 다음과 같습니다.



<a href="https://imgur.com/PNi83lL"><img src="https://i.imgur.com/PNi83lL.png" width="500px" title="source: imgur.com" /></a>



이 가운데 *second-order characterization*을 활용해 소프트맥스 함수가 *convex function*임을 증명해 보겠습니다. 다음과 같습니다.



<a href="https://imgur.com/qSTSjn5"><img src="https://i.imgur.com/qSTSjn5.png" width="500px" title="source: imgur.com" /></a>

