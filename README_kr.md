# Flask Slack Bot: Leave emojis automatically

이 프로젝트는 Flask 기반의 Slack Bot을 만드는 데 필요한 모든 파일과 코드를 제공합니다. 이 앱은 Slack에서 메시지를 받아 이벤트를 처리하는 역할을 합니다.

## Prerequisites

- Python 3.8 이상이 설치되어 있어야 합니다.
- Slack Workspace와 연동할 앱을 생성해야 합니다.
    - 앱 생성시 필요한 권한은 다음 네가지: `channels:history`, `groups:history`, `reactions:read`, `reactions:write`
- Slack 앱에 대한 Signing Secret과 Bot Token(Bot User OAuth Token)이 필요합니다.

## Local Development

### 1. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

### 2. 환경변수 설정

```bash
export SIGNING_SECRET=your_signing_secret
export SLACK_TOKEN=your_slack_token
```

### 3. 애플리케이션 실행

```bash
python app.py
```

## Deploy to Heroku

Heroku에 배포하기 위해서는 다음의 절차가 필요합니다.

### 1. Heroku 계정 생성 및 로그인

Heroku에 계정이 없다면, 먼저 [Heroku 사이트](https://www.heroku.com/)에서 계정을 생성하세요. 계정을 생성한 후에는 터미널에서 Heroku CLI를 사용하여 로그인해야 합니다.

```bash
heroku login
```

### 2. Heroku 앱 생성

```bash
heroku create your-app-name
```

### 3. 환경변수 설정

Heroku Dashboard의 Settings 탭에서 Config Vars 섹션에 들어가서 다음의 환경변수를 추가합니다.

- `SIGNING_SECRET`: your_signing_secret
- `SLACK_TOKEN`: your_slack_token

### 4. 배포

```bash
git add .
git commit -m "Ready to deploy"
git push heroku main
```

이제 Flask 기반의 Slack Bot이 Heroku에 배포되었습니다! 

## License

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.