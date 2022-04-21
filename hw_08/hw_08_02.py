import re


def parse_log(log):
    remote_addr = re.search(r'(.+) - -', log).group(1)
    request_datetime = re.search(r'\[(.*?)\]', log).group(1)
    request_type = re.search(r'GET|POST|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH', log).group()
    request_resource = re.search(r' ((/\w+)+)', log).group(1)
    response_code = re.search(r' (\d{3}) ', log).group(1)
    response_size = re.search(r' (\d{3}) (\d+) "', log).group(2)
    return remote_addr, request_datetime, request_type, request_resource, response_code, response_size


def show_logs_data():
    with open('nginx_logs.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            print(parse_log(line))


show_logs_data()
