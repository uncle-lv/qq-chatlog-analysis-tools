import os
from typing import List
from itertools import groupby

from message import Message


def readFile(fileName: str) -> List[str]:
    data_list = []
    url = os.path.normpath('./in/' + fileName)
    with open(url, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data_list.append(line.replace('\n', ''))
    return data_list


def filterData(raw_data: List[str]) -> List[str]:
    filtered_data = raw_data[7:]
    return filtered_data


def splitMessage(filtered_data: List[str]) -> List[List[str]]:
    message_list = [
        list(v) for k, v in groupby(filtered_data, lambda x: x == '') if not k
    ]
    return message_list


def list2Messages(message_list: List[List[str]]) -> List[Message]:
    messages = []
    for item in message_list:
        message_heaer = item[0]
        header_segments = message_heaer.split(' ')
        time = header_segments[0] + header_segments[1]
        sender = header_segments[2]
        message = Message(sender=sender,
                          time=time,
                          content='' if len(item) < 2 else item[1])
        messages.append(message)
    return messages


def filterNontext(messages: List[Message]) -> List[Message]:
    for message in messages:
        if message.content == '[图片]':
            messages.remove(message)

        if message.content == '':
            messages.remove(message)

    return messages
