import re
ipv4_regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
alert = "Remember an ipv4 direction format is\n [0-255].[0-255].[0-255].[0-255]"
print(alert)
def ipv4_evaluator():
    ip = input("Insert an ipv4 direction to evaluate it: ")
    if re.fullmatch(ipv4_regex, ip):
        print(f'The ipv4 direction "{ip}" is approved')
    else:
        print(f'The ipv4 direction "{ip}" is denied. Please try again!')

ipv4_evaluator()