function checkStringContains(str1, str2) {
  let occurs = 0;
  for (let i = 0; i < str1.length; i++) {
    for (let j = 0; j <= str2.length; j++) {
      if (str1[i] === str2[j]) {
        occurs++;
        break;
      }
    }
  }
  return occurs === str2.length;
}

const result = checkStringContains('python', 'ono');
console.log(result);