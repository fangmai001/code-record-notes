function fun() {
  setTimeout(() => {
    console.log("hey");
  }, 1000);
}
fun.call();
