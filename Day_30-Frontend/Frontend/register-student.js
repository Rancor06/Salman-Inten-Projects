// ==========================================
// REGEX PATTERNS (Task 03)
// ==========================================
const RE = {
  name:     /^[A-Za-z][A-Za-z\s]{2,49}$/,          // letters/spaces, 3-50 chars
  email:    /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  phone:    /^[6-9]\d{9}$/,                         // Indian mobile: starts 6-9, 10 digits
  rollNo:   /^[A-Za-z0-9\-\/]{4,15}$/,
  password: {
    len:   v => v.length >= 8,
    upper: v => /[A-Z]/.test(v),
    lower: v => /[a-z]/.test(v),
    num:   v => /\d/.test(v),
    spec:  v => /[^A-Za-z0-9]/.test(v)
  }
};

// ==========================================
// HELPERS
// ==========================================
function showErr(id, msg) {
  const el = document.getElementById(id);
  el.textContent = msg;
  el.classList.add('show');
}

function clearErr(id) {
  const el = document.getElementById(id);
  el.textContent = '';
  el.classList.remove('show');
}

function markField(el, valid) {
  el.classList.toggle('error', !valid);
  el.classList.toggle('valid', valid);
}

function calcAge(dobStr) {
  const dob = new Date(dobStr);
  const today = new Date();
  let age = today.getFullYear() - dob.getFullYear();
  const m = today.getMonth() - dob.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < dob.getDate())) age--;
  return age;
}

// ==========================================
// PASSWORD STRENGTH METER
// ==========================================
const pwInput = document.getElementById('password');
const pwBars = ['pb1', 'pb2', 'pb3', 'pb4'].map(id => document.getElementById(id));
const pwLabel = document.getElementById('pwStrengthLabel');
const barColors = ['#B42318', '#B45309', '#0F766E', '#0B5C56'];
const barLabels = ['Weak', 'Fair', 'Good', 'Strong'];

pwInput.addEventListener('input', () => {
  const v = pwInput.value;
  const score = Object.values(RE.password).filter(fn => fn(v)).length;

  if (!v) {
    pwBars.forEach(b => b.style.background = '#E1E5EB');
    pwLabel.textContent = '';
    return;
  }

  const idx = Math.min(score - 1, 3);
  pwBars.forEach((b, i) => b.style.background = i <= idx ? barColors[idx] : '#E1E5EB');
  pwLabel.textContent = barLabels[idx] || '';
  pwLabel.style.color = barColors[idx] || '#8B93A1';
});

// ==========================================
// SIDEBAR CHECKLIST — live section progress
// ==========================================
const checklistItems = document.querySelectorAll('.checklist li');

function updateChecklist(filledSections) {
  checklistItems.forEach((li, i) => {
    const numEl = li.querySelector('.num');
    li.classList.remove('active', 'done');
    if (i < filledSections) {
      li.classList.add('done');
      numEl.textContent = '✓';
    } else {
      numEl.textContent = i + 1;
      if (i === filledSections) li.classList.add('active');
    }
  });
}

document.getElementById('regForm').addEventListener('input', () => {
  const p1 = document.getElementById('fullName').value.trim()
          && document.getElementById('dob').value
          && document.querySelector('input[name="gender"]:checked');

  const p2 = document.getElementById('email').value.trim()
          && document.getElementById('phone').value.trim();

  const p3 = document.getElementById('rollNo').value.trim()
          && document.getElementById('course').value
          && document.getElementById('semester').value
          && document.getElementById('attendance').value !== ''
          && document.getElementById('gpa').value !== '';

  const p4 = document.getElementById('password').value
          && document.getElementById('confirmPw').value;

  let done = 0;
  if (p1) done = 1;
  if (p1 && p2) done = 2;
  if (p1 && p2 && p3) done = 3;
  if (p1 && p2 && p3 && p4) done = 4;

  updateChecklist(done);
});

