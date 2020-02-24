//String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.
const getLengthOfStr = str => {
    let firstBox = [];
    let secondBox = []
    for (let i = 0; i < str.length; i++) {
      let index = str.slice(i, i+1);
      for (let j = 0; j < firstBox.length; j++) {
        if (index === firstBox[j]) {
          if (secondBox.length < firstBox.length) {
            secondBox = firstBox.slice();
          }
          firstBox = firstBox.splice(j+1, firstBox.length);
          break;
        }
      }
      firstBox.push(index);
    }
    return Math.max(firstBox.length, secondBox.length);
  }

  getLengthOfStr("abcabcabc");