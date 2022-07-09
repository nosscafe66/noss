function getItem(){
    let Item1;
    document.getElementById("text1").textContent = "コーディング試験対策";
    Item1 = document.getElementById("text1").textContent;
    console.log(Item1)
    for(let i = 0; i < 10; i++){
        document.getElementById("text1").textContent = "コーディング試験対策" + i;
        console.log(Item1 + " " + i)
        if(i == 5){
            return i;
        }
    }
}

const testend = (num) =>{
    let Item2;
    document.getElementById("text1").textContent = "コーディング試験対策完了" + num;
    Item2 = document.getElementById("text1").textContent;
    console.log(Item2);
}

const setjson = () =>{
    const jsonobj = {
        info1:'',
        info2:'',
        info3:''
    }
    console.log(jsonobj);
}

function main(){
    let count;
    count = getItem()
    testend()
    setjson(count)
}main()