# Vue.js 영화 리뷰 프로젝트

## 개요
이 프로젝트는 Vue.js를 활용하여 영화 정보를 검색하고, 리뷰 동영상을 확인하며, 추천 영화를 조회할 수 있는 웹 애플리케이션입니다. The Movie Database(TMDb) API와 YouTube API를 통합하여 영화 데이터를 가져오고, 유저가 원하는 정보를 직관적으로 탐색할 수 있도록 구현하였습니다.

---

## 주요 기능
1. **최고 평점 영화 조회**:
   - TMDb API를 통해 평점이 높은 영화를 조회.
   - `MovieListView`에서 카드 형식으로 영화 목록을 출력.
   - 각 카드를 클릭하면 상세 페이지로 이동.

2. **영화 상세 정보**:
   - 특정 영화를 클릭하면 TMDb API를 활용해 영화의 상세 정보를 표시.
   - 포스터, 평점, 개봉일, 줄거리 등의 정보를 제공.

3. **영화 리뷰 검색**:
   - 유저가 영화 제목을 입력하면 YouTube API를 활용하여 영화 리뷰 동영상 목록을 제공.
   - 검색된 동영상은 `YouTubeCard` 컴포넌트로 출력.

4. **유튜브 리뷰 모달**:
   - 리뷰 카드 클릭 시 `YoutubeReviewModal`에서 동영상을 바로 재생.

5. **환경 변수 관리**:
   - `.env` 파일을 활용해 API 키를 안전하게 관리.

---

## 기술 스택
- **Frontend**: Vue.js 3, Composition API
- **API**:
  - [TMDb API](https://developers.themoviedb.org/3)
  - [YouTube Data API](https://developers.google.com/youtube/v3)
- **환경 변수 관리**: `.env`

---

## 프로젝트 구조
```plaintext
src/
├── assets/                # 정적 파일
├── components/            # 재사용 가능한 Vue 컴포넌트
│   ├── MovieCard.vue
│   ├── YouTubeCard.vue
│   ├── YoutubeReviewModal.vue
│   └── YoutubeTrailerModal.vue
├── views/                 # 페이지 단위 Vue 컴포넌트
│   ├── HomeView.vue
│   ├── MovieDetailView.vue
│   ├── MovieListView.vue
│   ├── RecommendedView.vue
│   └── ReviewSearchView.vue
├── router/                # Vue Router 설정
│   └── index.js
├── App.vue                # 메인 Vue 컴포넌트
└── main.js                # 앱의 진입점
```
---

## 🎓 학습한 내용 및 느낀 점

1. 🏗️ Vue.js를 활용한 프로젝트 구조화
  - Composition API를 활용해 재사용 가능한 컴포넌트를 설계하고, 유지보수가 용이한 구조를 구성했습니다.
  - props와 emit을 통해 부모-자식 컴포넌트 간 데이터 흐름을 처리하며, Vue의 데이터 전달 방식을 학습했습니다.
  - 컴포넌트를 효과적으로 나누고, 파일 구조를 고민하며 프로젝트의 확장성과 가독성을 고려한 설계를 경험했습니다.

2. 🌐 외부 API 통합
  - TMDb API와 YouTube API를 통합하여 동적으로 데이터를 가져오는 방법을 배웠습니다.
  - Axios를 활용한 비동기 요청 처리와 async/await의 효율적인 사용법, 그리고 에러 핸들링 방식을 학습했습니다.
  - API 응답 데이터를 Vue 컴포넌트로 렌더링하며, 외부 데이터와의 통합 작업을 이해했습니다.

3. 🔐 환경 변수 관리
  - .env 파일을 사용하여 민감한 정보를 안전하게 관리하는 방법을 배웠습니다.
  - Vite 프로젝트에서 import.meta.env를 활용해 환경 변수를 불러오는 방법을 익혔습니다.
  - 환경 변수를 설정함으로써 API 키를 보호하고 프로젝트의 보안성을 강화하는 경험을 했습니다.

4. 🎨 유저 경험 개선
  - YoutubeReviewModal을 활용해 유저가 리뷰 카드를 클릭했을 때 동영상을 바로 재생할 수 있도록 구현하며, 유저 중심의 UI 설계 방식을 배웠습니다.
  - Vue Router를 활용해 페이지 전환을 매끄럽게 처리하며 라우팅 설계와 구현의 중요성을 체감했습니다.
  - 클릭 이벤트와 모달 연동을 통해 유저가 직관적으로 사용할 수 있는 UI를 설계했습니다.

5. 🔧 문제 해결 과정
  - Vue.js에서 script setup와 Options API를 혼용하여 발생한 문제를 해결하며, Composition API의 강점을 이해하고 활용할 수 있었습니다.
  - 파일 구조와 컴포넌트 설계를 고민하며, 재사용성과 유지보수성을 높이는 방법을 익혔습니다.
  - 다양한 오류를 디버깅하며 Vue.js의 에러 메시지와 개발자 도구를 적극적으로 활용해 문제를 해결하는 경험을 쌓았습니다.
