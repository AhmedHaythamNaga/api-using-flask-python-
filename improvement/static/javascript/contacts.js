document.addEventListener("DOMContentLoaded", function() {
    const contactsList = document.getElementById("list");
    const errorMessage = document.getElementById("error-message");

    fetch('/contacts/list')
        .then(response => response.json())
        .then(contacts => {
            contacts.forEach(contact => {
                const contactElement = document.createElement("li");
                contactElement.id = `contact-${contact.id}`;
                contactElement.innerHTML = `
                    <span class="contact-name">${contact.name}</span>
                    <span class="rightmost">
                        <a href="/contacts/${contact.id}" class="icon-link">
                            <i class="fa-solid fa-eye" style="color:black;" title="View"></i>
                        </a>
                        <a href="/contacts/${contact.id}/edit" class="icon-link">
                            <i class="fa-solid fa-pen" style="color:black;" title="Edit"></i>
                        </a>
                        <form action="/contacts/${contact.id}/remove" method="POST" style="display:inline;" class="remove-contact-form">
                            <button type="submit" class="icon-link" style="background:none; border:none; cursor:pointer;color:black;" id="trash-${contact.id}">
                                <i class="fa-solid fa-trash" title="Remove"></i>
                            </button>
                        </form>
                    </span>
                    <br><br>
                `;
                contactsList.appendChild(contactElement);
            });
        })
        .catch(error => {
            errorMessage.textContent = 'An unexpected error occurred.';
            console.error('Error:', error);
        });
});