# 예제 11-17 이중 배열 트라이를 사용해 데이터 저장하기

import datrie
...
    chars = set()
    for word in text_example.readers:
        chars.update(word)
    trie = datrie.BaseTrie(chars)
...
    # chars를 만들면서 제네레이터를 이미 소비했으므로,
    # 새로운 제네레이터를 만들 필요가 있디ㅏ.
    readers = text_example.read_words(text_example.SUMMARIZED_FILE) # 새로운 제네레이터
    for word in readers:
        trie[word] = 0
