# 檔名：app.py
# 這是一個「期貨損益計算機」網站，全部用 Python 寫成

import streamlit as st   # 引入 Streamlit 工具

st.title("📈 我的期貨損益計算機")   # 網頁大標題

# 下面這幾行會自動變成網頁上的「輸入框」和「滑桿」
進場 = st.number_input("進場點數", value=18000)
出場 = st.number_input("出場點數", value=18120)
口數 = st.number_input("口數", value=1, step=1)
每點價值 = st.selectbox("每點價值（元）", [50, 200])   # 50=小台, 200=大台

# 這就是你第 4 章學的函式！
def 計算損益(進場, 出場, 口數, 每點價值):
    return (出場 - 進場) * 口數 * 每點價值

損益 = 計算損益(進場, 出場, 口數, 每點價值)

# 把結果顯示在網頁上
st.metric("這筆交易損益", f"{損益:+,.0f} 元")

if 損益 > 0:
    st.success("這是一筆獲利交易 🎉")
elif 損益 < 0:
    st.error("這是一筆虧損交易，檢討一下進出場 🧐")
else:
    st.info("不賺不賠（不計手續費）")