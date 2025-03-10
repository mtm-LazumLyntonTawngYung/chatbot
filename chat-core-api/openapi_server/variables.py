import os

responses = {
    'normal': {
        'GP_MSG_INTRO': '場合、以下のような対応が良い可能性が高いです。<br><br>',
        'BP_MSG_INTRO': '<br>反対に、以下のような対応は上の対応方法に比べてあまり良くないようです。<br><br>',
        'REF_URL_INTRO': '<br>※（）の中はうまくいった確率。<br>詳しくは、こちらをご覧ください。<br>',
        'NO_DATA_MSG_REPLY': '参考になる情報が見つかりませんでした。<br><br> もしかすると、以下のページで参考になるものがあるかもしれませんので、ぜひご覧ください。<br><a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>',  # noqa: E501
    },
    'friend': {
        'GP_MSG_INTRO': '場合、こんな対応をするといいかも！<br><br>',
        'BP_MSG_INTRO': '<br>反対に、こんな対応は上の方法と比べるとあまりよくないかもね。<br>',
        'REF_URL_INTRO': '<br>※（）の中はうまくいった確率。<br>もっと詳しく知りたいなら、これ見てみて！<br>',
        'NO_DATA_MSG_REPLY': '参考になりそうな情報が見つからなかったよ。<br><br> でも、もしかしたら下のページが役に立つかもしれないから、よかったら見てみて！<br><a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>',  # noqa: E501
    },
    'doctor': {
        'GP_MSG_INTRO': '場合、以下のような対応が適切である可能性が高いです。<br><br>',
        'BP_MSG_INTRO': '<br>反対に、以下の対応は先に挙げた方法と比べて、適切ではない場合があります。<br>',
        'REF_URL_INTRO': '<br>※（）の中はうまくいった確率。<br>詳しくは、こちらをご覧ください。<br>',
        'NO_DATA_MSG_REPLY': '参考となる情報が見つかりませんでした。<br><br> ただ、以下のページに有益な情報があるかもしれませんので、よろしければご覧ください。<br><a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>',  # noqa: E501
    },
}
GEMINI_API_ENDPOINT = os.getenv(
    'GEMINI_API_ENDPOINT', 'https://console-gemini-27920194398.asia-northeast1.run.app')

INSTANCE_CONNECTION_NAME = os.getenv(
    'INSTANCE_CONNECTION_NAME', '34.146.211.79')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'g_system01_dev')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'wp')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'chienowa2018727')
port = 8080

CASE_GROUP_THRESHOLD = 0.5
GP_RATE_THRESHOLD = 0.7
BP_RATE_THRESHOLD = 0.3

CHIENOWA_GPBP_SUMMARY_URL = '<a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>'  # noqa: E501

ALL_KEYWORD_TEXT = 'すべて'
