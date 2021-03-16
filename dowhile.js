//var cond = false;

//while(cond){
    //console.log("이 구문은 실행되지 않습니다.");
//}

//do{
 //   var ans = parseInt(prompt("1+1 = ?"));
//}while(ans !=2);
//console.log("맞혔습니다!");

var a = Math.ceil(Math.random()*10);
var b = Math.ceil(Math.random()*10);

var solution = a*b;

do{
    var ans;
    ans = parseInt(prompt(a+"*"+b+"=?"));
}while(ans != solution);
console.log("맞았습니다.");
