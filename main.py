import streamlit as st

# 웹앱 제목 설정
st.title("🌲 나의 취향 분석기 🏙️")

# 1. 도시 vs 자연 드롭다운 생성
choice = st.selectbox(
    "당신의 선호하는 여행 스타일은 무엇인가요?",
    ("선택하세요", "도시 (City)", "자연 (Nature)")
)

# 사용자의 선택에 따른 반응형 조건문
if choice == "도시 (City)":
    st.subheader("🏙️ 화려한 조명과 활기가 넘치는 도시를 좋아하시군요!")
    st.write("맛집 탐방, 쇼핑, 그리고 멋진 야경을 즐기는 여행을 추천합니다.")
    
elif choice == "자연 (Nature)":
    st.subheader("🌲 고요하고 평화로운 자연을 좋아하시군요!")
    st.write("캠핑, 등산, 그리고 조용한 숲속에서의 힐링 여행을 추천합니다.")
    
else:
    st.info("위 드롭다운에서 원하는 항목을 선택해 주세요!")
