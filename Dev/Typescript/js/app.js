const question = "住んでいるところはどれですか？";
const answers = ['神奈川県','茨城県','東京都','京都'];
const result = '神奈川県';
const $button = document.getElementsByTagName('button');

const setQuiz = () => {
    document.getElementById('question').textContent = question;
    let buttonIndex = 0;
    let buttonLength = $button.length;
    while(buttonIndex < buttonLength){
        $button[buttonIndex].textContent = answers[buttonIndex];
        buttonIndex ++;
    };
}
setQuiz();

const clickHandler = (e) => {
    if(result === e.target.textContent){
        window.alert('正解！');
    }else{
        window.alert('不正解');
    }
}

$button[0].addEventListener('click', (e) =>{
    clickHandler(e);
});
$button[1].addEventListener('click', (e) =>{
    clickHandler(e);
});
$button[2].addEventListener('click', (e) =>{
    clickHandler(e);
});
$button[3].addEventListener('click', (e) =>{
    clickHandler(e);
});