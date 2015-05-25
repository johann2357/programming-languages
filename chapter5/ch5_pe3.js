function subprogram1() {
  var svar1 = 0;
  svar1++;
  function subprogram2() {
    var svar2 = 0;
    svar1++;
    svar2++;
    function subprogram3() {
      var svar3 = 0;
      svar1++;
      svar2++;
      svar3++;
      console.log(svar1);
      console.log(svar2);
      console.log(svar3);
    }
    subprogram3();
  }
  subprogram2();
}
