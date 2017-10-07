---
title: Candidate Sampling
category: From frequency to semantics
tag: Candidate Sampling
---

이번 글에서는 소프트맥스 확률을 구할 때 계산량을 줄이는 **Candidate sampling** 기법에 대해 살펴보도록 하겠습니다. 이번 글은 각 논문과 [Quora](https://www.quora.com/What-is-Noise-Contrastive-estimation-NCE)를 정리하였습니다. 혹시 제가 잘못 알고 있거나 틀린 점 있으시면 댓글로 지적해주시면 고맙겠습니다. 그럼 시작하겠습니다.



## 목적

다범주 분류를 수행하는 딥러닝 모델의 말단에는 소프트맥스 확률과 크로스엔트로피 손실(loss)을 구하는 'Softmax-with-Loss' 계층이 있습니다. 딥러닝 모델의 파라메터 업데이트를 하기 위해서는 손실에 대한 그래디언트를 구해야 하는데요. 3개 범주를 분류하는 모델을 구축한다고 했을 때 Softmax-with-Loss 계층의 손실에 대한 그래디언트는 다음 그림의 적색 화살표와 같습니다.



<a href="https://imgur.com/gyeTKAn"><img src="https://i.imgur.com/gyeTKAn.png" width="400px" title="source: imgur.com" /></a>



위 그림에서 $y_i$는 $i$번째 범주에 대한 소프트맥스 확률입니다. $t_j$는 $j$번째 범주의 실제 정답(1 혹은 0)입니다. 다시 말해 모든 범주에 대해 소프트맥스 확률을 구해야 손실에 대한 그래디언트를 계산할 수 있다는 이야기입니다.

그런데 여기서 범주 수가 10만개가 넘는다면 어떻게 될까요? 소프트맥스 확률값을 구할 때 계산량이 어마어마하게 많아질 겁니다. 특히 자연어의 경우 단어의 수가 적게는 수십만개에서 많게는 수백만개에 이르기 때문에 자연언어처리를 위한 딥러닝 모델을 만들 때 소프트맥스 확률값을 구할 때 계산량을 줄이려는 노력이 계속돼 왔습니다. Candidate sampling이 제안된 배경입니다.





## 몇 개만 뽑아서 계산하기

가장 간단한 아이디어로는 단어 몇 개만 뽑아서 소프트맥스 확률값을 구하고, 뽑힌 해당 단어들과 해당 단어들에 관계된 파라메터에 대해서만 업데이트하는 겁니다. [On Using Very Large Target Vocabulary for Neural Machine Translation](https://arxiv.org/abs/1412.2007)에서 제안된 방법입니다. 예컨대 문맥 $c$가 주어졌을 때 단어 $w$가 나타날 조건부확률은 다음과 같이 근사화합니다. 


$$
\begin{align*}
p\left( w|c \right) =\frac { exp\left( { w }^{ T }c \right)  }{ \sum _{ w'\in V }^{  }{ exp\left( { w' }^{ T }c \right)  }  } \\ \approx \frac { exp\left( { w }^{ T }c \right)  }{ \sum _{ w'\in V' }^{  }{ exp\left( { w' }^{ T }c \right)  }  } 
\end{align*}
$$


위 식에서 $V$는 말뭉치 전체의 단어로 이뤄진 집합입니다. $V'$는 $V$에서 $k$개 단어를 뽑은 $V$의 부분집합입니다. 소프트맥스 확률을 구할 때 말뭉치 전체 단어를 고려하지 않고 $k$개 일부 단어들만 고려하기 때문에 계산량을 상당히 많이 줄일 수 있습니다. 논문에 따르면 그 성능도 많이 떨어지지 않는다고 합니다.





## Negative Sampling

[Word2Vec](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)에 쓰인 Negative Sampling은 **Noise Contrasive Estimation**의 단순화된 버전입니다. Negative Sampling은 소프트맥스 확률을 구할 때 계산량을 줄이기 위해 일부 샘플만 뽑아서 계산한다는 점에서는 위 방법과 공통점을 지닙니다. 가장 큰 차이점은 Noise Distribution 개념입니다.

Word2Vec의 Negative Sampling에서는 단어 벡터를 학습할 때 Noise(=Negative) 샘플인지 여부를 가리는 이진 분류 문제(binary classification problem)로 접근합니다. Word2Vec 모델에서 Negative 샘플은 사용자가 정한 window 내에 등장하지 않는 단어들(정답=0)입니다. 반면 Positive 샘플(window 내에 등장하는 단어들)은 정답을 1로 놓고 학습을 하는 방식입니다.

Word2Vec 학습과정에선 중심단어와 Positive 샘플의 단어벡터들끼리는 유사하게(내적값 상향), 중심 단어와 Negative 샘플의 단어벡터들끼리는 멀게(내적값 하향) 업데이트됩니다. 논문에 따르면 1회 학습시 사용하는 Negative 샘플의 수는 작은 말뭉치일 경우 5~20개, 큰 말뭉치일 경우 2~5개가 적당합니다. 다시 말해 1회 학습시 최대 20개 정도의 단어벡터를 업데이트하는 셈입니다.