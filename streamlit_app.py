import streamlit as st
import time

st.write("차태현")

with st.spinner("잠시만 기다려 주세요..."):
    time.sleep(5)  # 실제 작업 시뮬레이션

st.success("데이터 로딩 완료!")