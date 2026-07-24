// Mobile sidebar nav toggle
const sidebarToggle = document.getElementById('sidebarToggle');
const sidebarNav = document.getElementById('sidebarNav');
if (sidebarToggle && sidebarNav) {
    sidebarToggle.addEventListener('click', () => {
        const isOpen = sidebarNav.classList.toggle('open');
        sidebarToggle.setAttribute('aria-expanded', String(isOpen));
    });
}

// Live search filter for the student register table
const searchInput = document.getElementById('studentSearch');
if (searchInput) {
    const rows = () => document.querySelectorAll('#studentTable tbody tr');
    searchInput.addEventListener('input', (e) => {
        const q = e.target.value.trim().toLowerCase();
        rows().forEach(row => {
            const name = row.querySelector('.student-name')?.textContent.toLowerCase() || '';
            const id = row.querySelector('.student-id')?.textContent.toLowerCase() || '';
            row.style.display = (name.includes(q) || id.includes(q)) ? '' : 'none';
        });
    });
}

// Animate risk-driver bars in from zero on load
document.querySelectorAll('.factor-bar span').forEach(bar => {
    const target = bar.style.width;
    bar.style.width = '0%';
    requestAnimationFrame(() => {
        setTimeout(() => { bar.style.transition = 'width 0.6s ease'; bar.style.width = target; }, 50);
    });
});
