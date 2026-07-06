import streamlit as st
from datetime import time
import pandas as pd
import numpy as np

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
total_days = duration[1] - duration[0]

# 3. 선호 음식 선택 (체크박스 가로 배치)
st.subheader("3. 선호 음식 (중복 가능)")
col1, col2, col3, col4, col5 = st.columns(5)
with col1: korean = st.checkbox("한식", value=True)
with col2: chinese = st.checkbox("중식")
with col3: japanese = st.checkbox("일식")
with col4: western = st.checkbox("양식")
with col5: etc = st.checkbox("기타")

# 4. 활동 시간 범위 슬라이더
st.subheader("4. 선호 활동 시간대")
active_time = st.slider(
    "주로 언제 활동하는 것을 좋아하시나요?",
    min_value=time(0, 0),
    max_value=time(23, 30),
    value=(time(9, 0), time(21, 0)),
    format="HH:mm"
)

# --- 결과 요약 및 5. 라인 차트 출력 ---
if env_choice != "선택하세요":
    st.markdown("---")
    st.header("✨ 당신의 여행 취향 요약")
    
    # 요약 정보 출력
    st.write(f"📍 **선호 환경:** {env_choice}")
    st.write(f"📅 **여행 기간:** {duration[0]}일 ~ {duration[1]}일 (약 {total_days}일간)")
    
    selected_foods = []
    if korean: selected_foods.append("한식")
    if chinese: selected_foods.append("중식")
    if japanese: selected_foods.append("일식")
    if western: selected_foods.append("양식")
    if etc: selected_foods.append("기타")
    st.write(f"🍴 **음식 취향:** {', '.join(selected_foods) if selected_foods else '선택 안 함'}")
    
    start_t = active_time[0].strftime("%H:%M")
    end_t = active_time[1].strftime("%H:%M")
    st.write(f"⏰ **활동 시간:** {start_t}부터 {end_t}까지")

    # 5. 라인 차트: 여행 일자별 예상 체력/에너지 시뮬레이션
    st.markdown("---")
    st.subheader("📈 나의 여행 일자별 예상 에너지 추이")
    st.caption("선택하신 여행 기간과 활동 시간을 바탕으로 분석한 일자별 체력 변화 그래프입니다.")
    
    if total_days > 0:
        # 가상의 데이터 생성 (여행 일수에 따른 에너지 변화)
        days = [f"{i}일차" for i in range(1, total_days + 1)]
        
        # 활동 시간 길이에 따른 피로도 가중치 계산
        active_hours = active_time[1].hour - active_time[0].hour
        fatigue_flavor = 0.8 if active_hours > 12 else 1.0
        
        # U자형 곡선 모양으로 에너지 데이터 시뮬레이션
        x = np.linspace(0, np.pi, total_days)
        energy = 80 - 30 * np.sin(x) * fatigue_flavor + np.random.randint(-5, 5, total_days)
        energy = np.clip(energy, 10, 100) # 10~100 사이로 제한
        
        # 판다스 데이터프레임으로 변환
        chart_data = pd.DataFrame({
            "에너지 레벨 (%)": energy
        }, index=days)
        
        # 스트림릿 라인 차트 그리기
        st.line_chart(chart_data)
        
        st.info("💡 **팁:** 여행 중반부에 에너지가 가장 낮아지니, 이때는 퐁당퐁당 쉬어가는 일정을 짜보세요!")
    else:
        st.warning("여행 기간이 0일이라 그래프를 표시할 수 없습니다. 슬라이더의 범위를 넓혀주세요!")
