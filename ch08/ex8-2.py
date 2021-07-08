# 예제 8-2 콜백 예제

from functools import partial

def save_value(value, callback):
    print("Saving {} to database".format(value))
    save_result_to_db(result, callback)

def print_response(db_response):
    print("Response from database: {}".format(db_response))

if __name__ == "__main__":
    eventloop.put(
        partial(save_value, "Hello World", print_response)
    )
