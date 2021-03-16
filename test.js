var a = prompt('알고싶은 연도를입력하세요.');

console.log(isLeapYear(a));

function isLeapYear(year){
    if(year%4==0){
      return true;
    }
    else{
      return false;
    }
  }