const quiz = [
    {
    question: "エンジニア何年目ですか？",
    answers:[
        '1年目',
        '2年目',
        '3年目',
        '4年目'
    ],
    result:'3年目'
},{
    question: "一番好きな業務・工程はなんですか？",
    answers:[
        'コーディング',
        '設計',
        '要件',
        '運用'
    ],
    result:'コーディング'
},{
    question: "開発言語で好きなものはどれですか？",
    answers:[
        'Python',
        'TypeScript',
        'PHP',
        'Ruby'
    ],
    result:'Python'
},{
    question: "現在学習している開発言語は何ですか？",
    answers:[
        'Python',
        'TypeScript',
        'Go',
        'Scala'
    ],
    result:'TypeScript'
},{
    question: "あなたのなりたいエンジニアは？",
    answers:[
        'フルスタックエンジニア',
        'サーバーサイドエンジニア',
        'フロントエンドエンジニア',
        'インフラエンジニア'
    ],
    result:'フルスタックエンジニア'
},{
    question: "エンジニアの学習方法で一番大事なことは何？",
    answers:[
        '調査力',
        '自走力',
        '折衝力',
        '技術力'
    ],
    result:'調査力'
},{
    question: "FTCが目指していることは何？",
    answers:[
        '人間的成長',
        '技術的成長',
        '',
        ''
    ],
    result:'人間的成長'
},{
    question: "FTC3年目を迎えてどんな想いでここまで来ましたか？",
    answers:[
        '自力でシステム開発ができるようになること',
        '上流工程のスペシャリストとなること',
        'プログラミングスキルを向上をすること',
        'システム開発の知見を習得すること'
    ],
    result:'自力でシステム開発ができるようになること'
}
]

const quizlength = quiz.length;
let quizIndex = 0;

const $button = document.getElementsByTagName('button');
let buttonLength = $button.length;

const setQuiz = () => {
    document.getElementById('question').textContent = quiz[quizIndex].question;
    let buttonIndex = 0;
    while(buttonIndex < buttonLength){
        $button[buttonIndex].textContent = quiz[quizIndex].answers[buttonIndex];
        buttonIndex ++;
    };
}
setQuiz();

const clickHandler = (e) => {
    if(quiz[quizIndex].result === e.target.textContent){
        window.alert('正解！');
    }else{
        window.alert('不正解');
    }
    quizIndex ++;

    if(quizIndex < quizlength){
        setQuiz();
    }else{
        window.alert("あなたは高野須　悠人さんのことをマスターしました！おめでとうございます！");
    }
}

const handleIndex = () => {
    let handleIndex = 0;
    while(handleIndex < buttonLength){
        $button[handleIndex].addEventListener('click', (e) =>{
            clickHandler(e);
        });
        handleIndex ++;
    };
}
handleIndex();