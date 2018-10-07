import json


def convert_to_json_string_1(data):
    return json.dumps([{'compnay': i[0], 'date': i[1], 'price': i[2]} for i in data], indent=4)
    
def convert_to_json_string_2(data):
    return json.dumps({'data': [{'compnay': i[0], 'date': i[1], 'price': i[2]} for i in data]}, indent=4)


if __name__ == "__main__":
    data = [['00700', '2017-01', '46'], ['baba', '2017-01', '47'], ['tesla', '2017-01', '48']];
    print convert_to_json_string_1(data)
    print convert_to_json_string_2(data)