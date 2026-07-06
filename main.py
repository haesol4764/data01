import streamlit as st

st.title("🗺️ 나만의 여행 계획기")

# 1. 도시 vs 자연 드롭다운
choice = st.selectbox(
    "1. 당신이 선호하는 여행 스타일은 무엇인가요?",
    ("선택하세요", "도시 (City)", "자연 (Nature)")
)

# 2. 여행 기간 범위 슬라이더 (0일 ~ 100일)
duration = st.slider(
    "2. 원하는 여행 기간을 선택하세요 (일 단위)",
    min_value=0,
    max_value=100,
    value=(7, 14),
    step=1
)

st.write(
    f"현재 선택하신 기간: **{duration[0]}일**부터 **{duration[1]}일**까지 "
    f"(총 {duration[1] - duration[0]}일 일정)"
)

# 3. 선호 음식 다중 선택 (체크박스 스타일의 멀티셀렉트)
food_choices = st.multiselect(
    "3. 선호하는 음식 종류를 모두 골라주세요 (중복 선택 가능)",
    ["한식", "중식", "일식", "양식", "기타"],
    default=["한식"] # 기본값으로 '한식'이 먼저 체크되어 있도록 설정
)


# --- 결과 출력 화면 ---
if choice != "선택하세요":
    st.markdown("---")
    st.subheader("📋 당신의 여행 조건 요약")
    
    st.write(f"- **스타일:** {choice}")
    
    total_days = duration[1] - duration[0]
    st.write(f"- **기간:** 총 {total_days}일 일정")
    
    # 음식 선택 결과 출력
    if food_choices:
        # 사용자가 고른 음식들을 쉼표(,)로 연결해서 이쁘게 보여줍니다.
        foods_str = ", ".join(food_choices)
        st.write(f"- **선호 음식:** {foods_str}")
    else:
        st.write("- **선호 음식:** 선택한 음식이 없습니다. (금강산도 식후경인걸요! 😋)")
