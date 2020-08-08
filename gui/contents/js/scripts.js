const keyboard = $(".kb");

function retrieveData(kb) {
    $(".kb").removeClass("selected");
    kb.addClass("selected");

    const btn = kb.attr("data-btn");
    $("#buttonName").text("Button: " + btn);

    $.ajax({
        type: "GET",
        url: "http://localhost:8080/button?btn=" + btn,
        dataType: "json",
        success: function (data) {
            const info = $("#buttonInfo");
            info.empty();

            if (data == null) {
                info.append("<h4>This button does nothing</h4>");
            } else {
                info.append("<h4>Type: " + data.type + "</h4>");

                switch (data.type) {
                    case "keyboard":
                        let keys = "";
                        for (let i = 0; i < data.action.keys.length; i++) {
                            keys += data.action.keys[i].key.replace("_", " ");
                            if (i < data.action.keys.length - 1) keys += " <small>+</small> ";
                        }


                        info.append("<h4>Keys: " + keys + "</h4>");
                        break
                    case "command":
                        info.append("<h4>Command: " + data.action.command + "</h4>");
                        break
                    case "macro":
                        info.append("<h4>Macro: " + data.action.macro + "</h4>");
                        break
                    case "program":
                        info.append("<h4>Program: " + data.action.path + "</h4>");
                        break
                    case "internal":
                        info.append("<h4>Internal: " + data.action.command + "</h4>");
                        break
                }
            }
        }
    });
}

keyboard.on("click", function () {
    retrieveData($(this));
});

keyboard.on('contextmenu', async function (event) {
    retrieveData($(this))
    const menu = $("#kbContextMenu");
    if (menu.hasClass("active")) {
        menu.removeClass("active");
        await sleep(50);
    }
    menu.css("top", event.pageY);
    menu.css("left", event.pageX);
    menu.addClass("active");
});

$("body").on('click', function () {
    $("#kbContextMenu").removeClass("active");
});

$(document).on('click', function () {
    $('.collapse').collapse('hide');
});

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}