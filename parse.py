import re

input_file = 'target.txt'
output_file = 'listeip.txt'

ip_regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d+\s+'

ip_list = []

with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        match = re.match(ip_regex, line)
        if match:
            ip = match.group(1)
            ip_list.append(ip)

with open(output_file, 'w') as file:
    file.write('\n'.join(ip_list))

print(f'IP addresses extracted from {input_file} and saved to {output_file}.')
