import datetime

# 用於存儲帳本的字典
account_book = []

# 顯示當前餘額
def show_balance():
    balance = sum(item['amount'] for item in account_book)
    print(f"目前餘額: {balance} 元")

# 添加收入或支出
def add_record():
    date = input("請輸入日期 (YYYY-MM-DD): ")
    try:
        # 檢查日期格式
        date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        print("日期格式錯誤！請重新輸入。")
        return
    
    description = input("請輸入記錄描述: ")
    amount = float(input("請輸入金額 (收入請輸入正數，支出請輸入負數): "))
    
    # 創建一條記錄
    record = {
        'date': date,
        'description': description,
        'amount': amount
    }
    
    # 添加到帳本中
    account_book.append(record)
    print(f"記錄已成功添加：{record['description']}，金額：{record['amount']} 元")

# 顯示所有記錄
def show_records():
    if not account_book:
        print("目前沒有任何記錄。")
        return
    
    print("所有記錄：")
    for record in account_book:
        print(f"日期: {record['date']} | 描述: {record['description']} | 金額: {record['amount']} 元")

# 主選單
def main():
    while True:
        print("\n記帳系統")
        print("1. 顯示目前餘額")
        print("2. 添加收入或支出")
        print("3. 顯示所有記錄")
        print("4. 退出")
        
        choice = input("請選擇操作 (1/2/3/4): ")
        
        if choice == '1':
            show_balance()
        elif choice == '2':
            add_record()
        elif choice == '3':
            show_records()
        elif choice == '4':
            print("退出程式")
            break
        else:
            print("無效的選擇，請重新選擇。")

# 程式進入點
if __name__ == "__main__":
    main()