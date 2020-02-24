s는 여러 괄호들로 이루어진 String 인자입니다.s가 유효한 표현인지 아닌지 true/false로 반환해주세요
num: 종류는 '(', ')', '[', ']', '{', '}' 으로 총 6개 
return: true/false
예
s = "()[]{}"
return true
예
s = "(]"
return false

function isValid(s) {
  let arr = s.slice();
  for (let i = 0; i < s.length/2; i++){
    for (let j = 0; j < s.length-1; j++){
      let match = arr[j]+arr[j+1];
      if ( (match === "()") || (match === "{}") || (match === "[]")){
        arr= arr.replace(arr[j], "").replace(arr[j+1],"");
      }
    }  
  }
  if (arr === "") {
    return true
  } else {
    return false
  }  
}