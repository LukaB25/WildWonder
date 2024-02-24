document.addEventListener("DOMContentLoaded", function () {
    const editButton = document.getElementById("article-edit")
    const articleSlug = editButton.getAttribute('post_id')
    
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteArticleModal"));
    const deleteButton = document.getElementById("article-delete");
    const deleteConfirm = document.getElementById("deleteArticleConfirm");
    
    /**
     * Initializes edit functionality for the provided edit buttons.
     * 
     * For `editButton` in the collection:
     * - Retrieves the associated article's ID upon click.
     * - Fetches the content of the corresponding article.
     * - Populates the `articleText` input/textarea with the article's content for editing.
     * - Updates the submit button's text to "Update".
     * - Sets the form's action attribute to the `edit_article/{articleId}` endpoint.
     */
    editButton.addEventListener("click", (e) => {
        window.location.href = `edit/`;
        });
    
    /**
     * Initializes deletion functionality for the provided delete buttons.
     * 
     * For `deleteButton` in the collection:
     * - Retrieves the associated article's ID upon click.
     * - Updates the `deleteConfirm` link's href to point to the 
     * deletion endpoint for the specific article.
     * - Displays a confirmation modal (`deleteModal`) to prompt 
     * the user for confirmation before deletion.
     */
    deleteButton.addEventListener("click", (e) => {
        deleteConfirm.href = `delete/`;
        deleteModal.show();
        });
});