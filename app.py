import os
from slack_sdk import WebClient
from slack_sdk.signature import SignatureVerifier
from flask import Flask, request, jsonify, make_response

slack_token = os.environ.get("SLACK_TOKEN")
signing_secret = os.environ.get("SIGNING_SECRET")

slack_client = WebClient(token=slack_token)
signature_verifier = SignatureVerifier(signing_secret=signing_secret)

app = Flask(__name__)

@app.route('/slack/events', methods=['POST'])
def slack_event():
    payload = request.get_json()
    if payload['type'] == 'url_verification':
        return jsonify({'challenge': payload['challenge']})
    
    if not signature_verifier.is_valid_request(request.get_data(), request.headers):
        return make_response("invalid request", 403)

    event = payload.get('event', {})

    # 본 코드는 앱을 채널에 초대할 경우 모든 채널에서 작동하도록 작성됨.
    # 특정 채널에서만 작동을 원한다면 다음 코드에서 채널 ID만 넣어주면 됨: if event.get('type') == 'message' and 'thread_ts' in event and event.get('channel') == '채널ID':
    if event.get('type') == 'message' and 'thread_ts' in event:
        channel_id = event['channel']
        thread_ts = event['thread_ts']
        
        if event.get('subtype') == 'message_replied':
            # N차 답글
            slack_client.reactions_add(name='thumbsup', channel=channel_id, timestamp=event['message']['ts'])
        else:
            # 신규 스레드 및 1차 답글
            response = slack_client.conversations_replies(channel=channel_id, ts=thread_ts)
            if response['ok']:
                for message in response['messages']:
                    if 'thread_ts' in message and message['thread_ts'] == thread_ts and message['ts'] != thread_ts:
                        reaction_response = slack_client.reactions_get(channel=channel_id, timestamp=message['ts'])
                        if reaction_response['ok']:
                            if 'reactions' not in reaction_response['message']:
                                slack_client.reactions_add(name='thumbsup', channel=channel_id, timestamp=message['ts'])

    return make_response("", 200)

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 3000)))