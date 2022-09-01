  $(document).ready(function() {
  $(".nav-toggler").each(function(_, navToggler) {
      const target = $(navToggler).data("target");
      $(navToggler).on("click", function() {
      $(target).animate({
        height: "toggle"
      });
    });
  });
});