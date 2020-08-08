$(".kb").on("click", function () {
    const btn = $(this).attr("data-btn");
    $("#buttonName").text("Button: " + btn);

    $.ajax({
        type: "GET",
        url: "http://localhost:8080/button?btn=" + btn,
        dataType: "json",
        success: function (data) {
            console.log(data);
        }
    });
});