// Auto-resize textarea as the user types
document.getElementById('note-editor').addEventListener('input', function () {
    this.style.height = 'auto';  // Reset height
    this.style.height = (this.scrollHeight) + 'px';  // Set height to content's height
});