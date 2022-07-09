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
        window.alert("終了");
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

const jsonData= require('./json/info.json'); 
console.log(jsonData);