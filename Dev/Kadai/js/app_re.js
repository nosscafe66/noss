var quiz = [
    {
        question: "エンジニア何年目ですか？",
        answers: [
            '1年目',
            '2年目',
            '3年目',
            '4年目'
        ],
        result: '3年目'
    }, {
        question: "一番好きな業務・工程はなんですか？",
        answers: [
            'コーディング',
            '設計',
            '要件',
            '運用'
        ],
        result: 'コーディング'
    }, {
        question: "開発言語で好きなものはどれですか？",
        answers: [
            'Python',
            'TypeScript',
            'PHP',
            'Ruby'
        ],
        result: 'Python'
    }, {
        question: "現在学習している開発言語は何ですか？",
        answers: [
            'Python',
            'TypeScript',
            'Go',
            'Scala'
        ],
        result: 'TypeScript'
    }, {
        question: "あなたのなりたいエンジニアは？",
        answers: [
            'フルスタックエンジニア',
            'サーバーサイドエンジニア',
            'フロントエンドエンジニア',
            'インフラエンジニア'
        ],
        result: 'フルスタックエンジニア'
    }, {
        question: "エンジニアの学習方法で一番大事なことは何？",
        answers: [
            '調査力',
            '自走力',
            '折衝力',
            '技術力'
        ],
        result: '調査力'
    }, {
        question: "FTCが目指していることは何？",
        answers: [
            '人間的成長',
            '技術的成長',
            '',
            ''
        ],
        result: '人間的成長'
    }, {
        question: "FTC3年目を迎えてどんな想いでここまで来ましたか？",
        answers: [
            '自力でシステム開発ができるようになること',
            '上流工程のスペシャリストとなること',
            'プログラミングスキルを向上をすること',
            'システム開発の知見を習得すること'
        ],
        result: '自力でシステム開発ができるようになること'
    }, {
        question: "FTCのスキルのうち最も重要なスキルはどれですか？",
        answers: [
            'テクニカルスキル',
            'コアスキル',
            'プログラミングスキル',
            'マネジメントスキル'
        ],
        result: 'コアスキル'
    }, {
        question: "FTCの会社理念として一つ目に正しいものはどれですか？",
        answers: [
            'こどもたちに誇れる会社',
            'こどもたちに認められる会社',
            'こどもたちへ還元できる会社',
            'こどもたちから認知される会社'
        ],
        result: 'こどもたちに誇れる会社'
    }, {
        question: "FTCの会社理念として二つ目に正しいものはどれですか？",
        answers: [
            'テクノロジーで時代を越える会社',
            'テクノロジーを巧みに扱う会社',
            'テクノロジーで時代をつなげる会社',
            'テクノロジーを後世に残す会社'
        ],
        result: 'テクノロジーで時代をつなげる会社'
    }, {
        question: "FTCの事業領域として正しいものはどれですか？",
        answers: [
            'Itコンシェルジュサービス',
            'Itコンサルティングサービス',
            'Itマネジメントサービス',
            'Itアドバイザーサービス'
        ],
        result: 'Itコンシェルジュサービス'
    }, {
        question: "FTCのホーム画面に書かれている英語の言葉は何？",
        answers: [
            'make the tomorrow',
            'make to the future',
            'make the future',
            'make the business'
        ],
        result: 'make the future'
    }, {
        question: "FTCの自社サービスLoMeはどんなコンセプトか？",
        answers: [
            '中小企業向け労務管理システム',
            '中小企業向け勤怠管理システム',
            '中小企業向け給与管理システム',
            '中小企業向け勤労管理システム'
        ],
        result: '中小企業向け労務管理システム'
    }, {
        question: "FTCの今期の会社方針は何か？",
        answers: [
            '在り方を考える',
            '中小企業向け勤怠管理システム',
            '中小企業向け給与管理システム',
            '中小企業向け勤労管理システム'
        ],
        result: '中小企業向け労務管理システム'
    }
];
var quizlength = quiz.length;
var quizIndex = 0;
var $button = document.getElementsByTagName('button');
var buttonLength = $button.length;
var setQuiz = function () {
    document.getElementById('question').textContent = quiz[quizIndex].question;
    var buttonIndex = 0;
    while (buttonIndex < buttonLength) {
        $button[buttonIndex].textContent = quiz[quizIndex].answers[buttonIndex];
        buttonIndex++;
    }
    ;
};
setQuiz();
var clickHandler = function (e) {
    if (quiz[quizIndex].result === e.target.textContent) {
        window.alert('正解！');
    }
    else {
        window.alert('不正解');
    }
    quizIndex++;
    if (quizIndex < quizlength) {
        setQuiz();
    }
    else {
        window.alert("高野須悠人の略歴を終わります。これでFTCマスターですね！！");
        window.alert("継続的に学習していればアプリの仕組みを理解できるし作れるようになります！！");
    }
};
var handleIndex = function () {
    var handleIndex = 0;
    while (handleIndex < buttonLength) {
        $button[handleIndex].addEventListener('click', function (e) {
            clickHandler(e);
        });
        handleIndex++;
    }
    ;
};
handleIndex();
