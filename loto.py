import streamlit as st
import random
import time

# 1. 페이지 기본 설정
st.set_page_config(page_title="행운의 로또 번호 생성기", page_icon="🎰", layout="centered")

# 2. 커스텀 CSS (제목 디자인 등)
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 900;
        color: #FF4B4B;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #666;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# 3. 화면 상단 제목
st.markdown('<div class="main-title">🎰 행운의 로또 번호 생성기 🍀</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">당신의 인생 역전을 응원합니다! (최대 5게임)</div>', unsafe_allow_html=True)

# 4. 세션 상태 초기화
if 'lotto_history' not in st.session_state:
    st.session_state.lotto_history = []


# 로또 공 색상 설정
def get_ball_color(number):
    if number <= 10:
        return "#fbc400"  # 노란색
    elif number <= 20:
        return "#69c8f2"  # 파란색
    elif number <= 30:
        return "#ff7272"  # 빨간색
    elif number <= 40:
        return "#aaaaaa"  # 회색
    else:
        return "#b0d840"  # 초록색


# 5. 버튼 영역 (2단 구성)
col1, col2 = st.columns([3, 1])

with col1:
    generate_btn = st.button("🌟 로또 번호 생성하기", use_container_width=True)
with col2:
    reset_btn = st.button("🔄 초기화", use_container_width=True)

# 초기화 버튼 동작
if reset_btn:
    st.session_state.lotto_history = []
    st.rerun()  # 화면 새로고침

# 생성 버튼 동작
if generate_btn:
    # 약간의 로딩 효과 (시각적 재미)
    with st.spinner("행운의 숫자를 뽑는 중..."):
        time.sleep(0.5)

    new_numbers = sorted(random.sample(range(1, 46), 6))
    st.session_state.lotto_history.append(new_numbers)

    # 5개가 넘으면 가장 옛날 것 삭제
    if len(st.session_state.lotto_history) > 5:
        st.session_state.lotto_history.pop(0)

    # 5세트가 꽉 차면 대박 기원 풍선 애니메이션
    if len(st.session_state.lotto_history) == 5:
        st.balloons()

# 6. 결과 출력 영역
st.markdown("<hr style='border: 1px dashed #ccc; margin: 20px 0;'>", unsafe_allow_html=True)

if st.session_state.lotto_history:
    for numbers in st.session_state.lotto_history:
        # 배경이 있는 예쁜 카드 디자인 및 가운데 정렬
        html_content = "<div style='background-color: #f8f9fa; padding: 15px; border-radius: 15px; margin-bottom: 15px; display: flex; justify-content: center; align-items: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>"

        for num in numbers:
            base_color = get_ball_color(num)

            # 입체감을 위한 그라데이션 (3D 공 효과)
            gradient = f"radial-gradient(circle at 30% 30%, white 0%, {base_color} 50%, rgba(0,0,0,0.3) 100%)"

            # 공 모양 CSS 디자인
            ball_style = f"""
                width: 50px; height: 50px; 
                border-radius: 50%; 
                background: {gradient}; 
                color: white; 
                display: flex; 
                justify-content: center; 
                align-items: center; 
                font-size: 22px; 
                font-weight: 900; 
                margin: 0 8px; 
                box-shadow: 3px 4px 6px rgba(0,0,0,0.3); 
                text-shadow: 1px 1px 2px rgba(0,0,0,0.6);
            """
            # 줄바꿈 공백 방지를 위해 스타일을 한 줄로 변환 후 적용
            ball_style = ball_style.replace('\n', '')

            html_content += f"<div style='{ball_style}'>{num}</div>"

        html_content += "</div>"

        # HTML 렌더링
        st.markdown(html_content, unsafe_allow_html=True)
else:
    # 안내 문구 디자인
    st.markdown(
        "<div style='text-align: center; color: #888; font-size: 18px; padding: 30px;'>버튼을 눌러 행운의 숫자를 확인해 보세요! 💸</div>",
        unsafe_allow_html=True)