import jieba
#import jieba.analyse as analyse
#import jieba.analyse
from jieba import analyse
import jieba
import jieba.analyse

# 待分词的文本路径
sourceTxt = './能源数据安全/result_1.txt'
# 分好词后的文本路径
targetTxt = './能源数据安全/target.txt'
def Open():
# 对文本进行操作
    with open(sourceTxt, 'r', encoding = 'utf-8') as sourceFile, open(targetTxt, 'a+', encoding = 'utf-8') as targetFile:
        for line in sourceFile:
            seg = jieba.cut(line.strip(), cut_all = False)
        # 分好词之后之间用空格隔断
            output = ' '.join(seg)
            targetFile.write(output)
            targetFile.write('\n')
        print('写入成功！')
def close():
# 提取关键词
    with open(targetTxt, 'r', encoding = 'utf-8') as file:
        text = file.readlines()
    # """
    # 几个参数解释：
    #     * text : 待提取的字符串类型文本
    #     * topK : 返回TF-IDF权重最大的关键词的个数，默认为20个
    #     * withWeight : 是否返回关键词的权重值，默认为False
    #     * allowPOS : 包含指定词性的词，默认为空
    # """
        keywords = jieba.analyse.extract_tags(str(text), topK = 10, withWeight=True, allowPOS=())
       # file.write(keywords)

        with open('./能源数据安全/keyword.txt', 'w', encoding='utf-8') as f:
            keywords=str(keywords)
            print(keywords)
            f.write(keywords)

# def write():
#     with open('./能源数据安全/target.txt', 'r', encoding = 'utf-8') as f:
#         keywords=close()
#         keywords=keywords.join()
#         print(keywords)
#         #f.write(keywords)
    print('finish ')


if __name__ == '__main__':
        #delbank()
        Open()
        close()