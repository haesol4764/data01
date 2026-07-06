import streamlit as st

st.title("🗺️ 나만의 여행 계획기")

# 1. 도시 vs 자연 드롭다운
choice = st.selectbox(
    "당신이 선호하는 여행 스타일은 무엇인가요?",
    ("선택하세요", "도시 (City)", "자연 (Nature)")
)

# 2. 여행 기간 범위 슬라이더 (0일 ~ 100일)
duration = st.slider(
    "원하는 여행 기간을 선택하세요 (일 단위)",
    min_value=0,
    max_value=100,
    value=(7, 14), # 기본 선택 범위
    step=1
)

st.write(
    f"현재 선택하신 기간: **{duration[0]}일**부터 **{duration[1]}일**까지 "
    f"(총 {duration[1] - duration[0]}박 {duration[1] - duration[0] + 1}일 일정)"
)

# 선택 결과에 따른 조건문 (구분선은 st.markdown("---")으로 처리해야 합니다)
if choice != "선택하세요":
    st.markdown("---") # 파이썬 코드 안에서 구분선을 넣을 때는 이렇게 해야 합니다!
    st.subheader("📋 당신의 여행 조건 요약")
    
    st.write(f"- **스타일:** {choice}")
    
    total_days = duration[1] - duration[0]
    if total_days <= 5:
        st.write(f"- **일정 분석:** {total_days}일 이하의 짧고 굵은 {choice} 여행이군요! 알찬 루트를 추천합니다.")
    elif total_days >= 30:
        st.write(f"- **일정 분석:** {total_days}일 이상의 한 달 살기 스타일! {choice}에서 여유롭게 머무는 코스를 추천합니다.")
        import streamlit as st

st.subheader("3. 선호 음식 선택")

# 가로로 5개의 칸(Column)을 나눕니다.
col1, col2, col3, col4, col5 = st.columns(5)

# 각 칸에 체크박스를 하나씩 배치합니다.
with col1:
    korean = st.checkbox("한식", value=True) # value=True는 기본 체크 상태
with col2:
    chinese = st.checkbox("중식")
with col3:
    japanese = st.checkbox("일식")
with col4:
    western = st.checkbox("양식")
with col5:
    etc = st.checkbox("기타")

# 사용자가 어떤 체크박스를 선택했는지 리스트로 모으기
selected_foods = []
if korean: selected_foods.append("한식")
if chinese: selected_foods.append("중식")
if japanese: selected_foods.append("일식")
if western: selected_foods.append("양식")
if etc: selected_foods.append("기타")

# 선택 결과 출력 확인용 코드
st.write(f"선택된 음식 카테고리: {selected_foods}")
    else:
        st.write(f"- **일정 분석:** {total_days}일 동안 떠나는 균형 잡힌 {choice} 여행이군요!")
