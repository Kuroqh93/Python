import requests
response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
f = open("parser.txt","a")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                print(parse_elem_2)
                f.write(f"{parse_elem_2}\n")
f.close()