function adjustStyle(width) {
  width = parseInt(width);
  if (width < 931) {
    $("#size-stylesheet").attr("href", "/css/mobile.css");
  } else {
    $("#size-stylesheet").attr("href", "/css/style.css"); 
  }
}

$(function() {
  adjustStyle($(this).width());
  $(window).resize(function() {
    adjustStyle($(this).width());
  });
});

$(function() {
  adjustStyle($(this).width());
  $(window).resize(function() {
    adjustStyle($(this).width());
  });
});
