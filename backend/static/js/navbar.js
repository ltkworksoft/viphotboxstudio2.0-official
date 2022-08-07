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

let dropper = document.getElementsByClassName("dropper-btn");
let i;

for (i = 0; i < dropper.length; i++) {
    dropper[i].addEventListener("click", function () {
        this.classList.toggle("active");
        let dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}