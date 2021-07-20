# 예제 11-18 HAT 트라이를 사용해 데이터 저장하기

import hat_trie
...
    words_trie = hat_trie.Trie()
    for word in text_example.readers:
        words_trie[word] = 0
