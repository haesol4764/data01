import streamlit as st

st.title("🗺️ 나만의 여행 계획기")

# 1. 도시 vs 자연 드롭다운 (이전 단계)
choice = st.selectbox(
    "당신이 선호하는 여행 스타일은 무엇인가요?",
    ("선택하세요", "도시 (City)", "자연 (Nature)")
)

# 2. 여행 기간 범위 슬라이더 (0일 ~ 100일)
# value에 (시작값, 종료값)을 넣으면 '범위 선택' 슬라이더가 됩니다.
duration = st.slider(
    "원하는 여행 기간을 선택하세요 (일 단위)",
    min_value=0,
    max_value=100,
    value=(7, 14), # 앱이 처음 켜졌을 때 기본으로 선택되어 있을 범위
    step=1
)

st.write(
    f"현재 선택하신 기간: **{duration[0]}일**부터 **{duration[1]}일**까지 "
    f"(총 {duration[1] - duration[0]}박 {duration[1] - duration[0] + 1}일 일정)"
)

---

# 💡 선택 결과에 따른 조건문 예시
if choice != "선택하세요":
    st.markdown("---")
    st.subheader("📋 당신의 여행 조건 요약")
    
    # 드롭다운 결과 출력
    st.write(f"- **스타일:** {choice}")
    
    # 슬라이더 결과에 따른 맞춤 메시지 분기 예시
    total_days = duration[1] - duration[0]
    if total_days <= 5:
        st.write(f"- **일정 분석:** {total_days}일 이하의 짧고 굵은 {choice} 여행이군요! 알찬 루트를 추천합니다.")
    elif total_days >= 30:
        st.write(f"- **일정 분석:** {total_days}일 이상의 한 달 살기 스타일! {choice}에서 여유롭게 머무는 코스를 추천합니다.")
    else:
        st.write(f"- **일정 분석:** {total_days}일 동안 떠나는 균형 잡힌 {choice} 여행이군요!")
