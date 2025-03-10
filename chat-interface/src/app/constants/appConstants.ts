export const appConstants = {
    TIME_OUT_SETTING: 500,
    BOT_STYLE: [
      {label: '普通', value: 'normal'},
      {label: '友達', value: 'friend'},
      {label: '医者', value: 'doctor'}
    ],
    DEFAULT_MSG: "当社のウェブサイトへようこそ。近日中にご連絡させていただきます。",
    CHAT_MSG:{
      normal: {
        greetingMsg: 'こんにちは。認知症の方に起きたことを教えていただければ、どのような対応方法が好ましいか、過去の統計情報からお答えできます。<br><br> 起きたことの例<br> ・薬を飲むことを忘れてしまう <br>・さっき話したことを、何度も繰り返す<br>',
        questionMsg: 'どんなことが起こりましたか？',
        nextQAMsg: '他にはどんなことが起こりましたか？',
        defaultMsg: '参考になる情報が見つかりませんでした。<br><br> もしかすると、以下のページで参考になるものがあるかもしれませんので、ぜひご覧ください。<br><a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>'
    },
    friend: {
        greetingMsg: 'こんにちは！認知症の方に何かあったとき、どう対応するのがいいか、過去の統計データをもとにアドバイスできるよ。よかったら教えてね！<br><br>例えば、<br>・薬を飲むことを忘れてしまう<br>・さっき話したことを、何度も繰り返す<br>',
        questionMsg: '何があったの？',
        nextQAMsg: '他にはどんなことがあった？',
        defaultMsg: '参考になりそうな情報が見つからなかったよ。<br><br> でも、もしかしたら下のページが役に立つかもしれないから、よかったら見てみて！<br><a href=https://chienowa-net.com/gpbpsummary target=_blank>https://chienowa-net.com/gpbpsummary</a>'
    },
      doctor: {
        greetingMsg:'こんにちは。認知症の方の状況を教えていただければ、どのような対応が望ましいか過去の統計に基づいてお答えいたします。 ※開発中のため、何が起こったかを答える一問一答形式のみとなります。',
        questionMsg: 'どうしたの？',
        nextQAMsg: '他に何が起こったのでしょうか？',
        defaultMsg: '薬を飲み忘れる場合、以下のような対応が良い可能性が高いです。<br><br> <ol><li>服薬時に声掛けする。</li> <li>薬を本人に手渡しできる体制を作る。</li> <li>薬を手渡しできる体制を作り、さらに服用後にノートに記載する。</li></ol> <br><br> 反対に、以下のような対応は上の対応方法に比べてあまり良くないようです。 <br><br> <ol><li>薬を日付の書いた箱にセットする。</li> <li>カレンダー（薬カレンダー含む）を利用する。</li></ol> <br> <br> 詳しくは、こちらをご覧ください。<br> <a href="https://chienowa-net.com/gpbpsummary?cat=careinfo-forget">https://chienowa-net.com/gpbpsummary?cat=careinfo-forget</a>'
      }
    }
  };