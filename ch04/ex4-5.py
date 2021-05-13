# 예제 4-5 커스텀 해시 함수

class City(str):
    def __hash__(self):
        return ord(self[0])

# 임의의 값을 가지는 도시 이름으로 사전을 생성한다.
data = {
    City("Rome"): 4,
    City("San Francisco"): 3,
    City("New York"): 5,
    City("Barcelona"): 2,
}
