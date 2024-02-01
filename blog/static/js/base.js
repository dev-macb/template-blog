const dropdownTrigger = document.getElementById('dropdown-trigger');
const dropdown = document.querySelector('.cabecalho-menu-butao .dropdown');

dropdownTrigger.addEventListener('mouseenter', () => {
    dropdown.classList.add('show-dropdown');
});

dropdownTrigger.addEventListener('mouseleave', () => {
    dropdown.classList.remove('show-dropdown');
});
