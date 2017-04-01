

$(document).ready(function($) {
    $(".row-click-able").click(function() {
        // window.document.location = $(this).data("href");
        console.log($(this).data("href"));
    });
});
