# 예제 5-5 모두 함께 연결하기

data = read_data(data_filename)
data_day = day_grouper(data)
anomalous_dates = filter(None, map(check_anomaly, data_day))

first_anomalous_date, first_anomalous_data = anomalous_dates.next()
print("The first anomalous date is: ", first_anomalous_date)
