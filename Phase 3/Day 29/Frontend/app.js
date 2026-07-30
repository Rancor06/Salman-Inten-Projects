// Settings page: live threshold slider values
const watchSlider = document.getElementById('watchSlider');
const riskSlider = document.getElementById('riskSlider');
if (watchSlider) watchSlider.addEventListener('input', e => document.getElementById('watchVal').textContent = e.target.value + '%');
if (riskSlider) riskSlider.addEventListener('input', e => document.getElementById('riskVal').textContent = e.target.value + '%');

// Attendance trend chart (Reports page)
const trendEl = document.getElementById('trendChart');
if (trendEl) {
    const data = [88, 85, 83, 80, 79, 81];
    const labels = ['Wk 1', 'Wk 2', 'Wk 3', 'Wk 4', 'Wk 5', 'Wk 6'];
    const w = 460, h = 160, pad = 28;
    const min = 70, max = 95;
    const x = i => pad + (i * (w - pad * 2)) / (data.length - 1);
    const y = v => h - pad - ((v - min) / (max - min)) * (h - pad * 2);
    const points = data.map((v, i) => `${x(i)},${y(v)}`).join(' ');
    const dots = data.map((v, i) => `<circle cx="${x(i)}" cy="${y(v)}" r="3.5" fill="#33415C"/>`).join('');
    const labelEls = labels.map((l, i) => `<text x="${x(i)}" y="${h - 6}" font-size="10" fill="#8B93A6" text-anchor="middle" font-family="IBM Plex Mono, monospace">${l}</text>`).join('');
    trendEl.innerHTML = `
        <svg class="trend-svg" viewBox="0 0 ${w} ${h}" xmlns="http://www.w3.org/2000/svg">
            <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${h - pad}" stroke="#E1E5EC"/>
            <line x1="${pad}" y1="${h - pad}" x2="${w - pad}" y2="${h - pad}" stroke="#E1E5EC"/>
            <polyline points="${points}" fill="none" stroke="#33415C" stroke-width="2"/>
            ${dots}
            ${labelEls}
        </svg>`;
}

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
