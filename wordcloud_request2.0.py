from pyecharts.charts import WordCloud
from pyecharts.globals import ThemeType
words = [
    ('知识图谱',6000),
    ('Knowledge graph',5000),
    ('知识存储',5000),
    ('知识抽取',5000),
    ('实体对齐',4000),
    ('知识融合',5000),
    ('实体命名识别',4000),
    ('关系抽取',4000),
    ('Neo4j',3000),
    ('TransE',3000),
    ('图卷积GCN',3000),
    ('BERT', 3000),
    ('注意力机制', 3000),
    ('Transformer结构', 3000),
    ('RNN', 3000),
    ('LSTM', 3000),
    ('傅里叶变化', 3000),
]
(
    WordCloud()
    .add("", words, word_size_range=[12, 60], shape='circle')
    .render()
)