# LLM

## 01_tokenizer_and_embedding.ipynb

本 notebook 主要介绍大语言模型中的 **分词器（Tokenizer）** 和 **嵌入（Embedding）**。

内容从 LLM 如何把文本拆分成 token 开始，依次讲解词级、子词级、字符级和字节级等不同分词方式，并对比了 BERT、GPT-2、FLAN-T5、GPT-4、StarCoder2、Galactica、Phi-3 等模型的分词器特点，包括分词方法、词表大小和特殊词元的作用。

随后介绍了词元嵌入的基本概念：模型会先把 token id 转换成向量，再结合上下文生成更有语义的信息表示。基于这些向量，可以进一步用于命名实体识别、文本摘要、文本相似度计算等任务。

最后， notebook 还扩展到句子级文本嵌入、Word2Vec 词嵌入，以及推荐系统中的嵌入应用，展示了 Embedding 不仅可以用于语言模型，也可以用于相似度计算、语义检索和内容推荐等场景。


## 02_looking_inside_transformer_LLMs.ipynb

本 notebook 主要介绍 **Transformer 大语言模型的内部结构和文本生成过程**。

内容以 `microsoft/Phi-3-mini-4k-instruct` 为例，演示如何使用 Hugging Face Transformers 加载模型和分词器，并通过文本生成 Pipeline 完成文本续写任务。

随后逐层分析 Phi-3 模型的架构，包括词元嵌入层、Decoder Layer、Self-Attention、MLP、RMSNorm、旋转位置编码以及 `lm_head`，并展示模型如何将输入 token 转换为上下文表示，再映射为整个词表中各个 token 的预测分数。

最后介绍了 **KV-Cache** 的基本作用，通过对比启用和关闭 KV-Cache 时的文本生成速度，说明它如何复用已经计算过的 Key 和 Value，从而减少重复计算并提升自回归生成效率。


## 03_text_classification.ipynb

本 notebook 主要介绍 **大语言模型与表示模型在文本分类任务中的应用**，并以电影评论情感分类为主要案例，对比不同分类方法的实现方式和效果。

内容首先使用 `rotten_tomatoes` 数据集作为实验数据，并介绍 **BERT、RoBERTa、DistilBERT、ALBERT 和 DeBERTa** 等常见 Transformer 表示模型及其主要特点。随后使用针对情感分析微调过的 `cardiffnlp/twitter-roberta-base-sentiment-latest` 模型直接进行分类，并通过 Precision、Recall、F1-score 和 Accuracy 等指标评估模型性能。

接着介绍如何使用 `sentence-transformers/all-mpnet-base-v2` 将文本转换为 **Embedding 向量**，并基于这些向量完成不同形式的文本分类，包括使用 Logistic Regression 的**有监督分类**、通过计算类别中心向量和 Cosine Similarity 的**无监督分类**，以及根据类别文本描述进行匹配的 **Zero-shot Classification（零样本分类）**。

最后介绍如何使用 **生成模型进行文本分类**，通过 `google/flan-t5-small` 将情感分类问题转换为文本生成任务，让模型直接生成 `positive` 或 `negative` 作为分类结果。通过这些实验，本 notebook 展示了文本分类的几种主要思路：**任务专用模型、Embedding + 分类器、Embedding 相似度分类、Zero-shot 分类以及生成式分类**，并比较了不同方法在同一情感分析任务上的表现。


## 04_text_clf_and_topic_modeling.ipynb

本 notebook 主要介绍 **Transformer Embedding 在无监督文本学习中的应用**，重点讲解 **文本聚类（Text Clustering）和主题建模（Topic Modeling）** 的基本原理与实现流程。

内容首先以 ArXiv 的 `cs.CL` 论文摘要数据集为例，介绍文本聚类的通用流程：使用 `thenlper/gte-small` 将文本转换为 **Embedding 向量**，再使用 **UMAP** 对高维嵌入进行降维，最后利用 **HDBSCAN** 根据文本之间的语义关系完成聚类。同时系统介绍了 **K-Means、DBSCAN、HDBSCAN 和 GMM** 等常见聚类算法，以及 Homogeneity、Completeness、V-measure、ARI 和 Silhouette Coefficient 等聚类评价指标。

随后从文本聚类进一步过渡到 **BERTopic 主题建模**。BERTopic 延续了 `Embedding → UMAP → HDBSCAN` 的聚类流程，然后利用 **词袋模型和 c-TF-IDF** 从每个聚类中提取具有代表性的关键词，从而将语义相近的文档簇转换为可以解释的主题。Notebook 还展示了主题查询、主题搜索以及文档分布、主题热力图和主题层次关系等多种可视化方法。

最后进一步介绍 BERTopic 的 **模块化主题表示机制**。通过 `KeyBERTInspired` 利用 Embedding 相似度重新排序主题关键词，并使用 **Maximal Marginal Relevance（MMR）** 在关键词相关性与多样性之间进行权衡，从而减少主题词之间的语义冗余。在此基础上，还使用 `Flan-T5` 生成模型作为 BERTopic 的表示模块，根据主题关键词和代表性文档直接生成更加自然的**主题标签**。

通过这些实验，本 notebook 展示了一条完整的无监督文本分析流程：**文本 Embedding → 降维 → 聚类 → BERTopic 主题建模 → c-TF-IDF 主题表示 → KeyBERT/MMR 优化 → 生成模型生成主题标签**，说明了如何从大量未标注文本中自动发现语义结构和潜在主题。



## BPE_with_Python.ipynb

使用 Python 实现 Byte Pair Encoding 算法。

本 notebook 从零实现了 BPE 的核心流程，包括初始化词表、统计相邻 token pair 的频率、选择最高频 pair、合并词表，并保存每一轮得到的 merge rules。

示例中先使用 `low`、`lower`、`lowest` 等简单语料演示 BPE 的合并过程，帮助理解子词是如何一步步生成的。随后使用 `names.txt` 中的英文名字数据进行训练，并展示训练得到的合并规则和最终词表。

最后，notebook 实现了 `encode_word` 方法，用训练好的 BPE merge rules 对新单词进行分词，从而完整演示了 BPE 从训练到编码的基本过程。




## hello_world.ipynb

LLM 入门示例，用于演示如何使用 Hugging Face `transformers` 加载本地大语言模型并完成文本生成。

该 Notebook 使用 `microsoft/Phi-3-mini-4k-instruct` 作为示例模型，包含依赖安装、模型加载、Tokenizer 初始化、文本生成 Pipeline 构建，以及中英文 Prompt 调用示例。

适合作为学习大语言模型调用流程的第一个 `Hello World` 案例。