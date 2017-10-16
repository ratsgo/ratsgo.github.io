---
title: 은닉마코프모델 계산 및 구현
category: Machine Learning
tag: HMMs
---

이번 글에선 **은닉마코프모델(Hidden Markov Models, HMMs)**의 계산과정과 구현을 다루어 보도록 하겠습니다. 순차적인 데이터를 다루는 데 강점을 지녀 개체명 인식, 포스태깅 등 단어의 연쇄로 나타나는 언어구조 처리에 과거 많은 주목을 받았던 기법입니다. 이 글은 고려대 강필성 교수님 강의와 역시 같은 대학의 정순영 교수님 강의, 서울대 언어학과 신효필 교수님 저서, 위키피디아, [Speech and Language Processing 3rd edition draft](https://web.stanford.edu/~jurafsky/slp3/9.pdf)를 정리했고, [jason2506](https://github.com/jason2506)님의 코드([BSD-licensed](https://opensource.org/licenses/BSD-3-Clause))를 이해하기 쉽게 정리했음을 먼저 밝힙니다. 모델 자체에 대해서는 [이곳](https://ratsgo.github.io/machine%20learning/2017/03/18/HMMs/)을 참고하시면 좋을 것 같습니다. 그럼 시작하겠습니다.



## example

날씨를 은닉마코프모델로 구축한 예시는 다음 그림과 같습니다.

<a href="https://imgur.com/lEMDGBC"><img src="https://i.imgur.com/lEMDGBC.png" width="500px" title="source: imgur.com" /></a>

위 그림에 나타난 전이확률 $A$를 행렬 형태로 나타내면 다음과 같습니다.

|  구분   | start | HOT  | COLD | end  |
| :---: | :---: | :--: | :--: | :--: |
| start |   0   | 0.8  | 0.2  |  0   |
|  HOT  |   0   | 0.6  | 0.3  | 0.1  |
| COLD  |   0   | 0.4  | 0.5  | 0.1  |
|  end  |   0   |  0   |  0   |  0   |

방출확률 $B$는 다음과 같습니다.

|  구분  | HOT  | COLD |
| :--: | :--: | :--: |
|  1   | 0.2  | 0.5  |
|  2   | 0.4  | 0.4  |
|  3   | 0.4  | 0.1  |

아이스크림 관측치 $O$가 [3, 1, 3, 3, 1]으로 나타났다고 가정해 보겠습니다. 위 표와 같은 $A$, $B$, 즉 $θ$가 주어졌을 때 $O$가 나타날 확률(우도) $P(O$\|$θ)$는 다음과 같이 32가지 경우의 수에 해당하는 모든 확률들의 합입니다.

|   상태1(3개)   |   상태2(1개)   |   상태3(3개)   |   상태4(3개)   |   상태5(1개)   | prob×10^7 |
| :---------: | :---------: | :---------: | :---------: | :---------: | :-------: |
| cold(.2×.1) | cold(.5×.5) | cold(.5×.1) | cold(.5×.1) | cold(.5×.5) |   31.25   |
| cold(.2×.1) | cold(.5×.5) | cold(.5×.1) | cold(.5×.1) | hot(.4×.2)  |    10     |
| cold(.2×.1) | cold(.5×.5) | cold(.5×.1) | hot(.4×.4)  | cold(.3×.5) |    60     |
| cold(.2×.1) | cold(.5×.5) | hot(.4×.4)  | cold(.3×.1) | cold(.5×.5) |    60     |
| cold(.2×.1) | hot(.4×.2)  | cold(.3×.1) | cold(.5×.1) | cold(.5×.5) |     6     |
| hot(.8×.4)  | cold(.3×.5) | cold(.5×.1) | cold(.5×.1) | cold(.5×.5) |    300    |
| cold(.2×.1) | cold(.5×.5) | cold(.5×.1) | hot(.4×.4)  | hot(.6×.2)  |    48     |
| cold(.2×.1) | cold(.5×.5) | hot(.4×.4)  | cold(.3×.1) | hot(.4×.2)  |   19.2    |
| cold(.2×.1) | hot(.4×.2)  | cold(.3×.1) | cold(.5×.1) | hot(.4×.2)  |   1.92    |
| hot(.8×.4)  | cold(.3×.5) | cold(.5×.1) | cold(.5×.1) | hot(.4×.2)  |    96     |
| cold(.2×.1) | cold(.5×.5) | hot(.4×.4)  | hot(.6×.4)  | cold(.3×.5) |    288    |
| cold(.2×.1) | hot(.4×.2)  | cold(.3×.1) | hot(.4×.4)  | cold(.3×.5) |   11.52   |
| hot(.8×.4)  | cold(.3×.5) | cold(.5×.1) | hot(.4×.4)  | cold(.3×.5) |    576    |
| cold(.2×.1) | hot(.4×.2)  | hot(.6×.4)  | cold(.3×.1) | cold(.5×.5) |   28.8    |
| hot(.8×.4)  | cold(.3×.5) | hot(.4×.4)  | cold(.3×.1) | cold(.5×.5) |    576    |
| cold(.2×.1) | cold(.5×.5) | hot(.4×.4)  | hot(.6×.4)  | hot(.6×.2)  |  230.400  |
| cold(.2×.1) | hot(.4×.2)  | cold(.3×.1) | hot(.4×.4)  | hot(.6×.2)  |   9.216   |
| hot(.8×.4)  | cold(.3×.5) | cold(.5×.1) | hot(.4×.4)  | hot(.6×.2)  |   460.8   |
| cold(.2×.1) | hot(.4×.2)  | hot(.6×.4)  | cold(.3×.1) | hot(.4×.2)  |   9.216   |
| hot(.8×.4)  | cold(.3×.5) | hot(.4×.4)  | cold(.3×.1) | hot(.4×.2)  |  184.32   |
| hot(.8×.4)  | hot(.6×.2)  | cold(.3×.1) | cold(.5×.1) | hot(.4×.2)  |   46.08   |
| cold(.2×.1) | hot(.4×.2)  | hot(.6×.4)  | hot(.6×.4)  | cold(.3×.5) |  138.24   |
| hot(.8×.4)  | cold(.3×.5) | hot(.4×.4)  | hot(.6×.4)  | cold(.3×.5) |  2764.8   |
| hot(.8×.4)  | hot(.6×.2)  | cold(.3×.1) | hot(.4×.4)  | cold(.3×.5) |  276.48   |
| hot(.8×.4)  | hot(.6×.2)  | hot(.6×.4)  | cold(.3×.1) | cold(.5×.5) |   691.2   |
| cold(.2×.1) | hot(.4×.2)  | hot(.6×.4)  | hot(.6×.4)  | hot(.6×.2)  |  110.592  |
| hot(.8×.4)  | cold(.3×.5) | hot(.4×.4)  | hot(.6×.4)  | hot(.6×.2)  |  2211.84  |
| hot(.8×.4)  | hot(.6×.2)  | cold(.3×.1) | hot(.4×.4)  | hot(.6×.2)  |  221.184  |
| hot(.8×.4)  | hot(.6×.2)  | hot(.6×.4)  | cold(.3×.1) | hot(.4×.2)  |  221.184  |
| hot(.8×.4)  | hot(.6×.2)  | hot(.6×.4)  | hot(.6×.4)  | cold(.3×.5) |  3317.76  |
| hot(.8×.4)  | hot(.6×.2)  | hot(.6×.4)  | hot(.6×.4)  | hot(.6×.2)  | 2654.208  |

위 32가지 경우의 수에 해당하는 결합확률의 합, 즉 우도는 0.001566021입니다. 이번엔 최적상태열을 구해보겠습니다. 

| 항목          | 도출과정                                     |
| ----------- | ---------------------------------------- |
| $v_1(hot)$  | P(hot\|start)×P(3\|hot)                  |
| $v_1(cold)$ | P(cold\|start)×P(3\|cold)                |
| $v_2(hot)$  | max{$v_1$(hot)×P(hot\|hot)×P(1\|hot),$v_1$(cold)×P(hot\|cold)×P(1\|hot)\} |
| $v_2(cold)$ | max\{$v_1$(hot)×P(cold\|hot)×P(1\|cold),$v_1$(cold)×P(cold\|cold)×P(1\|cold)\} |
| $v_3(hot)$  | max\{$v_2$(hot)×P(hot\|hot)×P(3\|hot),$v_2$(cold)×P(hot\|cold)×P(3\|hot)\} |
| $v_3(cold)$ | max\{$v_2$(hot)×P(cold\|hot)×P(3\|cold),$v_2$(cold)×P(cold\|cold)×P(3\|cold)\} |
| $v_4(hot)$  | max\{$v_3$(hot)×P(hot\|hot)×P(3\|hot),$v_3$(cold)×P(hot\|cold)×P(3\|hot)\} |
| $v_4(cold)$ | max\{$v_3$(hot)×P(cold\|hot)×P(3\|cold),$v_3$(cold)×P(cold\|cold)×P(3\|cold)\} |
| $v_5(hot)$  | max\{$v_4$(hot)×P(hot\|hot)×P(1\|hot),$v_4$(cold)×P(hot\|cold)×P(1\|hot)\} |
| $v_5(cold)$ | max\{$v_4$(hot)×P(cold\|hot)×P(1\|cold),$v_4$(cold)×P(cold\|cold)×P(1\|cold)\} |
| $v_6(end)$  | max\{$v_5$(hot)×P(end\|hot),$v_5$(cold)×P(end\|cold)\} |

위 표를 실제 계산하면 다음과 같습니다.

| 항목          | 최적상태(직전) | 비터비 확률                                   |
| ----------- | -------- | ---------------------------------------- |
| $v_1(hot)$  | -        | .8×.4=.32                                |
| $v_1(cold)$ | -        | .2×.1=.02                                |
| $v_2(hot)$  | hot      | max(**.32×.6×.2**,.02×.4.×2)=.0384       |
| $v_2(cold)$ | hot      | max(**.32×.3×.5**,.02×.5.×5)=.048        |
| $v_3(hot)$  | hot      | max(**.0384×.6×.4**,.048×.4.×4)=.009216  |
| $v_3(cold)$ | cold     | max(.0384×.3×.1,**.048×.5.×.1**)=.0024   |
| $v_4(hot)$  | cold     | max(.009126×.6×.4,**.0024×.4.×4**)=.000384 |
| $v_4(cold)$ | hot      | max(**.009126×.3×.1**,.0024×.5.×.1)=.00027378 |
| $v_5(hot)$  | hot      | max(**.000384×.6×.2**,.00027378×.4.×2)=.00004608 |
| $v_5(cold)$ | cold     | max(.000384×.3×.5,**.00027378×.5.×5**)=.000068445 |
| $v_6(end)$  | cold     | max(.00004608×.1,**.000068445×.1**)=.0000068445 |

계산된 위 표를 토대로 backtrace를 하면 다음과 같은 최적상태열을 구할 수 있습니다.

> HOT, HOT, HOT, COLD, COLD





## Define Vars

전이확률 $A$, 방출확률 $B$, 상태집합 $Q$를 정의합니다. 초기 시작확률(*start_prob*) 또한 정의했습니다.

```python
class Model(object):
	
    # 변수 초기화
    def __init__(self, states, symbols, start_prob=None, trans_prob=None, emit_prob=None):
        # 상태(states) : hot, cold
        self._states = set(states)
        # 관측치(observation) : 아이스크림 개수 1, 2, 3
        # 포스태깅 등에선 품사 태그(symbol)
        self._symbols = set(symbols)
        # 시작확률 : p(hot\|start), p(cold\|start)
        self._start_prob = _normalize_prob(start_prob, self._states)
        # 전이확률 : p(hot\|hot), p(cold\|hot), etc
        self._trans_prob = _normalize_prob_two_dim(trans_prob, self._states, self._states)
        # 방출확률 : p(3\|hot), etc
        self._emit_prob = _normalize_prob_two_dim(emit_prob, self._states, self._symbols)
```





## Forward Algorithm

Forward Algorith은 $j$번째 상태에서 $o_1,...,o_t$가 나타날 전방확률 $α$를 구하는 기법입니다. 다음과 같이 정의됩니다.


$$
{ \alpha  }_{ t }(j)=\sum _{ i=1 }^{ n }{ { \alpha  }_{ t-1 }(i)\times { a }_{ ij } } \times { b }_{ j }({ o }_{ t })
$$



Forward Algorithm을 파이썬 코드로 구현한 결과는 다음과 같습니다.

```python
    def _forward(self, sequence):
        # sequence : O
        # 아이스크림 소비 기록 시퀀스 [3, 1, 3]
        sequence_length = len(sequence)
        if sequence_length == 0:
            return []
	    
        # Dynamic Programming
        # 앞으로 중간 계산된 값들은 alpha라는 변수에 저장
        alpha = [{}]
        
        # 시작 지점의 alpha값 계산 후 alpha[0]에 저장
        # alpha[0] = {'hot' : p(hot\|start) * p(3\|hot), 
        #             'cold' : p(cold\|start) * p(3\|cold)}
        # p(3\|cold) : emit_prob('cold', 3)
        # sequence[0] : 3
        for state in self._states:
            alpha[0][state] = self.start_prob(state) * self.emit_prob(state, sequence[0])
	    
        # sequence의 두번째 값부터 마지막까지 likelihood 모두 계산
        # index : 위 수식에서 t
        for index in range(1, sequence_length):
            alpha.append({})
            for state_to in self._states:
                prob = 0
                for state_from in self._states:
                    # += : 위 수식에서 Σ
                    # alpha[index-1] : 위 수식에서 α_t-1
                    # state_from : 위 수식에서 i
                    # state_to : 위 수식에서 j
                    # trans_prob : 위 수식에서 a_ij
                    prob += alpha[index - 1][state_from] * \
                        self.trans_prob(state_from, state_to)
                # emit_prob : 위 수식에서 b
                # sequence[index] : 위 수식에서 o_t 
                alpha[index][state_to] = prob * self.emit_prob(state_to, sequence[index])

        return alpha
```





## Backward Probability

전방확률 $α$와 반대 방향으로 계산한 것이 후방확률 $β$입니다. 다음과 같이 정의됩니다.


$$
{ \beta  }_{ t }(i)=\sum _{ j=1 }^{ n }{ { a }_{ ij } } \times { b }_{ j }({ o }_{ t+1 })\times { \beta  }_{ t+1 }(j)
$$


다음은 $β$를 구하는 파이썬 코드입니다. 

```python
    def _backward(self, sequence):
        sequence_length = len(sequence)
        if sequence_length == 0:
            return []

        beta = [{}]
        for state in self._states:
            beta[0][state] = 1

        for index in range(sequence_length - 1, 0, -1):
            beta.insert(0, {})
            for state_from in self._states:
                prob = 0
                for state_to in self._states:
                    prob += beta[1][state_to] * \
                        self.trans_prob(state_from, state_to) * \
                        self.emit_prob(state_to, sequence[index])
                beta[0][state_from] = prob

        return beta
```






## Viterbi algorithm

$v_t(j)$는 $t$번째 시점의 $j$번째 은닉상태의 비터비 확률을 가리킵니다. $t$번째 시점 $j$번째 상태의 backtrace $b_{t_t}(j)$는 다음과 같이 정의됩니다.


$$
{ v }_{ t }(j)=\max _{ i } ^{n}{ \left[ { v }_{ t-1 }(i)\times { a }_{ ij }\times { b }_{ j }({ o }_{ t }) \right]  }\\{ b }_{ { t }_{ t } }(j)=arg\max _{ i=1 }^n{ \left[ { v }_{ t-1 }(i)\times { a }_{ ij }\times { b }_{ j }({ o }_{ t }) \right]  }
$$


파이썬 코드로 구현한 결과는 다음과 같습니다.

```python
    def decode(self, sequence):
        # sequence : O
        # sequence_length : T
        sequence_length = len(sequence)
        if sequence_length == 0:
            return []
	   
        # delta : 비터비 확률 v
        # Dynamic Programming : 중간 계산값 저장해 활용
        delta = {}
        
        # 시작 지점의 delta값 계산
        for state in self._states:
            # start_prob(state) : p(cold\|start) or p(hot\|start)
            # sequence[0] : 관측 시퀀스의 첫번째 요소, o_1, '3'
            # emit_prob(state, sequence[0]) : p(3\|cold) or p(3\|hot)
            delta[state] = self.start_prob(state) * self.emit_prob(state, sequence[0])
            
        # pre : backtrace
        pre = []
        
        # sequence의 두번째 값부터 마지막까지 delta, backtrace 모두 계산
        # index : 위 수식에서 t
        for index in range(1, sequence_length):
            # delta_bar : t번째 관측치의 비터비 확률들
            # index가 거듭될수록 그 요소가 늘어남
            # 다 돌면 sequence_length 길이
            delta_bar = {}
            # pre_state : t번째 관측치의 backtrace들
            # index가 거듭될수록 그 요소가 늘어남
            # 다 돌면 sequence_length 길이
            pre_state = {}
            for state_to in self._states:
                max_prob = 0
                max_state = None # backtrace 변수
                for state_from in self._states:
                    # state_from : 위 수식에서 i
                    # state_to : 위 수식에서 j
                    # delta[state_from] : 직전 상태의 비터비 확률(저장된 값 불러와 계산량 줄임)
                    # trans_prob : 위 수식에서 a
                    prob = delta[state_from] * self.trans_prob(state_from, state_to)
                    # 비터비 확률 수식에서 i에 대해 최대값을 구하는데,
                    # 방출확률 b는 i에 대해 무관하므로 최대값 연산에서 제외
                    if prob > max_prob:
                        # 최대값 저장 : 현재 상태의 비터비 확률
                        max_prob = prob 
                        # 최대값의 위치 저장 : 현재 상태의 backtrace
                        max_state = state_from 
                delta_bar[state_to] = max_prob * self.emit_prob(state_to, sequence[index])
                pre_state[state_to] = max_state
            # o_2까지의 비터비 확률을 구했다면 o_1 이전의 비터비 확률은 불필요
            # o_2의 비터비 확률들의 모음인 delta_bar를 전체 delta에 덮어씌움
            delta = delta_bar
            # o_2까지의 backtrace를 구했다 하더라도 o_3은 달라질 수 있음
            # pre에 pre_state를 append
            pre.append(pre_state)
	    
        # 전체 시퀀스를 대상으로 최대 비터비확률과
        # 최대 비터비 확률을 내는 state 찾기
        # 현재 delta에는 시퀀스의 마지막 요소(O_T)에 
        # 해당하는 비터비 확률들이 저장돼 있기 때문
        # (state로만 구분되어 있음)
        max_state = None
        max_prob = 0
        for state in self._states:
            if delta[state] > max_prob:
                max_prob = delta[state]
                max_state = state

        if max_state is None:
            return []
	   
        # 최대 비터비 확률을 내는 state가 backtrace의 첫번째 요소
        result = [max_state]
        # index를 시퀀스의 역방향으로 후진하면서
        for index in range(sequence_length - 1, 0, -1):
            # index에 해당하는 max_state들을 뽑아내기
            # 이는 저 위쪽에서 이미 max_state들을 저장해두었기 때문에 가능
            max_state = pre[index - 1][max_state]
            # 뽑아낸 max_state들을 result의 첫번째 위치에 저장
            result.insert(0, max_state)

        return result
```





## Training

은닉마코프모델의 학습 의사코드는 다음과 같습니다.

<a href="https://imgur.com/ukU14ub"><img src="https://i.imgur.com/ukU14ub.png" width="600px" title="source: imgur.com" /></a>

파이썬으로 구현한 결과는 다음과 같습니다.

```python
   def learn(self, sequence, smoothing=0):

        length = len(sequence)
        alpha = self._forward(sequence)
        beta = self._backward(sequence)

        gamma = []
        for index in range(length):
            prob_sum = 0
            gamma.append({})
            for state in self._states:
                prob = alpha[index][state] * beta[index][state]
                gamma[index][state] = prob
                prob_sum += prob

            if prob_sum == 0:
                continue

            for state in self._states:
                gamma[index][state] /= prob_sum

        xi = []
        for index in range(length - 1):
            prob_sum = 0
            xi.append({})
            for state_from in self._states:
                xi[index][state_from] = {}
                for state_to in self._states:
                    prob = alpha[index][state_from] * beta[index + 1][state_to] * \
                        self.trans_prob(state_from, state_to) * \
                        self.emit_prob(state_to, sequence[index + 1])
                    xi[index][state_from][state_to] = prob
                    prob_sum += prob

            if prob_sum == 0:
                continue

            for state_from in self._states:
                for state_to in self._states:
                    xi[index][state_from][state_to] /= prob_sum

        states_number = len(self._states)
        symbols_number = len(self._symbols)
        for state in self._states:
            # update start probability
            self._start_prob[state] = \
                (smoothing + gamma[0][state]) / (1 + states_number * smoothing)

            # update transition probability
            gamma_sum = 0
            for index in range(length - 1):
                gamma_sum += gamma[index][state]

            if gamma_sum > 0:
                denominator = gamma_sum + states_number * smoothing
                for state_to in self._states:
                    xi_sum = 0
                    for index in range(length - 1):
                        xi_sum += xi[index][state][state_to]
                    self._trans_prob[state][state_to] = (smoothing + xi_sum) / denominator
            else:
                for state_to in self._states:
                    self._trans_prob[state][state_to] = 0

            # update emission probability
            gamma_sum += gamma[length - 1][state]
            emit_gamma_sum = {}
            for symbol in self._symbols:
                emit_gamma_sum[symbol] = 0

            for index in range(length):
                emit_gamma_sum[sequence[index]] += gamma[index][state]

            if gamma_sum > 0:
                denominator = gamma_sum + symbols_number * smoothing
                for symbol in self._symbols:
                    self._emit_prob[state][symbol] = \
                        (smoothing + emit_gamma_sum[symbol]) / denominator
            else:
                for symbol in self._symbols:
                    self._emit_prob[state][symbol] = 0        
```





## 코드 실행

원저자의 코드는 [이곳](https://github.com/jason2506/PythonHMM/blob/master/hmm.py), 백업용으로 올려놓은 코드는 [이곳](https://gist.github.com/ratsgo/69376c0575bc34fda5992f66c83e7fad)에 있습니다. 은닉마코프모델을 수동으로 구성(모델이 이미 있는 것으로 전제)해 그 작동을 확인해보고자 한다면 아래와 같이 실행하면 됩니다. (위의 그림 예시와 같으나 end state는 없는 걸로 가정)

```python
import hmm
states = ('hot', 'cold')
symbols = ('1', '2', '3')

start_prob = {
    'hot' : 0.8,
    'cold' : 0.2
}

trans_prob = {
    'hot': { 'hot' : 0.6, 'cold' : 0.4 },
    'cold': { 'hot' : 0.4, 'cold' : 0.6 }
}

emit_prob = {
    'hot': { '1' : 0.2, '2' : 0.4, '3' : 0.4 },
    'cold': { '1' : 0.5, '2' : 0.4, '3' : 0.1 }
}

model = hmm.Model(states, symbols, start_prob, trans_prob, emit_prob)
sequence = ['3', '1', '3']
print(model.evaluate(sequence)) # Likelihood 계산
print(model.decode(sequence)) # 최적상태열 추정
```

EM 알고리즘을 통한 학습은 다음과 같이 합니다.

```python
import hmm
sequences = [
    (state_list1, symbol_list1),
    (state_list2, symbol_list2),
    ...
    (state_listN, symbol_listN)]
model = hmm.train(sequences)
```