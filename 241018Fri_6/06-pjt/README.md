# 프로젝트 참여 후기✨

## 유지인 - Accounts 앱 담당👩‍💻

깃을 배우는 과정에서 침착함의 중요성을 깨달았으며,
깃을 되돌리기위한 reset무새 행동을 멈춰야 합니다.
협업을 위한 git 공부를 더 해야 할 것 같습니다.📚

또한 accounts에서 기본적인 로그인, 로그아웃 복습 및
profile에서 팔로우, 본인이 쓴 글, 댓글, 팔로우한 사람들을 보여주는
로직을 작성하고 기본적으로 html을 이뿌게 꾸몄습니다.🎨

깃만 생각하면 눈물이 앞을 가리지만 견디겠습니다 😢💪

---

## 강혜경 - Board 앱 담당👩‍💻


깃 브랜치 배울때 팀장님이 브랜치 리세마라 하셔서, 제가 팀장자리 갈취하여 진행하였습니다.🎉

로그인 후 댓글 작성 가능하도록 수정하였고,
본인 게시글 및 댓글을 수정/삭제 하도록 작업했습니다.

작업을 다하고 git 머지할때 떨렸지만 다행히 안터지고 문제없이 해결되어서 짜릿했습니다.🙌✨
아직 배울게 많아서 기쁩니다.😊

---


(※참고: 게임을 플레이하는 도중에 원하는 결과가 나오지 않았을 경우, 처음부터 다시 시작하거나 세이브해 둔 파일을 로드하여 원하는 결과가 나올 때까지 계속 리셋하는 일종의 어뷰징 행위. 일본어로 리셋 마라톤, 줄여서 리세마라(リセマラ)라고 부른다)


---

# 도파민아저씨와 포항피바다의 합작 프로젝트

## 1. 프로젝트 생성
- **레포지토리 만들기**: `git_flow_practice` (README 포함, 프리마켓으로 생성)
- **클론 받기**: 레포지토리 클론

## 2. 멤버 초대
- 팀원 및 강사님 초대

## 3. 개발 환경 설정
1. **VS 코드 열기**
2. `.gitignore` 파일 생성 (https://www.toptal.com/developers/gitignore 참조)
3. 가상 환경 생성 및 활성화
   ```bash
   py -m venv venv
   source venv/Scripts/activate  # Windows 경우
   # 또는
   source venv/bin/activate       # Mac/Linux 경우

## 4. 필수 패키지 설치
pip freeze > requirements.txt

## 5. 브랜치 생성 및 전환
git branch dev
git switch dev

## 6. 변경사항 확인 및 커밋
git status
git add .
git commit -m "기본 환경 설정 문서"
git log --oneline

4. Django 앱 생성 및 설정
프로젝트 및 앱 생성
django-admin startproject pjt .
python manage.py startapp articles
앱 등록: pjt/settings.py 파일에서 INSTALLED_APPS에 articles 추가
모델 등록 및 마이그레이션
python manage.py makemigrations
python manage.py migrate
Django Extensions 추가: INSTALLED_APPS에 'django_extensions' 추가
Django 쉘 사용
python manage.py shell_plus
article = Article(title='test')
article.save()
exit()
데이터 덤프 및 fixtures 설정
python manage.py dumpdata --indent=4 articles > articles.json
mkdir articles/fixtures
mv articles.json articles/fixtures/
변경사항 커밋 및 푸시
git add .
git commit -m "초기 데이터 추가"
git push -u origin dev
팀원 작업 흐름
레포지토리 클론

git pull origin dev로 최신 코드 가져오기
가상 환경 설정 및 패키지 설치
python -m venv venv
pip install -r requirements.txt
새로운 브랜치 생성

git branch accounts 후 git switch accounts로 이동
앱 생성 및 설정
python manage.py startapp accounts
INSTALLED_APPS에 accounts 추가
AUTH_USER_MODEL 설정
슈퍼유저 생성 및 데이터 덤프

python manage.py createsuperuser
python manage.py dumpdata --indent=4 accounts > users.json
mkdir accounts/fixtures
mv users.json accounts/fixtures/
변경사항 커밋 및 푸시

git add .
git commit -m "accounts 모델 추가"
git push origin accounts
머지 리퀘스트 생성: 프로젝트 레포지토리에서 accounts 브랜치를 dev로 머지

추가 설정 및 작업
설정 브랜치 생성

git branch settings
git switch settings
BASE_DIR / 'templates' 추가 후 저장
변경사항 커밋 및 푸시
git add .
git commit -m "settings 수정"
git push origin settings
다른 브랜치와의 통합

git pull origin accounts
아티클 브랜치 작업

git branch articles
git switch articles
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata users.json
아티클 생성 및 데이터 덤프

python manage.py shell_plus
user = User.objects.get(pk=1)
article = Article(user=user, title='test')
article.save()
exit()
python manage.py dumpdata --indent=4 articles > articles.json
최종 커밋 및 푸시

git add .
git commit -m "user article 1:N 관계 추가"
git push origin articles
