import sys
import wordcloud
import jieba

from data_processor import (readFile, filterData, splitMessage, list2Messages,
                            filterNontext)

if __name__ == '__main__':
    raw_data = readFile(sys.argv[1])
    filtered_data = filterData(raw_data)
    message_list = splitMessage(filtered_data)
    messages = list2Messages(message_list)
    filtered_messages = filterNontext(messages)

    content_list = []
    nickname_list = []

    for message in filtered_messages:
        content_list.append(message.content)
        nickname_list.append(message.sender)

    content = ' '.join(content_list)
    nickname = ' '.join(nickname_list)
    jieba_content_list = jieba.lcut(content)
    # this list is used for filter the nickname
    jieba_nikename_list = jieba.lcut(nickname)
    text = ' '.join(jieba_content_list)

    # custom stopword list
    custom_stopwords = []

    stopwords = custom_stopwords + jieba_nikename_list
    wc = wordcloud.WordCloud(font_path="msyh.ttc",
                             width=1000,
                             height=700,
                             background_color='white',
                             max_words=100,
                             stopwords=stopwords)

    # generate wordcloud
    wc.generate(text)
    wc.to_file('./out/wordcloud.png')
