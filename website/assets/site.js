/* Native Material checkboxes remain the source of search/drawer state. */
document.querySelectorAll('.site-search-button, .site-menu-button').forEach(label => {
  label.addEventListener('keydown', event => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      label.click();
    }
  });
});
