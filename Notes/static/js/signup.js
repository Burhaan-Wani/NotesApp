$(".previous").on("click", function () {
    $(".fieldset2").addClass("d-none");
    $(".fieldset1").removeClass("d-none");
    $(".progress-bar").css("width", "33%");
    $("#personal").removeClass("active");
});
