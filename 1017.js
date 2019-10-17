//숫자인 num을 인자로 넘겨주면, 뒤집은 모양이 num과 똑같은지 여부를 반환해주세요.
//num: 숫자
//return: true or false (뒤집은 모양이 num와 똑같은지 여부)
const sameReverse = num => {
    let a = num.toString();
    let b = a.length;
    let c = 0;
    let arr = [];
    let reverseArr = [];
    for(let i = 0; i<a.length; i++){
      arr[i] = a.slice(i,i+1);
    }
    for(let j = b; j>=1;j--){
      reverseArr[c] = a.slice(j-1,j);
      c++
    }
    for(let k=0; k<a.length; k++){
      if(arr[k]!==reverseArr[k]){
        return false;
      }
    return true;
    }
    
  }
  
  sameReverse(1234);