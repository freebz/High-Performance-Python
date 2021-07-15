# 예제 9-32 공유한 결과를 검증하기 위한 main

print("Verification - extracting unique values from {:,} items\nin the numpy array (this might be slow)...".format(NBR_ITEMS_IN_ARRAY))
# main_nparray.flat은 배열의 내용을 순회한다. 이때 복사본을 만들지 않는다.
counter = Counter(main_nparray.flat)
print("Unique values in main_nparray:")
tbl = PrettyTable(["PID", "Count"])
for pid, count in counter.items():
    tbl.add_row([pid, count])
print(tbl)

total_items_set_in_array = sum(counter.values())

# 배열의 모든 원소가 DEFAULT_VALUE와 다른지 검사한다.
assert DEFAULT_VALUE not in counter.keys()
# 배열의 모든 원소를 샜는지 검사한다.
assert total_items_set_in_array == NBR_ITEMS_IN_ARRAY
# 모든 프로세스가 작업을 했는지를 확인하기 위해서
# 유일한 키가 NBR_OF_PROCESSES 만큼 있는지 살펴본다.
assert len(counter) == NBR_OF_PROCESSES
input("Press a key to exit...")
