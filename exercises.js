/* ===== CodingBat Exercises — Gamified Logic ===== */

(function () {
    'use strict';

    // ===== Category Emojis & Difficulty =====
    const CATEGORY_META = {
        'Warmup-1': { emoji: '☀️', difficulty: 'easy', xp: 10 },
        'Warmup-2': { emoji: '🌤️', difficulty: 'easy', xp: 15 },
        'String-1': { emoji: '🔤', difficulty: 'easy', xp: 15 },
        'String-2': { emoji: '📝', difficulty: 'medium', xp: 20 },
        'String-3': { emoji: '🧩', difficulty: 'hard', xp: 30 },
        'Logic-1': { emoji: '🧠', difficulty: 'medium', xp: 20 },
        'Logic-2': { emoji: '🎯', difficulty: 'hard', xp: 30 },
        'Recursion-1': { emoji: '🔁', difficulty: 'medium', xp: 25 },
        'Recursion-2': { emoji: '🌀', difficulty: 'hard', xp: 35 },
    };

    const LEVELS = [
        { name: 'Beginner', icon: '🌱', minXP: 0 },
        { name: 'Learner', icon: '📖', minXP: 50 },
        { name: 'Coder', icon: '💻', minXP: 150 },
        { name: 'Problem Solver', icon: '🧠', minXP: 350 },
        { name: 'Skilled', icon: '⚡', minXP: 600 },
        { name: 'Expert', icon: '🏆', minXP: 1000 },
        { name: 'Master', icon: '👑', minXP: 1500 },
        { name: 'Legend', icon: '🌟', minXP: 2500 },
    ];

    // ===== State =====
    let editor = null;
    let pyodide = null;
    let currentProblem = null;
    let currentCategory = null;
    let solved = JSON.parse(localStorage.getItem('codingbat_solved') || '{}');
    let xp = parseInt(localStorage.getItem('codingbat_xp') || '0');
    let streak = parseInt(localStorage.getItem('codingbat_streak') || '0');

    // ===== DOM =====
    const categoriesList = document.getElementById('categories-list');
    const descTitle = document.getElementById('desc-title');
    const descBody = document.getElementById('desc-body');
    const badgeTests = document.getElementById('badge-tests');
    const badgeDifficulty = document.getElementById('badge-difficulty');
    const problemEmoji = document.getElementById('problem-emoji');
    const consoleOutput = document.getElementById('console-output');
    const editorFilename = document.getElementById('editor-filename');
    const btnRun = document.getElementById('btn-run');
    const btnReset = document.getElementById('btn-reset');
    const btnClear = document.getElementById('btn-clear-console');
    const pyodideStatus = document.getElementById('pyodide-status');
    const progressSummary = document.getElementById('progress-summary');
    const overallProgressFill = document.getElementById('overall-progress-fill');
    const xpValue = document.getElementById('xp-value');
    const streakValue = document.getElementById('streak-value');
    const levelBadge = document.getElementById('level-badge');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');

    // ===== Confetti Engine =====
    const confettiCanvas = document.getElementById('confetti-canvas');
    const confettiCtx = confettiCanvas.getContext('2d');
    let confettiPieces = [];
    let confettiRunning = false;

    function resizeConfettiCanvas() {
        confettiCanvas.width = window.innerWidth;
        confettiCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeConfettiCanvas);
    resizeConfettiCanvas();

    function launchConfetti() {
        const colors = ['#6c5ce7', '#a29bfe', '#55efc4', '#00b894', '#fdcb6e', '#fd79a8', '#74b9ff', '#ffeaa7'];
        confettiPieces = [];
        for (let i = 0; i < 120; i++) {
            confettiPieces.push({
                x: window.innerWidth / 2 + (Math.random() - 0.5) * 200,
                y: window.innerHeight / 2,
                vx: (Math.random() - 0.5) * 16,
                vy: -(Math.random() * 12 + 5),
                color: colors[Math.floor(Math.random() * colors.length)],
                size: Math.random() * 8 + 4,
                rotation: Math.random() * 360,
                rotSpeed: (Math.random() - 0.5) * 12,
                gravity: 0.25 + Math.random() * 0.1,
                opacity: 1,
            });
        }
        if (!confettiRunning) {
            confettiRunning = true;
            animateConfetti();
        }
    }

    function animateConfetti() {
        confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
        let alive = false;
        for (const p of confettiPieces) {
            p.x += p.vx;
            p.vy += p.gravity;
            p.y += p.vy;
            p.vx *= 0.98;
            p.rotation += p.rotSpeed;
            p.opacity -= 0.008;
            if (p.opacity <= 0) continue;
            alive = true;
            confettiCtx.save();
            confettiCtx.translate(p.x, p.y);
            confettiCtx.rotate((p.rotation * Math.PI) / 180);
            confettiCtx.globalAlpha = p.opacity;
            confettiCtx.fillStyle = p.color;
            confettiCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
            confettiCtx.restore();
        }
        if (alive) {
            requestAnimationFrame(animateConfetti);
        } else {
            confettiRunning = false;
            confettiCtx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
        }
    }

    // ===== XP Float Animation =====
    function floatXP(amount) {
        const el = document.createElement('div');
        el.className = 'xp-float';
        el.textContent = `+${amount} XP`;
        el.style.left = '50%';
        el.style.top = '45%';
        el.style.transform = 'translateX(-50%)';
        document.body.appendChild(el);
        setTimeout(() => el.remove(), 1300);
    }

    // ===== Level Helpers =====
    function getLevel(xpAmount) {
        let level = LEVELS[0];
        for (const l of LEVELS) {
            if (xpAmount >= l.minXP) level = l;
        }
        return level;
    }

    function updateGameUI() {
        xpValue.textContent = `${xp} XP`;
        streakValue.textContent = streak;
        const level = getLevel(xp);
        levelBadge.innerHTML = `<span class="level-icon">${level.icon}</span><span class="level-text">${level.name}</span>`;
    }

    // ===== Initialize Monaco Editor =====
    function initMonaco() {
        return new Promise((resolve) => {
            require.config({
                paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs' }
            });

            require(['vs/editor/editor.main'], function () {
                monaco.editor.defineTheme('codingbat-gamified', {
                    base: 'vs-dark',
                    inherit: true,
                    rules: [
                        { token: 'comment', foreground: '6A9955', fontStyle: 'italic' },
                        { token: 'keyword', foreground: 'C586C0' },
                        { token: 'string', foreground: 'CE9178' },
                        { token: 'number', foreground: 'B5CEA8' },
                        { token: 'identifier', foreground: '9CDCFE' },
                        { token: 'type', foreground: '4EC9B0' },
                    ],
                    colors: {
                        'editor.background': '#1a1a2e',
                        'editor.foreground': '#d4d4d4',
                        'editorLineNumber.foreground': '#4a4a6a',
                        'editorLineNumber.activeForeground': '#a29bfe',
                        'editor.selectionBackground': '#3d3d6e',
                        'editor.lineHighlightBackground': '#22223a',
                        'editorCursor.foreground': '#a29bfe',
                        'editorIndentGuide.background': '#2d2d4a',
                    }
                });

                editor = monaco.editor.create(document.getElementById('monaco-editor'), {
                    value: '# Pick a challenge from the sidebar! 🎯\n',
                    language: 'python',
                    theme: 'codingbat-gamified',
                    fontSize: 14,
                    fontFamily: "'JetBrains Mono', 'Fira Code', 'Consolas', monospace",
                    fontLigatures: true,
                    minimap: { enabled: false },
                    scrollBeyondLastLine: false,
                    lineNumbers: 'on',
                    renderLineHighlight: 'line',
                    automaticLayout: true,
                    tabSize: 4,
                    wordWrap: 'on',
                    padding: { top: 14, bottom: 14 },
                    quickSuggestions: true,
                    suggestOnTriggerCharacters: true,
                    parameterHints: { enabled: true },
                    bracketPairColorization: { enabled: true },
                    cursorBlinking: 'smooth',
                    smoothScrolling: true,
                });

                editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, runTests);

                editor.onDidChangeModelContent(() => {
                    if (currentProblem) saveCode(currentProblem.id);
                });

                resolve();
            });
        });
    }

    // ===== Initialize Pyodide =====
    async function initPyodide() {
        try {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/pyodide/v0.27.4/full/pyodide.js';
            document.head.appendChild(script);
            await new Promise((resolve, reject) => { script.onload = resolve; script.onerror = reject; });
            pyodide = await loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.27.4/full/' });
            pyodideStatus.innerHTML = '<div class="status-dot"></div><span>Python Ready ✓</span>';
        } catch (err) {
            pyodideStatus.innerHTML = '<div class="status-dot error"></div><span>Python Error</span>';
            console.error('Pyodide load error:', err);
        }
    }

    // ===== Render Sidebar =====
    function renderSidebar() {
        categoriesList.innerHTML = '';
        let totalProblems = 0;
        let totalSolved = 0;

        EXERCISES_DATA.categories.forEach((cat) => {
            const meta = CATEGORY_META[cat.name] || { emoji: '📁', difficulty: 'medium', xp: 15 };
            const catEl = document.createElement('div');
            catEl.className = 'category-item';

            const solvedInCat = cat.problems.filter(p => solved[p.id]).length;
            totalProblems += cat.problems.length;
            totalSolved += solvedInCat;
            const progress = cat.problems.length > 0 ? (solvedInCat / cat.problems.length) * 100 : 0;

            const header = document.createElement('div');
            header.className = 'category-header' + (cat.name === currentCategory ? ' active' : '');
            header.innerHTML = `
                <div class="category-header-left">
                    <span class="category-chevron"><i class="fa-solid fa-chevron-right"></i></span>
                    <span class="category-emoji">${meta.emoji}</span>
                    <span>${cat.name}</span>
                </div>
                <div class="category-right">
                    <div class="category-progress-bar">
                        <div class="category-progress-fill" style="width:${progress}%"></div>
                    </div>
                    <span class="category-count">${solvedInCat}/${cat.problems.length}</span>
                </div>
            `;

            const list = document.createElement('div');
            list.className = 'problems-list' + (cat.name === currentCategory ? ' expanded' : '');

            cat.problems.forEach(problem => {
                const isSolved = solved[problem.id];
                const item = document.createElement('div');
                item.className = 'problem-item' + (isSolved ? ' solved' : '') + (currentProblem && currentProblem.id === problem.id ? ' active' : '');
                item.dataset.id = problem.id;
                item.innerHTML = `
                    <span class="solve-icon">${isSolved ? '✅' : '○'}</span>
                    <span>${problem.name}</span>
                `;
                item.addEventListener('click', () => {
                    currentCategory = cat.name;
                    loadProblem(problem, cat.name);
                });
                list.appendChild(item);
            });

            header.addEventListener('click', () => {
                const wasActive = header.classList.contains('active');
                // Close all
                document.querySelectorAll('.category-header.active').forEach(h => h.classList.remove('active'));
                document.querySelectorAll('.problems-list.expanded').forEach(l => l.classList.remove('expanded'));
                if (!wasActive) {
                    header.classList.add('active');
                    list.classList.add('expanded');
                    currentCategory = cat.name;
                } else {
                    currentCategory = null;
                }
            });

            catEl.appendChild(header);
            catEl.appendChild(list);
            categoriesList.appendChild(catEl);
        });

        const overallProgress = totalProblems > 0 ? (totalSolved / totalProblems) * 100 : 0;
        progressSummary.textContent = `${totalSolved}/${totalProblems}`;
        overallProgressFill.style.width = overallProgress + '%';
    }

    // ===== Load Problem =====
    function loadProblem(problem, categoryName) {
        currentProblem = problem;
        const meta = CATEGORY_META[categoryName] || { emoji: '📝', difficulty: 'medium', xp: 15 };

        // Update header
        problemEmoji.textContent = meta.emoji;
        descTitle.textContent = problem.name;
        editorFilename.textContent = problem.id + '.py';

        // Difficulty badge
        const diffLabels = { easy: '🟢 Easy', medium: '🟡 Medium', hard: '🔴 Hard' };
        badgeDifficulty.className = 'badge-difficulty ' + meta.difficulty;
        badgeDifficulty.textContent = diffLabels[meta.difficulty] || meta.difficulty;

        // Test count
        const testCount = problem.tests ? problem.tests.length : 0;
        badgeTests.textContent = `${testCount} tests`;

        // Description
        let descHTML = `<p>${escapeHTML(problem.description).replace(/\n/g, '<br>')}</p>`;
        if (problem.tests && problem.tests.length > 0) {
            descHTML += '<div class="desc-examples">';
            const showCount = Math.min(problem.tests.length, 3);
            for (let i = 0; i < showCount; i++) {
                const t = problem.tests[i];
                descHTML += `<div class="example-chip">${escapeHTML(t.call)} <span class="arrow">→</span> <span class="expected">${escapeHTML(t.expected)}</span></div>`;
            }
            if (problem.tests.length > 3) {
                descHTML += `<div class="example-chip" style="color:var(--text-muted);">+${problem.tests.length - 3} more</div>`;
            }
            descHTML += '</div>';
        }
        descBody.innerHTML = descHTML;

        // Load code
        const savedCode = loadCode(problem.id);
        editor.setValue(savedCode || problem.stub);

        // Clear console
        resetConsole();

        // Highlight active
        document.querySelectorAll('.problem-item').forEach(el => {
            el.classList.toggle('active', el.dataset.id === problem.id);
        });

        sidebar.classList.remove('open');
        editor.focus();
    }

    function resetConsole() {
        consoleOutput.innerHTML = `
            <div class="console-placeholder">
                <div class="placeholder-icon">🚀</div>
                <p>Write your solution and hit <kbd>Run Tests</kbd></p>
                <p class="placeholder-hint">or press <kbd>Ctrl+Enter</kbd></p>
            </div>
        `;
    }

    // ===== Run Tests =====
    async function runTests() {
        if (!currentProblem || !pyodide) {
            if (!pyodide) {
                consoleOutput.innerHTML = '<div class="test-line test-error"><span class="icon">⏳</span><span class="detail">Python is still loading... hang tight!</span></div>';
            }
            return;
        }

        const tests = currentProblem.tests;
        if (!tests || tests.length === 0) {
            consoleOutput.innerHTML = '<div class="test-line test-error"><span class="icon">ℹ️</span><span class="detail">No test cases available for this problem yet.</span></div>';
            return;
        }

        btnRun.classList.add('running');
        btnRun.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> <span>Running...</span>';
        consoleOutput.innerHTML = '';

        const userCode = editor.getValue();
        let passed = 0;
        let failed = 0;

        // Define user function
        try {
            await pyodide.runPythonAsync(userCode);
        } catch (err) {
            consoleOutput.innerHTML = `
                <div class="test-line test-error">
                    <span class="icon">💥</span>
                    <span class="detail">Oops! There's an error in your code:</span>
                </div>
                <pre style="color:var(--red);margin:8px 0;padding:12px;background:var(--red-bg);border:1px solid var(--red-border);border-radius:8px;font-size:12px;overflow-x:auto;">${escapeHTML(err.message)}</pre>
            `;
            btnRun.classList.remove('running');
            btnRun.innerHTML = '<i class="fa-solid fa-play"></i> <span>Run Tests</span>';
            return;
        }

        // Run each test
        for (let i = 0; i < tests.length; i++) {
            const test = tests[i];
            const line = document.createElement('div');
            line.style.animationDelay = (i * 40) + 'ms';

            try {
                const result = await pyodide.runPythonAsync(`result = ${test.call}\nrepr(result)`);
                const expectedRepr = await pyodide.runPythonAsync(`repr(${test.expected})`);

                if (result === expectedRepr) {
                    passed++;
                    line.className = 'test-line test-pass';
                    line.innerHTML = `<span class="icon">✅</span><span class="detail"><code>${escapeHTML(test.call)}</code> → ${escapeHTML(test.expected)}</span>`;
                } else {
                    failed++;
                    const actualDisplay = await pyodide.runPythonAsync(`str(${test.call})`);
                    line.className = 'test-line test-fail';
                    line.innerHTML = `<span class="icon">❌</span><span class="detail"><code>${escapeHTML(test.call)}</code> → expected <strong>${escapeHTML(test.expected)}</strong>, got <strong>${escapeHTML(actualDisplay)}</strong></span>`;
                }
            } catch (err) {
                failed++;
                line.className = 'test-line test-error';
                line.innerHTML = `<span class="icon">⚠️</span><span class="detail"><code>${escapeHTML(test.call)}</code> → ${escapeHTML(err.message.split('\\n').pop())}</span>`;
            }
            consoleOutput.appendChild(line);
        }

        // Summary
        const summary = document.createElement('div');
        const allPassed = failed === 0 && passed > 0;
        summary.className = 'test-summary ' + (allPassed ? 'all-pass' : 'has-fail');

        if (allPassed) {
            const meta = CATEGORY_META[currentCategory] || { xp: 15 };
            const alreadySolved = solved[currentProblem.id];
            const earnedXP = alreadySolved ? 0 : meta.xp;

            summary.innerHTML = `
                <span>🎉</span>
                <span>${passed}/${passed + failed} tests passed — Perfect!</span>
                ${earnedXP > 0 ? `<span class="xp-earned">+${earnedXP} XP</span>` : ''}
            `;

            if (!alreadySolved) {
                solved[currentProblem.id] = true;
                localStorage.setItem('codingbat_solved', JSON.stringify(solved));
                xp += earnedXP;
                streak++;
                localStorage.setItem('codingbat_xp', xp.toString());
                localStorage.setItem('codingbat_streak', streak.toString());
                updateGameUI();
                renderSidebar();
                // Re-highlight
                document.querySelectorAll('.problem-item').forEach(el => {
                    el.classList.toggle('active', el.dataset.id === currentProblem.id);
                });
                // Celebrations!
                launchConfetti();
                floatXP(earnedXP);
            }
        } else {
            summary.innerHTML = `<span>😅</span><span>${passed}/${passed + failed} tests passed — Keep trying!</span>`;
            streak = 0;
            localStorage.setItem('codingbat_streak', '0');
            updateGameUI();
        }
        consoleOutput.appendChild(summary);

        btnRun.classList.remove('running');
        btnRun.innerHTML = '<i class="fa-solid fa-play"></i> <span>Run Tests</span>';
    }

    // ===== LocalStorage =====
    function saveCode(problemId) {
        localStorage.setItem('codingbat_code_' + problemId, editor.getValue());
    }

    function loadCode(problemId) {
        return localStorage.getItem('codingbat_code_' + problemId);
    }

    // ===== Utilities =====
    function escapeHTML(str) {
        if (!str) return '';
        return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // ===== Event Listeners =====
    btnRun.addEventListener('click', runTests);

    btnReset.addEventListener('click', () => {
        if (currentProblem && confirm('Reset code to the original stub?')) {
            editor.setValue(currentProblem.stub);
            saveCode(currentProblem.id);
        }
    });

    btnClear.addEventListener('click', resetConsole);

    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    // ===== Init =====
    async function init() {
        updateGameUI();
        renderSidebar();

        // Open first category
        const firstHeader = categoriesList.querySelector('.category-header');
        if (firstHeader) {
            firstHeader.classList.add('active');
            firstHeader.nextElementSibling.classList.add('expanded');
            currentCategory = EXERCISES_DATA.categories[0]?.name;
        }

        await Promise.all([initMonaco(), initPyodide()]);
    }

    init();
})();
