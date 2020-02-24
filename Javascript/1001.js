function sliceCityFromAddress(address) {
  var a = address.indexOf("시");
  var b = address.indexOf("도"); // 숫자값이 저장된다.
  if (a){
    if ( !== -1){
      return address.slice(0,b+2) + address.slice(a+2, address.length)
    }
    return address.slice(1,address.length)
  }
}

  let sumAmount=0;
  let sumReview=0;
  let sumLike=0;
  let i;
  for (i=0; i < salesArr.length; i++){
    sumAmount += salesArr[i][1];
    sumReview += reviewArr[i][1];
    sumLike += likeArr[i][1];
  }

// 파이썬과의 차이
// 선언과 초기화 둘다해야지 숫자로 인식
// 선언만 할시에 자료형을 인식못해서
// Not a null로리턴
