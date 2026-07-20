// ===============================
// Registration Form Validation
// ===============================
function validateRegister() {

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();
    let confirmPassword = document.getElementById("confirmPassword").value.trim();

    if (name === "") {
        alert("Please enter your name.");
        return false;
    }

    if (email === "") {
        alert("Please enter your email.");
        return false;
    }

    if (password === "") {
        alert("Please enter your password.");
        return false;
    }

    if (password.length < 6) {
        alert("Password must be at least 6 characters.");
        return false;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return false;
    }

    return true;
}

// ===============================
// Login Form Validation
// ===============================
function validateLogin() {

    let email = document.getElementById("email").value.trim();
    let password = document.getElementById("password").value.trim();

    if (email === "") {
        alert("Please enter your email.");
        return false;
    }

    if (password === "") {
        alert("Please enter your password.");
        return false;
    }

    return true;
}

// ===============================
// Complaint Form Validation
// ===============================
function validateComplaint() {

    let complaintType = document.getElementById("complaintType").value;
    let subject = document.getElementById("subject").value.trim();
    let description = document.getElementById("description").value.trim();

    if (complaintType === "") {
        alert("Please select a complaint type.");
        return false;
    }

    if (subject === "") {
        alert("Please enter the complaint subject.");
        return false;
    }

    if (description === "") {
        alert("Please enter the complaint description.");
        return false;
    }

    alert("Complaint submitted successfully!");
    return true;
}
