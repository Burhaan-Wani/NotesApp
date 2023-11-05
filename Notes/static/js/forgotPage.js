$(".previous1").on("click", function () {
  $(".fieldset5").removeClass("d-block");
  $(".fieldset5").addClass("d-none");
  $(".fieldset4").removeClass("d-none");
  $(".fieldset4").addClass("d-block");
  $(".progress-bar").css("width", "25%");
  $("#personal").removeClass("active");
});

$(".previous2").on("click", function () {
  $(".fieldset6").removeClass("d-block");
  $(".fieldset6").addClass("d-none");
  $(".fieldset5").removeClass("d-none");
  $(".fieldset5").addClass("d-block");
  $(".progress-bar").css("width", "50%");
  $("#payment").removeClass("active");
});
