import pyupbit

access = "5Cu0dx8YSx0xxPG0J51bIb9qAxpl7ctwHtzYukG2"          # 본인 값으로 변경
secret = "jNIU8i9TYxIYe9vGgkdDwFQkxYZnBmIBzAqSeEez"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # 보유 KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

