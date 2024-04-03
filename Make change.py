price, input_money= map(int, input().split())

coin_500 = 500      # 동전
coin_100 = 100
coin_50 = 50
coin_10 = 10


if input_money >= price:       
    operated_money = input_money - price    
        
    count_coin_500 = operated_money // 500      # 500원 동전 갯수 할당
    operated_money = operated_money % 500       # 거스름돈에서 500원 갯수만큼 금액 제외
        
    count_coin_100 = operated_money // 100      # 100원 동전 갯수 할당
    operated_money = operated_money % 100       # 거스름돈에서 100원 갯수만큼 금액 제외
        
    count_coin_50 = operated_money // 50        # 100원 동전 갯수 할당 
    operated_money = operated_money % 50        # 거스름돈에서 50원 갯수만큼 금액 제외
        
    count_coin_10 = operated_money // 10        # 100원 동전 갯수 할당 
    operated_money = operated_money % 10        # 거스름돈에서 10원 갯수만큼 금액 제외
    
    
    if operated_money % 10 != 0:      # 동전으로 거스름돈 못주면 -1 반환
        print(-1)
    else :
        print(1, count_coin_500, count_coin_100, count_coin_50, count_coin_10)
    
else:
    print(-1)     # 동전으로 거스름돈 못주면 -1 반환