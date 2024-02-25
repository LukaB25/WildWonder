document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("article-edit")
    
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteArticleModal"));
    const deleteButton = document.getElementById("article-delete");
    const deleteConfirm = document.getElementById("deleteArticleConfirm");
    
    /**
     * Initializes edit functionality for the provided edit button.
     * 
     * For 'editButton':
     * - Fetches the content of the corresponding article.
     * - Triggers a window location change to the 'edit/' endpoint.
     */
    editButton.addEventListener("click", (e) => {
        window.location.href = 'edit/';
        });
    
    /**
     * Initializes deletion functionality for the provided delete button.
     * 
     * For 'deleteButton':
     * - Updates the `deleteConfirm` link's href to point to the 
     * deletion endpoint for the specific article.
     * - Displays a confirmation modal (`deleteModal`) to prompt 
     * the user for confirmation before deletion.
     */
    deleteButton.addEventListener("click", (e) => {
        deleteConfirm.href = 'delete/';
        deleteModal.show();
        });
});
