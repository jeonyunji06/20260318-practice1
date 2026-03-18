import streamlit as st

st.set_page_config(page_title="자기소개 페이지", page_icon="👋")

st.title("👋 안녕하세요, 저는 [당신 이름]입니다")
st.write("저에 대해서 간단히 알아보세요. Streamlit으로 만든 자기소개 페이지입니다.")

st.header("📌 기본 정보")
st.markdown("- 이름: 홍길동")
st.markdown("- 직업: 데이터 분석가 / 소프트웨어 개발자")
st.markdown("- 이메일: hong@example.com")
st.markdown("- 위치: 서울, 한국")

st.header("🎯 관심 분야")
st.markdown("1. 머신러닝 & 딥러닝")
st.markdown("2. 데이터 시각화")
st.markdown("3. 웹 애플리케이션 개발")

st.header("💼 주요 기술 스택")
st.markdown("- Python, Pandas, NumPy")
st.markdown("- Streamlit, Flask, FastAPI")
st.markdown("- TensorFlow, PyTorch, scikit-learn")

st.header("📚 학습 및 프로젝트")
st.write("저는 다음과 같은 프로젝트를 진행했습니다:")
st.write("- 고객 이탈 예측 모델 개발")
st.write("- 실시간 대시보드 웹 앱 제작")
st.write("- 자연어 처리 기반 추천 시스템")

st.header("📷 취미 및 관심사")
st.write("사진 촬영, 여행, 등산, 독서")

st.header("✉️ 연락")
st.write("궁금한 점이나 협업 요청은 언제든지 환영합니다.")
st.write("이메일: hong@example.com")

with st.expander("더 알아보기"):
    st.write("저는 기술과 사람을 연결하는 것을 좋아합니다. 오픈소스 기여와 커뮤니티 활동에도 적극적입니다.")