// ==========================================
// FORM SUBMIT & VALIDATION (Task 02 + 03)
// ==========================================
document.getElementById('regForm').addEventListener('submit', function (e) {
  e.preventDefault();
  let valid = true;

  // — Personal —
  const fullName = document.getElementById('fullName');
  if (!RE.name.test(fullName.value.trim())) {
    showErr('fullNameErr', 'Enter a valid name (letters and spaces, 3+ characters)');
    markField(fullName, false); valid = false;
  } else { clearErr('fullNameErr'); markField(fullName, true); }

  const dob = document.getElementById('dob');
  if (!dob.value) {
    showErr('dobErr', 'Date of birth is required');
    markField(dob, false); valid = false;
  } else if (calcAge(dob.value) < 18) {
    showErr('dobErr', 'Student must be at least 18 years old');
    markField(dob, false); valid = false;
  } else { clearErr('dobErr'); markField(dob, true); }

  const gender = document.querySelector('input[name="gender"]:checked');
  const genderGroup = document.querySelector('.radio-group');
  if (!gender) {
    showErr('genderErr', 'Please select a gender');
    genderGroup.classList.add('error'); valid = false;
  } else { clearErr('genderErr'); genderGroup.classList.remove('error'); }

  // — Contact —
  const email = document.getElementById('email');
  if (!RE.email.test(email.value.trim())) {
    showErr('emailErr', 'Enter a valid email address');
    markField(email, false); valid = false;
  } else { clearErr('emailErr'); markField(email, true); }

  const phone = document.getElementById('phone');
  if (!RE.phone.test(phone.value.trim())) {
    showErr('phoneErr', 'Enter a valid 10-digit mobile number (starts 6-9)');
    markField(phone, false); valid = false;
  } else { clearErr('phoneErr'); markField(phone, true); }

  // — Academic Details —
  const rollNo = document.getElementById('rollNo');
  if (!RE.rollNo.test(rollNo.value.trim())) {
    showErr('rollNoErr', 'Enter a valid roll number (4-15 characters)');
    markField(rollNo, false); valid = false;
  } else { clearErr('rollNoErr'); markField(rollNo, true); }

  const course = document.getElementById('course');
  if (!course.value) {
    showErr('courseErr', 'Please select a course');
    markField(course, false); valid = false;
  } else { clearErr('courseErr'); markField(course, true); }

  const semester = document.getElementById('semester');
  if (!semester.value) {
    showErr('semesterErr', 'Please select a semester');
    markField(semester, false); valid = false;
  } else { clearErr('semesterErr'); markField(semester, true); }

  const attendance = document.getElementById('attendance');
  const attVal = parseFloat(attendance.value);
  if (attendance.value === '' || isNaN(attVal) || attVal < 0 || attVal > 100) {
    showErr('attendanceErr', 'Enter attendance between 0 and 100');
    markField(attendance, false); valid = false;
  } else { clearErr('attendanceErr'); markField(attendance, true); }

  const gpa = document.getElementById('gpa');
  const gpaVal = parseFloat(gpa.value);
  if (gpa.value === '' || isNaN(gpaVal) || gpaVal < 0 || gpaVal > 10) {
    showErr('gpaErr', 'Enter GPA between 0.00 and 10.00');
    markField(gpa, false); valid = false;
  } else { clearErr('gpaErr'); markField(gpa, true); }

  const backlogs = document.getElementById('backlogs');
  if (backlogs.value !== '' && (isNaN(backlogs.value) || parseInt(backlogs.value) < 0)) {
    showErr('backlogsErr', 'Backlogs must be a non-negative number');
    markField(backlogs, false); valid = false;
  } else { clearErr('backlogsErr'); if (backlogs.value !== '') markField(backlogs, true); }

  // — Account —
  const pw = document.getElementById('password');
  const pwOk = Object.values(RE.password).every(fn => fn(pw.value));
  if (!pwOk) {
    showErr('passwordErr', 'Password needs 8+ chars, upper, lower, number & special character');
    markField(pw, false); valid = false;
  } else { clearErr('passwordErr'); markField(pw, true); }

  const cpw = document.getElementById('confirmPw');
  if (!cpw.value || cpw.value !== pw.value) {
    showErr('confirmPwErr', 'Passwords do not match');
    markField(cpw, false); valid = false;
  } else { clearErr('confirmPwErr'); markField(cpw, true); }

  if (!valid) return;

  // — Success —
  const toast = document.getElementById('toast');
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3500);

  this.reset();
  document.querySelectorAll('.err-msg').forEach(el => el.classList.remove('show'));
  document.querySelectorAll('input, select').forEach(el => el.classList.remove('error', 'valid'));
  pwBars.forEach(b => b.style.background = '#E1E5EB');
  pwLabel.textContent = '';
  genderGroup.classList.remove('error');
  updateChecklist(0);
});
