$(document).ready(function () {
    // Text animation
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: "bounceIn" },
        out: { effect: "bounceOut" },
    });

    // SiriWave configuration
    const siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: window.innerWidth > 800 ? 800 : window.innerWidth - 20, // Responsive width
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.3,
        autostart: true,
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: "fadeInUp", sync: true },
        out: { effect: "fadeOutUp", sync: true },
    });

    // Microphone button events
    $("#MicBtn").on("click", function () {
        eel.playAssistantsound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommand()()
    });
});
