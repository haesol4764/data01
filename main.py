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

# --- 결과 요약 및 5. 맞춤형 라인 차트 출력 ---
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

    # 5. 라인 차트: 선택 조건에 따른 "여행 일자별 기대도/만족도 변화 트렌드"
    st.markdown("---")
    st.subheader("📈 나의 여행 패턴별 '기대감 & 만족도' 곡선")
    st.caption("선택하신 환경(도시/자연)과 활동 시간에 따른 심리적 변화를 나타낸 라인 차트입니다.")
    
    if total_days > 0:
        # X축 데이터 (1일차, 2일차...)
        days = [f"{i}일차" for i in range(1, total_days + 1)]
        
        # 1) 환경(도시 vs 자연)에 따른 기본 감정 곡선 기본값 생성
        x = np.linspace(0, 3, total_days)
        if env_choice == "도시 (City)":
            # 도시는 초반에 화려함에 흥분(피크)했다가 중간에 지치고 마지막에 쇼핑으로 회복하는 경향
            base_curve = 70 + 20 * np.sin(x*2) 
            chart_label = "도시 탐방 만족도"
        else:
            # 자연은 초반에는 적응하느라 완만하다가 갈수록 힐링되어 만족도가 우상향하는 경향
            base_curve = 50 + 40 * (1 - np.exp(-x))
            chart_label = "자연 힐링 만족도"
            
        # 2) 활동 시간 길이에 따른 피로도(감점 요소) 반영
        active_hours = active_time[1].hour - active_time[0].hour
        if active_hours > 13: # 활동 시간이 너무 길면 후반부 만족도 급감
            base_curve[-int(total_days/3):] -= 15 
            
        # 3) 노이즈 추가 및 데이터 정리
        satisfaction = base_curve + np.random.randint(-3, 4, total_days)
        satisfaction = np.clip(satisfaction, 0, 100) # 0~100 제한
        
        # 판다스 데이터프레임 생성
        chart_data = pd.DataFrame({
            chart_label: satisfaction
        }, index=days)
        
        # 스트림릿 라인 차트 실행
        st.line_chart(chart_data)
        
        # 차트 결과에 따른 맞춤형 위트 코멘트
        if env_choice == "도시 (City)" and active_hours > 13:
            st.warning("🚨 **주의:** 빡빡한 도시 일정으로 3일차 이후 '현타(여행 권태기)'가 올 수 있으니 늦잠을 허용하세요!")
        elif env_choice == "자연 (Nature)":
            st.success("🌲 **분석:** 시간이 지날수록 일상의 스트레스가 풀리며 만족도가 극대화되는 '진정한 힐러' 타입이십니다.")
        else:
            st.info("💡 **분석:** 전형적으로 알차고 균형 잡힌 감정 흐름을 보여주는 안정적인 여행가이시군요!")
            
    else:
        st.warning("여행 기간을 1일 이상으로 선택해야 그래프가 표시됩니다.")
