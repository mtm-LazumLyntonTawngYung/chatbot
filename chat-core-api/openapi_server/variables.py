import os

responses = {
    'normal': "薬を定期的に服用することは重要です。毎日のリマインダーを設定すると役立つかもしれません。",
    'friend': "大丈夫です、忘れた時は一緒にリマインダーをセットしようね。",
    'doctor': "薬を飲み忘れると健康に影響を及ぼす可能性があります。リマインダーを使って忘れないようにしましょう。"
}
DATABASE_NAME = os.getenv('DATABASE_NAME', 'g_system01_dev')
DATABASE_USERNAME = os.getenv('DATATBASE_USERNAME', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'root')
INSTANCE_CONNECTION_NAME = os.getenv('INSTANCE_CONNECTION_NAME', 'localhost')
