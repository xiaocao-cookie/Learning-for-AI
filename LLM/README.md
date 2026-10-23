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

## 05_prompt_engineering.ipynb

本 notebook 主要介绍 **生成式大语言模型的使用方式以及 Prompt Engineering（提示词工程）**，重点讲解如何通过模型参数、提示词结构、推理方法和输出约束来提升文本生成质量与可控性。

内容首先以 `microsoft/Phi-3-mini-4k-instruct` 为例，介绍如何使用 Hugging Face Transformers 加载文本生成模型，并通过 `apply_chat_template()` 查看聊天消息在模型内部使用的 Prompt 模板。随后介绍 `temperature` 和 `top_p` 等生成参数，说明它们如何影响 Token 采样过程以及生成文本的随机性和多样性。

接着系统介绍 **Prompt Engineering 的基本组成与高级设计方法**。基础提示词通常由 Instruction、Data 和 Output Indicator 构成，在此基础上进一步扩展出 **Persona、Context、Format、Audience、Tone 和 Data** 等模块，并通过论文总结案例展示不同提示词组合对生成结果的影响。同时介绍 **In-context Learning（上下文内学习）**，包括 Zero-shot、One-shot 和 Few-shot，以及通过 **Prompt Chaining（提示词链）** 将复杂任务拆分成多个连续步骤的方法。

随后进入生成式模型的**推理提示技术**，介绍 **Chain-of-Thought（CoT）**、Zero-shot CoT、**Self-Consistency（自洽性）** 和 **Tree-of-Thought（ToT，思维树）**。这些方法通过增加中间推理步骤、重复采样并选择一致答案，或者并行探索多种解决路径，使模型能够在复杂任务中获得更好的输出结果。

最后介绍 **LLM 输出验证与约束**。Notebook 从 Structured Output、有效性、安全性和准确性等角度说明为什么需要验证模型输出，并比较通过示例、Grammar 和 Fine-tuning 控制输出的方法。随后使用 `llama-cpp-python` 加载 Phi-3 的 GGUF 模型，并利用 **JSON Grammar / `response_format`** 在 Token 生成阶段约束模型，使其稳定生成符合 JSON 格式的结构化结果。

通过这些实验，本 notebook 展示了一条完整的生成式模型使用流程：**模型加载与生成参数控制 → Prompt 基础结构 → 高级 Prompt Engineering → In-context Learning → Prompt Chaining → CoT / Self-Consistency / ToT 推理 → 输出验证与结构化约束**，说明了如何通过提示词和生成控制技术提升 LLM 输出的质量、推理能力与可控性。


## 06_advanced_text_generation_tech_and_tools.ipynb

本 notebook 主要介绍 **如何使用 LangChain 和 LangGraph 将单独的大语言模型扩展为具有 Chain、Memory 和 Agent 能力的完整 LLM 应用系统**，重点从模型调用逐步过渡到多步骤工作流、对话记忆以及工具调用。

内容首先介绍 **GGUF 与模型量化（Quantization）**，以 Phi-3-mini 为例说明如何使用较低精度的量化模型减少模型所需的内存和 VRAM，并通过 `llama-cpp-python` 与 LangChain 的 `LlamaCpp` 加载 GGUF 模型。在此基础上使用 `PromptTemplate` 构建 Phi-3 所需要的提示词格式，实现 LangChain 中基本的 Model I/O。

随后介绍 **Chains（链）与 LCEL（LangChain Expression Language）**。通过 `Prompt | LLM | OutputParser` 的方式将多个组件组合起来，并进一步利用 `RunnablePassthrough.assign()` 将复杂任务拆分为多个顺序执行的子任务。例如先根据摘要生成故事标题，再生成角色描述，最后结合这些结果生成完整故事，从而展示 LLM 工作流的组合能力。

接着重点介绍 **Memory（记忆）机制**。Notebook 使用 LangGraph 的 `State`、`Checkpointer` 和 `thread_id` 实现对话状态持久化，并分别演示 **Conversation Buffer、Windowed Conversation Buffer 和 Conversation Summary** 三种经典记忆策略。同时进一步区分 **Short-term Memory（短期记忆）和 Long-term Memory（长期记忆）**，说明短期记忆主要通过 Checkpointer 保存同一会话中的状态，而长期记忆可以通过 Store 保存跨会话共享的语义记忆、情景记忆和程序性记忆。

最后介绍 **Agent 与 ReAct（Reasoning and Acting）框架**。Agent 不再按照固定流程执行任务，而是由 LLM 根据当前问题自行决定下一步需要调用什么工具。Notebook 使用 LangChain 的 `create_agent()` 创建 ReAct Agent，并为其提供 **Apple 官网 MacBook Pro 价格查询工具**和**美元兑换欧元工具**，让 Agent 根据用户需求自动完成信息获取、工具调用和结果整合。同时通过 LangGraph 的 `InMemorySaver` 为 Agent 增加短期记忆，并对比有记忆和无记忆情况下的多轮对话效果。

通过这些实验，本 notebook 展示了一条从基础 LLM 到 Agent 系统的完整扩展路径：**GGUF / Quantization → Model I/O → PromptTemplate → LCEL Chains → Memory → LangGraph State / Checkpointer → Tools → ReAct → Agent**，说明了如何利用 LangChain 和 LangGraph 将语言模型构建成能够执行多步骤任务、保持上下文并调用外部工具的智能应用。


## 07_semantic_search_and_RAG.ipynb

