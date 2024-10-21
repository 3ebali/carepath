import streamlit as st

# 응급처치 데이터베이스
first_aid_data = {
    "심장마비": {
        "단계": [
            "환자를 편안한 곳에 눕힌다.",
            "즉시 119에 전화하여 응급 도움을 요청한다.",
            "심폐소생술을 시작한다. (30번 가슴 압박 후 2번 인공호흡)",
            "도움이 올 때까지 계속 심폐소생술을 실시한다."
        ],
        "설명": "심장마비는 즉각적인 응급처치가 필요합니다.",
        "건강 관리 팁": "정기적인 건강 검진과 심혈관 건강을 위한 운동을 하세요.",
        "리뷰": []
    },
    "출혈": {
        "단계": [
            "상처를 깨끗한 천으로 압박한다.",
            "출혈이 멈추지 않으면 더 높은 위치에서 압박한다.",
            "즉시 의사의 진료를 받도록 한다."
        ],
        "설명": "출혈이 심할 경우, 즉각적으로 조치해야 합니다.",
        "건강 관리 팁": "상처 관리와 감염 예방을 위해 적절한 위생을 유지하세요.",
        "리뷰": []
    },
    "화상": {
        "단계": [
            "화상 부위를 흐르는 찬물에 10분 이상 식힌다.",
            "흉터 방지를 위해 화상 부위에 얼음이나 기름을 바르지 않도록 한다.",
            "상처를 깨끗한 천으로 덮고 의사에게 보인다."
        ],
        "설명": "화상은 치료가 필요하며, 적절하게 처치해야 합니다.",
        "건강 관리 팁": "화상 예방을 위해 주의 깊게 작업하고, 필요한 경우 방열 장비를 사용하세요.",
        "리뷰": []
    },
    "경련": {
        "단계": [
            "환자를 안전한 장소로 이동시킨다.",
            "환자의 머리를 보호하고, 물건을 입에 넣지 않도록 한다.",
            "경련이 끝난 후, 환자를 안정시키고 의사에게 보낸다."
        ],
        "설명": "경련 발생 시 안전이 최우선입니다.",
        "건강 관리 팁": "스트레스를 관리하고 충분한 수면을 취하세요.",
        "리뷰": []
    },
    "알레르기 반응": {
        "단계": [
            "환자를 편안하게 앉힌다.",
            "의사가 처방한 에피네프린 자동 주입기를 사용한다.",
            "119에 전화하여 즉각적인 도움을 요청한다."
        ],
        "설명": "알레르기 반응은 생명을 위협할 수 있으므로 신속한 조치가 필수입니다.",
        "건강 관리 팁": "식사 전에 알레르기 유발 식품을 피하고, 응급 약품을 항상 지참하세요.",
        "리뷰": []
    },
    # 추가된 증상들
    "급성 호흡 곤란": {
        "단계": [
            "환자를 편안하게 앉힌다.",
            "숨쉬기 어렵다면 119에 즉시 전화한다.",
            "환자가 편안한 자세를 취할 수 있도록 한다."
        ],
        "설명": "급성 호흡 곤란은 즉각적인 의학적 도움이 필요합니다.",
        "건강 관리 팁": "천식 등의 기저 질환이 있는 경우 정기적인 검진을 하세요.",
        "리뷰": []
    },
    "기절": {
        "단계": [
            "환자를 눕힌다.",
            "환자의 다리를 높인다.",
            "환자가 의식이 돌아올 때까지 기다린다."
        ],
        "설명": "기절은 여러 원인으로 발생할 수 있으며, 주의가 필요합니다.",
        "건강 관리 팁": "식사와 수분 섭취를 충분히 하세요.",
        "리뷰": []
    },
    "복통": {
        "단계": [
            "환자를 편안하게 눕힌다.",
            "통증의 위치와 정도를 확인한다.",
            "심한 통증일 경우 즉시 의료기관을 방문한다."
        ],
        "설명": "복통은 다양한 원인으로 발생할 수 있습니다.",
        "건강 관리 팁": "균형 잡힌 식사와 정기적인 운동을 권장합니다.",
        "리뷰": []
    },
    "타박상": {
        "단계": [
            "상처 부위를 차갑게 유지한다.",
            "손상을 최소화하기 위해 붕대를 감는다.",
            "통증이 지속될 경우 의료기관을 방문한다."
        ],
        "설명": "타박상은 즉각적인 처치가 필요한 경우가 많습니다.",
        "건강 관리 팁": "안전한 환경에서 활동하세요.",
        "리뷰": []
    },
    "구토": {
        "단계": [
            "환자를 편안하게 눕힌다.",
            "입안을 깨끗하게 헹구게 한다.",
            "지속적인 구토가 발생할 경우 의료기관을 방문한다."
        ],
        "설명": "구토는 여러 원인으로 발생하며, 관찰이 필요합니다.",
        "건강 관리 팁": "소량씩 자주 먹는 것이 좋습니다.",
        "리뷰": []
    },
    # 기립성 저혈압 추가
    "기립성 저혈압": {
        "단계": [
            "환자를 편안한 곳에 앉히거나 눕힌다.",
            "천천히 자세를 일으키도록 한다.",
            "상황이 나아지지 않으면 즉시 의료기관에 연락한다."
        ],
        "설명": "기립성 저혈압은 갑작스럽게 일어날 때 혈압이 떨어지는 상태입니다.",
        "건강 관리 팁": "수분 섭취를 충분히 하고, 기립성 저혈압이 있는 경우 천천히 움직이세요.",
        "리뷰": []
    }
}

