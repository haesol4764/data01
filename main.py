import streamlit as st
from datetime import time

st.title("🗺️ 나만의 여행 취향 분석기")

# 1. 도시 vs 자연 드롭다운
st.subheader("1. 선호 환경")
env_choice = st.selectbox(
    "어느 곳으로 떠나고 싶나요?",
    ("선택하세요", "도시 (City)", "자연 (Nature)")
)

# 2. 여행 기간 범위 슬라이더
st.subheader("2. 여행 기간")
duration = st.slider(
    "여행 기간 범위를 선택하세요 (일 단위)",
    min_value=0,
    max_value=100,
    value=(7, 14)
)

# 3. 선호 음식 선택 (체크박스 가로 배치)
st.subheader("3. 선호 음식 (중복 가능)")
col1, col2, col3, col4, col5 = st.columns(5)
with col1: korean = st.checkbox("한식", value=True)
with col2: chinese = st.checkbox("중식")
with col3: japanese = st.checkbox("일식")
with col4: western = st.checkbox("양식")
with col5: etc = st.checkbox("기타")

# 4. 활동 시간 범위 슬라이더 (추가된 기능)
st.subheader("4. 선호 활동 시간대")
active_time = st.slider(
    "주로 언제 활동하는 것을 좋아하시나요?",
    min_value=time(0, 0), # 00:00
    max_value=time(23, 30), # 23:30
    value=(time(9, 0), time(21, 0)), # 초기값 09:00 ~ 21:00
    format="HH:mm" # 시간 형식 설정
)

# --- 결과 요약 출력 ---
if env_choice != "선택하세요":
    st.markdown("---")
    st.header("✨ 당신의 여행 취향 요약")
    
    # 1. 환경
    st.write(f"📍 **선호 환경:** {env_choice}")
    
    # 2. 기간
    total_days = duration[1] - duration[0]
    st.write(f"📅 **여행 기간:** {duration[0]}일 ~ {duration[1]}일 (약 {total_days}일간)")
    
    # 3. 음식
    selected_foods = []
    if korean: selected_foods.append("한식")
    if chinese: selected_foods.append("중식")
    if japanese: selected_foods.append("일식")
    if western: selected_foods.append("양식")
    if etc: selected_foods.append("기타")
    st.write(f"🍴 **음식 취향:** {', '.join(selected_foods) if selected_foods else '선택 안 함'}")
    
    # 4. 시간 (시간 포맷팅해서 출력)
    start_t = active_time[0].strftime("%H:%M")
    end_t = active_time[1].strftime("%H:%M")
    st.write(f"⏰ **활동 시간:** {start_t}부터 {end_t}까지 활동하는 것을 선호함")

    # 활동 시간에 따른 짧은 코멘트
    if active_time[0] < time(7, 0):
        st.caption("💡 부지런한 얼리버드 스타일이시네요!")
    elif active_time[1] > time(22, 0):
        st.caption("💡 밤의 정취를 즐기는 올빼미 스타일이시네요!")
