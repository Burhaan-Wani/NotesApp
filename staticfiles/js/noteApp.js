$(".button").click(function () {
  var buttonId = $(this).attr("id");
  $("#modal-container").removeAttr("class").addClass(buttonId);
  $("body").addClass("modal-active");
});

// $("#modal-container").click(function () {
//   $(this).addClass("");
//   $("body").removeClass("modal-active");
// });

$("#closeBtn").click(function () {
  $("#modal-container").addClass("out");
  $("body").removeClass("modal-active");
});

$(".plus-btn").click(function () {
  var buttonId2 = $(this).attr("id");
  $("#modal-container").removeAttr("class").addClass(buttonId2);
  $("body").addClass("modal-active");
});