# Streamlit UI
st.title("응급처치 안내")

# 비상 연락처를 입력받는 필드
emergency_contact = st.text_input("비상연락처 입력 (이름 및 전화번호):")

# 비상 연락처 저장하기
if st.button('비상 연락처 저장'):
    if emergency_contact:
        st.session_state.emergency_contact = emergency_contact
        st.success("비상 연락처가 저장되었습니다.")
    else:
        st.error("비상 연락처를 입력해 주세요.")

# 저장된 비상 연락처 표시하기
if 'emergency_contact' in st.session_state:
    st.write(f"저장된 비상 연락처: {st.session_state.emergency_contact}")

# 즐겨찾기 상태 관리
if 'favorites' not in st.session_state:
    st.session_state.favorites = []

# 사용자로부터 증상 입력 받기
symptom = st.text_input("증상 입력:")

if symptom:
    first_aid_info = first_aid_data.get(symptom, None)
    if first_aid_info:
        st.subheader(f"증상: {symptom}")
        st.write(first_aid_info["설명"])
        st.subheader("처치 단계:")
        for step in first_aid_info["단계"]:
            st.write(f"- {step}")
        st.subheader("건강 관리 팁:")
        st.write(first_aid_info["건강 관리 팁"])

        # 리뷰 입력란
        user_review = st.text_area("이 응급처치에 대한 경험이나 피드백을 작성해 주세요:")
        if st.button("리뷰 남기기"):
            if user_review:
                first_aid_data[symptom]["리뷰"].append(user_review)
                st.success("리뷰가 남겨졌습니다.")
            else:
                st.error("내용을 입력해 주세요.")

        # 저장된 리뷰 표시
        if first_aid_data[symptom]["리뷰"]:
            st.subheader("사용자 리뷰:")
            for review in first_aid_data[symptom]["리뷰"]:
                st.write(f"- {review}")

        # 즐겨찾기 추가 버튼
        if st.button(f"{symptom} 즐겨찾기 추가"):
            if symptom not in st.session_state.favorites:
                st.session_state.favorites.append(symptom)
                st.success(f"{symptom}가 즐겨찾기에 추가되었습니다.")
            else:
                st.warning("이미 즐겨찾기에 추가되었습니다.")
    else:
        st.write("해당 증상에 대한 정보가 없습니다.")

# 즐겨찾기 표시하기
st.subheader("즐겨찾기 목록:")
for favorite in st.session_state.favorites:
    st.write(f"- {favorite}")

# 즐겨찾기 정보 표시
if st.session_state.favorites:
    for favorite in st.session_state.favorites:
        info = first_aid_data[favorite]
        st.write(f"### {favorite}")
        st.write(info["설명"])
        st.subheader("처치 단계:")
        for step in info["단계"]:
            st.write(f"- {step}")
        st.subheader("건강 관리 팁:")
        st.write(info["건강 관리 팁"])

        # 즐겨찾기 리뷰 표시
        if info["리뷰"]:
            st.subheader("사용자 리뷰:")
            for review in info["리뷰"]:
                st.write(f"- {review}")