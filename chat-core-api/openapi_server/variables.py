import os

responses = {
    'normal': "薬を定期的に服用することは重要です。毎日のリマインダーを設定すると役立つかもしれません。",
    'friend': "大丈夫です、忘れた時は一緒にリマインダーをセットしようね。",
    'doctor': "薬を飲み忘れると健康に影響を及ぼす可能性があります。リマインダーを使って忘れないようにしましょう。"
}
GEMINI_API_ENDPOINT = os.getenv(
    'GEMINI_API_ENDPOINT', 'https://console-gemini-27920194398.asia-northeast1.run.app')

INSTANCE_CONNECTION_NAME = os.getenv(
    'INSTANCE_CONNECTION_NAME', '34.146.211.79')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'g_system01_dev')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'wp')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'chienowa2018727')
