// Example function for validating form input (not used in this specific case)
function validateForm() {
    var featuresInput = document.forms["ratingForm"]["features"].value;
    if (featuresInput == "") {
        alert("Features must be filled out");
        return false;
    }
    return true;
}