# Flask Slack Bot: Leave emojis automatically

> leave warming emojis automatically on thread replies 👍🏻

🇰🇷 [한글 README 바로가기](./README_kr.md)

This project provides all the files and code you need to create a Slack Bot based on Flask. This app serves to process events by receiving messages in Slack.

## Prerequisites

- Python 3.8 or higher should be installed.
- You need to create an app that will be linked with your Slack Workspace.
    - These are the Bot Token Scopes need to be granted: `channels:history`, `groups:history`, `reactions:read`, `reactions:write`
- You need the Signing Secret and Bot Token(Bot User OAuth Token) for the Slack app.

## Local Development

### 1. Install required packages

```bash
pip install -r requirements.txt
```

### 2. Set environment variables

```bash
export SIGNING_SECRET=your_signing_secret
export SLACK_TOKEN=your_slack_token
```

### 3. Run the application

```bash
python app.py
```

## Deploy to Heroku

To deploy to Heroku, you need to follow these steps:

### 1. Create a Heroku account and log in

If you do not have a Heroku account, first create one on the [Heroku website](https://www.heroku.com/). After creating an account, you need to log in via the Heroku CLI in your terminal.

```bash
heroku login
```

### 2. Create a Heroku app

```bash
heroku create your-app-name
```

### 3. Set environment variables

Go to the Config Vars section in the Settings tab of the Heroku Dashboard and add the following environment variables:

- `SIGNING_SECRET`: your_signing_secret
- `SLACK_TOKEN`: your_slack_token

### 4. Deploy

```bash
git add .
git commit -m "Ready to deploy"
git push heroku main
```

Now, your Flask-based Slack Bot is deployed to Heroku!

## License

This project is licensed under the MIT License. For more information, see the LICENSE file.