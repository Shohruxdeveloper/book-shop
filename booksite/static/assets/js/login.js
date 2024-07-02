document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Perform your login logic here. For demonstration, let's assume it's a simple check.
    if (username === "user" && password === "pass") {
        document.getElementById('message').innerHTML = "Login successful!";
        document.getElementById('message').style.color = "green";
    } else {
        document.getElementById('message').innerHTML = "Invalid username or password.";
        document.getElementById('message').style.color = "red";
    }
});
