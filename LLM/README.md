# LLM

## 01_tokenizer_and_embedding.ipynb

本 notebook 主要介绍大语言模型中的 **分词器（Tokenizer）** 和 **嵌入（Embedding）**。

内容从 LLM 如何把文本拆分成 token 开始，依次讲解词级、子词级、字符级和字节级等不同分词方式，并对比了 BERT、GPT-2、FLAN-T5、GPT-4、StarCoder2、Galactica、Phi-3 等模型的分词器特点，包括分词方法、词表大小和特殊词元的作用。

随后介绍了词元嵌入的基本概念：模型会先把 token id 转换成向量，再结合上下文生成更有语义的信息表示。基于这些向量，可以进一步用于命名实体识别、文本摘要、文本相似度计算等任务。

最后， notebook 还扩展到句子级文本嵌入、Word2Vec 词嵌入，以及推荐系统中的嵌入应用，展示了 Embedding 不仅可以用于语言模型，也可以用于相似度计算、语义检索和内容推荐等场景。



## BPE_with_Python.ipynb

使用 Python 实现 Byte Pair Encoding 算法。

本 notebook 从零实现了 BPE 的核心流程，包括初始化词表、统计相邻 token pair 的频率、选择最高频 pair、合并词表，并保存每一轮得到的 merge rules。

示例中先使用 `low`、`lower`、`lowest` 等简单语料演示 BPE 的合并过程，帮助理解子词是如何一步步生成的。随后使用 `names.txt` 中的英文名字数据进行训练，并展示训练得到的合并规则和最终词表。

最后，notebook 实现了 `encode_word` 方法，用训练好的 BPE merge rules 对新单词进行分词，从而完整演示了 BPE 从训练到编码的基本过程。




## hello_world.ipynb

LLM 入门示例，用于演示如何使用 Hugging Face `transformers` 加载本地大语言模型并完成文本生成。

该 Notebook 使用 `microsoft/Phi-3-mini-4k-instruct` 作为示例模型，包含依赖安装、模型加载、Tokenizer 初始化、文本生成 Pipeline 构建，以及中英文 Prompt 调用示例。

适合作为学习大语言模型调用流程的第一个 `Hello World` 案例。