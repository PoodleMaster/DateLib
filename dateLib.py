from datetime import datetime, timedelta

# 「YYYY-MM-DDTHH:MM:SS」をdatetime obj形式に変換
def str_to_datetime(date_str):
    time_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    return time_obj

# 「YYYY-MM-DDTHH:MM:SS」の開始日と終了日をdatetime obj形式に変換して比較
def chk_term(date_start_str, date_end_str):
    if(str_to_datetime(date_start_str) <= str_to_datetime(date_end_str)):
        # 開始日≦終了日の場合
        return True
    else:
        # 開始日＞終了日の場合
        return False

# 日本時間の「YYYY-MM-DDTHH:MM:SS」をUTCに変換
def date_jap_to_utc(date_jap_str):
    time_jap = datetime.strptime(date_jap_str, "%Y-%m-%dT%H:%M:%S")
    time_utc_offset = timedelta(hours=9)  # 日本時間はUTC+9
    time_utc = time_jap - time_utc_offset
    date_utc_str = time_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    return date_utc_str

# UTCの「YYYY-MM-DDTHH:MM:SSZ」を日本時間に変換
def utc_to_date_jap(utc_str):
    time_utc = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
    time_utc_offset = timedelta(hours=9)  # 日本時間はUTC+9
    time_jap = time_utc + time_utc_offset
    date_jap_str = time_jap.strftime("%Y-%m-%dT%H:%M:%S")
    return date_jap_str

# 「YYYY-MM-DDTHH:MM:SS」の日付を1日インクリメント
def incre_day(date_str):
    time_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    time_inc_date = time_obj + timedelta(days=1)
    date_inc_str = time_inc_date.strftime("%Y-%m-%dT%H:%M:%S")
    return date_inc_str

# 「YYYY-MM-DDTHH:MM:SS」の時刻を「YYYY-MM-DDT23:59:59」に変換
def end_of_day(date_str):
    time_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    time_end_of_day_obj = datetime(time_obj.year, time_obj.month, time_obj.day, 23, 59, 59)
    data_end_of_day_str = time_end_of_day_obj.strftime("%Y-%m-%dT%H:%M:%S")
    return data_end_of_day_str

# 「termS0_str」～「termS1_str」までループ
def exec_s0_to_s1(termS0_str, termS1_str):
    dayS0_jap_str = termS0_str + "T00:00:00"
    dayE0_jap_str = end_of_day(termS1_str + "T00:00:00")
    print(f"Term : {dayS0_jap_str} - {dayE0_jap_str}")

    while chk_term(dayS0_jap_str, dayE0_jap_str):
        dayS1_jap_str = end_of_day(dayS0_jap_str)
        dayS0_utc_str = date_jap_to_utc(dayS0_jap_str)
        dayS1_utc_str = date_jap_to_utc(dayS1_jap_str)

        # 「dayS0_utc_str」～「dayS1_utc_str」でAPIコール
        print(f"API : JapTime: {dayS0_jap_str} - {dayS1_jap_str}, UtcTime: {dayS0_utc_str} - {dayS1_utc_str}")

        dayS0_jap_str = incre_day(dayS0_jap_str)