本 notebook 主要介绍 **语义搜索（Semantic Search）、重排序（Reranking）以及 RAG（Retrieval-Augmented Generation，检索增强生成）** 的基本原理与完整实现流程，重点说明如何通过检索外部知识减少 LLM 幻觉，并提升生成结果的事实准确性。

内容首先介绍 **Dense Retrieval（稠密检索）**。Dense Retrieval 利用 Embedding 将用户 Query 和文档映射到同一个向量空间，再根据向量距离寻找语义最接近的文档。Notebook 以 GLM-5.3 的介绍文档为例，使用智谱 `embedding-3` 生成文本向量，并利用 **FAISS** 构建向量搜索索引，完成 `Embedding → Index → Nearest Neighbor Search` 的语义检索流程。同时介绍 Flat、IVF 和 HNSW 等常见向量索引技术，并使用 **BM25** 实现关键词检索，对比语义搜索与传统关键词搜索之间的区别。

随后分析 **Dense Retrieval 的局限性与优化方法**。当知识库中不存在答案时，Dense Retrieval 仍然可能返回语义距离最近但实际上无关的内容；对于需要精确关键词匹配的场景，则更适合结合 BM25 构建 **Hybrid Search（混合检索）**。Notebook 进一步介绍固定长度、滑动窗口、递归、语义、文档结构和层次化等多种 **Chunking（文本切块）策略**，以及通过正负样本微调 Embedding 模型，使相关 Query 与文档在向量空间中更加接近。

接着介绍 **Reranking（重排序）**。初步检索负责从大量文档中快速召回候选结果，而 Reranker 再对这些候选文档进行更加精确的相关性评分。Notebook 重点介绍基于 **Cross-Encoder** 的重排序方式，即将 Query 和候选文档同时输入模型，计算两者之间的相关性分数，并通过智谱 Rerank API 演示候选文档重新排序的过程。

在检索效果评估部分，Notebook 系统介绍 **Precision@K、Recall@K、MRR、AP、MAP 和 NDCG@K** 等信息检索指标。其中 Precision 和 Recall 分别关注检索结果的准确程度与覆盖程度，MRR 关注第一个相关文档出现的位置，MAP 衡量多个相关文档的整体排序质量，而 **NDCG@K** 进一步考虑文档的多级相关性以及排名位置，尤其适合评估 Reranker 和 RAG 中的排序质量。

随后从语义搜索进一步过渡到 **RAG**。RAG 在检索流程之后增加生成模型，将用户问题和检索得到的相关文档共同提供给 LLM，使模型基于外部知识回答问题。Notebook 使用 `Phi-3-mini-4k` 作为生成模型、`thenlper/gte-small` 作为 Embedding 模型，并通过 LangChain 的 **FAISS VectorStore、Retriever、PromptTemplate 和 LCEL** 构建完整的 RAG Pipeline，实现 **Query → Retriever → Context → Prompt → LLM → Answer** 的基本流程。

在基础 RAG 之上，Notebook 进一步介绍多种 **高级 RAG 技术**，包括通过 LLM 简化和优化用户问题的 **Query Rewriting（查询重写）**、将复杂问题拆分成多个搜索请求的 **Multi-Query RAG**、需要根据前一步结果继续检索的 **Multi-hop RAG**，以及根据问题类型将查询发送到不同知识库或业务系统的 **Query Routing（查询路由）**。

最后系统介绍 **RAG 评估体系**。除了前面介绍的检索和重排序指标之外，还从 Context Precision、Context Recall 等指标评价检索上下文质量；通过 Faithfulness、Answer Relevancy、Answer Correctness 等指标评价生成答案质量；通过 Citation Recall 和 Citation Precision 评价引用质量；并使用 Latency、TTFT、Throughput、Token Usage、Cost per Query 以及 P50/P95/P99 等指标评价 RAG 系统上线后的工程性能。

通过这些实验，本 notebook 展示了一条完整的 RAG 技术路线：**文本切块 → Embedding → FAISS 向量索引 → Dense Retrieval / BM25 → Hybrid Search → Reranking → 检索评估 → Retriever → Context → LLM → RAG → Query Rewriting / Multi-Query / Multi-hop / Routing → RAG 全链路评估**，说明了如何从基础语义搜索逐步构建一个具有较高检索质量、事实准确性和工程可评估性的 RAG 系统。


## BPE_with_Python.ipynb

使用 Python 实现 Byte Pair Encoding 算法。

本 notebook 从零实现了 BPE 的核心流程，包括初始化词表、统计相邻 token pair 的频率、选择最高频 pair、合并词表，并保存每一轮得到的 merge rules。

示例中先使用 `low`、`lower`、`lowest` 等简单语料演示 BPE 的合并过程，帮助理解子词是如何一步步生成的。随后使用 `names.txt` 中的英文名字数据进行训练，并展示训练得到的合并规则和最终词表。

最后，notebook 实现了 `encode_word` 方法，用训练好的 BPE merge rules 对新单词进行分词，从而完整演示了 BPE 从训练到编码的基本过程。




## hello_world.ipynb

LLM 入门示例，用于演示如何使用 Hugging Face `transformers` 加载本地大语言模型并完成文本生成。

该 Notebook 使用 `microsoft/Phi-3-mini-4k-instruct` 作为示例模型，包含依赖安装、模型加载、Tokenizer 初始化、文本生成 Pipeline 构建，以及中英文 Prompt 调用示例。

适合作为学习大语言模型调用流程的第一个 `Hello World` 案例。