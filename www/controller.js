$(document).ready(function () {
    // Expose function to Python
    eel.expose(DisplayMessage);

    function DisplayMessage(message) {
        // Check if the element exists before updating
        const siriMessage = $(".siri-message");
        if (siriMessage.length > 0) {
            siriMessage.find("li:first").text(message); // Update the first list item's text
            siriMessage.textillate('start'); // Start the animation
        } else {
            console.error("Element '.siri-message' not found!");
        }
    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
});
