(async function () {

var a;
var b;
var c;
var run;
var d;

async function go() {
  while (!(run == 0)) {
    if (run == 0) {
      stop2();
    } else {
      a.on();
      b.off();
    }
    await delay(1);
    if (run == 0) {
      stop2();
    } else {
      a.off();
      b.on();
    }
    await delay(1);
  }
}

function stop2() {
  a.off();
  b.off();
  c.off();
  d.off();
}


boardReady({device: ''}, async function (board) {
  board.systemReset();
  board.samplingInterval = 250;
  a = getLed(board, 6);
  b = getLed(board, 7);
  c = getLed(board, 8);
  d = getLed(board, 9);
  run = 0;
  document.onkeydown = async function(e){
    console.log(e.keyCode);
    if(e.keyCode == 65){
        run = 1;
      go();
    }
    if(e.keyCode == 66){
        run = 0;
      stop2();
    }
  };
});

}());