document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("add-contact-form");
    const errorMessage = document.getElementById("error-message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch('/contacts/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                errorMessage.textContent = result.error;
            } else {
                alert(result.message);
                window.location.href = "/contacts";
            }
        })
        .catch(error => {
            errorMessage.textContent = 'An unexpected error occurred.';
            console.error('Error:', error);
        });
    });

    document.getElementById("returnToContacts").addEventListener("click", function() {
        window.location.href = "/contacts";
    });
});
