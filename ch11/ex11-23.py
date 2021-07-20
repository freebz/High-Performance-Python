# 예제 11-23 countmemaybe의 KMinValues 구현

from countmemaybe import KMinValues
kmv1 = KMinValues(k=1024)
kmv2 = KMinValues(k=1024)
for i in range(0, 50000):
    kmv1.add(str(i))
    ...:
for i in range(25000, 75000):
    kmv2.add(str(i))
    ...:
print(len(kmv1))
# 50416
print(len(kmv2))
# 52439
print(kmv1.cadinality_intersection(kmv2))
# 25900.2862992
print(kmv1.cardinality_union(kmv2))
# 75346.2874158
