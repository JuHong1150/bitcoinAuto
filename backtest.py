
import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume)로 당일시가, 고가, 저가, 종가, 거래량 에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count = 14)

# 변동폭 * k  계산, (고가 - 저가) * k 값
df['range'] = (df['high'] - df['low']) * 0.5

#target(매수가), range 컬럼을 한칸씩 미틍로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

fee = 0.01  # 수수료(살때, 팔때 각각 0.005 그냥 대충 0.01로 잡아뒀음)

# ror(수익률), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")