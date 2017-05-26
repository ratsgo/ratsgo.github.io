---
title: 딥러닝 이전의 문서 분류
category: From frequency to semantics
tag: document classification
---

이번 글에서는 딥러닝이 주목받기 전인 2000년대 초반까지의 문서 분류 방식에 대해 살펴보도록 하겠습니다. [AK Nassirtoussi(2015)](http://www.sciencedirect.com/science/article/pii/S0957417414004801)는 금융 관련 문서들로 주가를 예측하는 연구를 했었는데요, 도메인이 금융에 특화돼 있긴 하지만 기존 문서 분류 연구들을 잘 정리해놓은 것 같다는 생각에 이를 인용해봤습니다. 그럼 시작하겠습니다.



## 문서 전처리

2000년대 초반 연구에서는 비정형데이터를 정형데이터로 변환하는 데 **TF-IDF**가 많이 쓰인 점을 확인할 수 있습니다. 토픽모델링 기법인 **Latent Dirichlet Allocation**을 입력 벡터로 만든 연구도 눈에 띕니다. 요즘엔 구글에서 2013년 개발한 **Word2Vec**이나 미국 스탠포드에서 개발한 **GloVe** 등을 주로 쓰고 있다는 점을 생각하면 격세지감이네요. TF-IDF에 대해 자세한 내용은 [이곳](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/28/tfidf/)을, Word2Vec에 대해서는 [이곳](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/03/30/word2vec/), GloVe는 [이곳](https://ratsgo.github.io/from%20frequency%20to%20semantics/2017/04/09/glove/)을 참고하시면 좋을 것 같습니다.

<a href="http://imgur.com/JlGAbLy"><img src="http://i.imgur.com/JlGAbLy.png" title="source: imgur.com" /></a>



## 분류 모델

분류 모델로는 **서포트 벡터 머신(SVM)** 계열 비중이 압도적입니다. 그도 그럴 것이 딥러닝 이전 뛰어난 성능으로 많은 주목을 받았던 모델 때문이 아닌가 생각합니다. 이밖에 **선형회귀**, **나이브 베이지안**, **K-NN** 같은 비교적 간단한 모델도 분류기로 많이 쓰였습니다. 요즘에는 **Convolutional Neural Networks**, **Recurrent Neural Networks**, **Recursive Neural Networks** 등 딥러닝 모델들이 각광받고 있습니다. 

SVM에 대한 자세한 내용은 [이곳](https://ratsgo.github.io/machine%20learning/2017/05/23/SVM/)을, 나이브 베이지안 모델은 [이곳](https://ratsgo.github.io/machine%20learning/2017/05/18/naive/), K-NN은 [이곳](https://ratsgo.github.io/machine%20learning/2017/04/17/KNN/)을 참고하면 좋을 것 같습니다. 아울러 CNN은 [이곳](https://ratsgo.github.io/natural%20language%20processing/2017/03/19/CNN/), Recurrent Neural Networks는 [이곳](https://ratsgo.github.io/natural%20language%20processing/2017/03/09/rnnlstm/), Recursive Neural Networks는 [이곳](https://ratsgo.github.io/deep%20learning/2017/04/03/recursive/)을 보시면 좋을 것 같습니다.

<a href="http://imgur.com/ORYsKWB"><img src="http://i.imgur.com/ORYsKWB.png" title="source: imgur.com" /></a>



## Appendix

제가 인용한 논문입니다. 

Nassirtoussi, A. K., Aghabozorgi, S., Wah, T. Y., & Ngo, D. C. L. (2015). Text mining of news-headlines for FOREX market prediction: A Multi-layer Dimension Reduction Algorithm with semantics and sentiment. *Expert Systems with Applications*, *42*(1), 306-324.

표에 언급된 논문 목록입니다.

Wuthrich, B., Cho, V., Leung, S., Permunetilleke, D., Sankaran, K., & Zhang, J. (1998). Daily stock market forecast from textual web data. In 1998 IEEE international conference on systems, man, and cybernetics (Vols. 3 and 2723, pp. 2720–2725).

Peramunetilleke, D., & Wong, R. K. (2002). Currency exchange rate forecasting from news headlines. Australian Computer Science Communications, 24, 131–139.

Werner, A., & Myrray, Z. F. (2004). Is all that talk just noise ? The information content of internet stock message boards. Journal of Finance, 1259–1294.

Mittermayer, M. A. (2004). Forecasting intraday stock price trends with text mining techniques. In Proceedings of the 37th annual Hawaii international conference on system sciences, 2004 (p. 10).

Das, S. R., & Chen, M. Y. (2007). Yahoo! for Amazon: Sentiment extraction from small talk on the web. Management Science, 53, 1375–1388.

Soni, A., van Eck, N. J., & Kaymak, U. (2007). Prediction of stock price movements based on concept map information. In IEEE symposium on computational intelligence in multicriteria decision making (pp. 205–211).

Zhai, Y., Hsu, A., & Halgamuge, S. K. (2007). Combining news and technical indicators in daily stock price trends prediction. In Proceedings of the fourth international symposium on neural networks: advances in neural networks, Part III (pp. 1087–1096). Nanjing, China: Springer-Verlag.

Rachlin, G., Last, M., Alberg, D., & Kandel, A. (2007). ADMIRAL: A data mining based financial trading system. In IEEE symposium on computational intelligence and data mining, 2007. CIDM 2007 (pp. 720–725).

Tetlock, P. C., Saar-Tsechansky, M., & Macskassy, S. (2008). More than words: Quantifying language to measure firms’ fundamentals. The Journal of Finance, 63, 1437–1467.

Mahajan, A., Dey, L., & Haque, S. M. (2008). Mining financial news for major events and their impacts on the market. In IEEE/WIC/ACM international conference on web intelligence and intelligent agent technology, 2008. WI-IAT ‘08 (Vol. 1, pp. 423–426).

Butler, M., & Kešelj, V. (2009). Financial forecasting using character N-gram analysis and readability scores of annual reports. In Y. Gao & N. Japkowicz (Eds.). Advances in artificial intelligence (Vol. 5549, pp. 39–51). Berlin, Heidelberg: Springer.

Schumaker, R. P., & Chen, H. (2009). Textual analysis of stock market prediction using breaking financial news: The AZF in text system. ACM Transactions on Information Systems, 27, 1–19.

Lugmayr, A., & Gossen, G. (2012). Evaluation of methods and techniques for language based sentiment analysis for DAX 30 stock exchange – a first concept of a ‘‘LUGO’’ sentiment indicator. In Lugmayr, A., Risse, T., Stockleben, B., Kaario, J., Pogorelc, B., & Serral Asensio, E. (Eds.). SAME 2012 – fifth international workshop on semantic ambient media experience.

Yu, Y., Duan, W., & Cao, Q. (2013). The impact of social and conventional media on firm equity value: A sentiment analysis approach. Decision Support Systems.

Hagenau, M., Liebmann, M., & Neumann, D. (2013). Automated news reading: Stock price prediction based on financial news using context-capturing features. Decision Support Systems, 55, 685–697.

Jin, F., Self, N., Saraf, P., Butler, P., Wang, W., & Ramakrishnan, N. (2013). Forexforeteller: Currency trend modeling using news articles. In Proceedings of the 19th ACM SIGKDD international conference on Knowledge discovery and data mining (pp. 1470–1473). Chicago, IL, USA: ACM.

Chatrath, A., Miao, H., Ramchander, S., & Villupuram, S. (2014). Currency jumps, cojumps and the role of macro news. Journal of International Money and Finance, 40, 42–62.

Bollen, J., Huina, M., & Zeng, Xiao-Jun (2010). Twitter mood predicts the stock market. Journal of Computational Science, 2, 1–8.

Vu, T. T., Chang, S., Ha, Q. T., & Collier, N. (2012). An experiment in integrating sentiment features for tech stock prediction in twitter. In Proceedings of the workshop on information extraction and entity analytics on social media data (pp. 23–38). Mumbai, India: The COLING 2012 Organizing Committee.

Pui Cheong Fung, G., Xu Yu, J., & Wai, L. (2003). Stock prediction: Integrating text mining approach using real-time news. In Proceedings. 2003 IEEE international conference on computational intelligence for financial engineering (pp. 395–402).

Schumaker, R. P., Zhang, Y., Huang, C.-N., & Chen, H. (2012). Evaluating sentiment in financial news articles. Decision Support Systems, 53, 458–464.

Li, F. (2010). The information content of forward-looking statements in corporate filings—a Naïve Bayesian machine learning approach. Journal of Accounting Research, 48, 1049–1102.

Li, C. H., Yang, J. C., & Park, S. C. (2012). Text categorization algorithms using semantic approaches, corpus-based thesaurus and WordNet. Expert Systems with Applications, 39, 765–772.

Huang, C.-J., Liao, J.-J., Yang, D.-X., Chang, T.-Y., & Luo, Y.-C. (2010). Realization of a news dissemination agent based on weighted association rules and text mining techniques. Expert Systems with Applications, 37, 6409–6413.

Groth, S. S., & Muntermann, J. (2011). An intraday market risk management approach based on textual analysis. Decision Support Systems, 50, 680–691.