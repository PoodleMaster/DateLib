from dateLib import exec_s0_to_s1

# 処理開始期間（日本日時）
termS0_str = "2023-12-01"       # 開始日
termS1_str = "2023-12-31"       # 終了日

termS0_str = "2024-01-01"       # 開始日
termS1_str = "2024-01-31"       # 終了日

# 処理開始
def main():
    exec_s0_to_s1(termS0_str, termS1_str)

if __name__ == '__main__':
    main()
