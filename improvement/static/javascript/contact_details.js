document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactDetails");
    const errorMessage = document.createElement("div");
    errorMessage.style.color = "red";
    form.insertBefore(errorMessage, form.firstChild);

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        fetch(form.action, {
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
                window.location.href = "/contacts"; // Redirect to contacts page on success
            }
        })
        .catch(error => {
            errorMessage.textContent = 'An unexpected error occurred.';
            console.error('Error:', error);
        });
    });

    const enableEditRadio = document.getElementById("m");
    const disableEditRadio = document.getElementById("b");

    enableEditRadio.addEventListener("change", function() {
        toggleEditMode(true);
    });

    disableEditRadio.addEventListener("change", function() {
        toggleEditMode(false);
    });

    function toggleEditMode(enable) {
        const inputs = document.querySelectorAll(".edit");
        inputs.forEach(input => {
            input.readOnly = !enable;
        });
    }
});
