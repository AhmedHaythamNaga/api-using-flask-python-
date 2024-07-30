document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const errorMessage = document.getElementById("error-message");

    loginForm.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(loginForm);
        const data = new URLSearchParams(formData).toString();

        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: data
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                errorMessage.textContent = result.error;
            } else {
                alert(result.message);
                window.location.href = "/contacts"; // Redirect to contacts page on success
            }
        })
        .catch(error => {
            errorMessage.textContent = 'An unexpected error occurred.';
            console.error('Error:', error);
        });
    });
});
