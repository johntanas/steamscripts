def parse_price(price: str):
    pattern = '\D?(\d*)(,*)?(\d+)(\.)(\d+)'
    tokens = re.search(pattern, price, re.UNICODE)
    decimal_str = tokens.group(1)+tokens.group(3)+"."+tokens.group(5)
