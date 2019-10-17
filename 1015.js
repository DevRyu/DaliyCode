//twoSum함수에 숫자배열과 '특정 수'를 인자로 넘기면,
//더해서 '특정 수'가 나오는 index를 배열에 담아 return해 주세요.
const reverse = x => {
    return (
      parseFloat(
        x
          .toString()
          .split('')
          .reverse()
          .join('')
      ) * Math.sign(x)
    )                 
  }
  
  reverse(1234);