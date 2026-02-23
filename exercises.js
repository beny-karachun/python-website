/* ===== CodingBat Exercises — Main Logic ===== */

(function () {
    'use strict';

    // ===== State =====
    let editor = null;
    let pyodide = null;
    let currentProblem = null;
    let solved = JSON.parse(localStorage.getItem('codingbat_solved') || '{}');

    // ===== DOM =====
    const categoriesList = document.getElementById('categories-list');
    const problemTitle = document.getElementById('problem-title');
    const descTitle = document.getElementById('desc-title');
    const descBody = document.getElementById('desc-body');
    const badgeTests = document.getElementById('badge-tests');
    const consoleOutput = document.getElementById('console-output');
    const editorFilename = document.getElementById('editor-filename');
    const btnRun = document.getElementById('btn-run');
    const btnReset = document.getElementById('btn-reset');
    const btnClear = document.getElementById('btn-clear-console');
    const pyodideStatus = document.getElementById('pyodide-status');
    const progressSummary = document.getElementById('progress-summary');
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');

    // ===== Initialize Monaco Editor =====
    function initMonaco() {
        return new Promise((resolve) => {
            require.config({
                paths: {
                    vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.45.0/min/vs'
                }
            });

            require(['vs/editor/editor.main'], function () {
                // Define a custom dark theme matching our CSS
                monaco.editor.defineTheme('codingbat-dark', {
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
                        'editor.background': '#1e1e1e',
                        'editor.foreground': '#d4d4d4',
                        'editorLineNumber.foreground': '#5a5a5a',
                        'editorLineNumber.activeForeground': '#c6c6c6',
                        'editor.selectionBackground': '#264f78',
                        'editor.lineHighlightBackground': '#2a2d2e',
                        'editorCursor.foreground': '#aeafad',
                        'editorIndentGuide.background': '#404040',
                    }
                });

                editor = monaco.editor.create(document.getElementById('monaco-editor'), {
                    value: '# Select a problem from the sidebar to begin\n',
                    language: 'python',
                    theme: 'codingbat-dark',
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
                    padding: { top: 12, bottom: 12 },
                    quickSuggestions: true,
                    suggestOnTriggerCharacters: true,
                    parameterHints: { enabled: true },
                    bracketPairColorization: { enabled: true },
                });

                // Ctrl+Enter to run
                editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, runTests);

                // Save code on change
                editor.onDidChangeModelContent(() => {
                    if (currentProblem) {
                        saveCode(currentProblem.id);
                    }
                });

                resolve();
            });
        });
    }

    // ===== Initialize Pyodide =====
    async function initPyodide() {
        const statusEl = pyodideStatus;
        try {
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/pyodide/v0.27.4/full/pyodide.js';
            document.head.appendChild(script);

            await new Promise((resolve, reject) => {
                script.onload = resolve;
                script.onerror = reject;
            });

            pyodide = await loadPyodide({
                indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.27.4/full/'
            });

            statusEl.innerHTML = '<div class="status-dot"></div><span>Pyodide Ready</span>';
        } catch (err) {
            statusEl.innerHTML = '<div class="status-dot error"></div><span>Pyodide Error</span>';
            console.error('Pyodide load error:', err);
        }
    }

    // ===== Render Sidebar =====
    function renderSidebar() {
        categoriesList.innerHTML = '';
        let totalProblems = 0;
        let totalSolved = 0;

        EXERCISES_DATA.categories.forEach((cat, ci) => {
            const catEl = document.createElement('div');
            catEl.className = 'category-item';

            const solvedInCat = cat.problems.filter(p => solved[p.id]).length;
            totalProblems += cat.problems.length;
            totalSolved += solvedInCat;

            const header = document.createElement('div');
            header.className = 'category-header';
            header.innerHTML = `
                <div class="category-header-left">
                    <span class="category-chevron"><i class="fa-solid fa-chevron-right"></i></span>
                    <span>${cat.name}</span>
                </div>
                <div style="display:flex;align-items:center;gap:6px;">
                    ${solvedInCat > 0 ? `<span class="category-progress">${solvedInCat}/${cat.problems.length}</span>` : ''}
                    <span class="category-count">${cat.problems.length}</span>
                </div>
            `;

            const list = document.createElement('div');
            list.className = 'problems-list';

            cat.problems.forEach(problem => {
                const item = document.createElement('div');
                item.className = 'problem-item' + (solved[problem.id] ? ' solved' : '');
                item.dataset.id = problem.id;
                item.innerHTML = `
                    <span class="solve-icon">${solved[problem.id] ? '<i class="fa-solid fa-check-circle"></i>' : '<i class="fa-regular fa-circle"></i>'}</span>
                    <span>${problem.name}</span>
                `;
                item.addEventListener('click', () => loadProblem(problem));
                list.appendChild(item);
            });

            header.addEventListener('click', () => {
                header.classList.toggle('active');
                list.classList.toggle('expanded');
            });

            catEl.appendChild(header);
            catEl.appendChild(list);
            categoriesList.appendChild(catEl);
        });

        progressSummary.textContent = `${totalSolved}/${totalProblems} solved`;
    }

    // ===== Load Problem =====
    function loadProblem(problem) {
        currentProblem = problem;

        // Update UI
        problemTitle.textContent = problem.name;
        descTitle.textContent = problem.name;
        editorFilename.textContent = problem.id + '.py';

        // Badge
        const testCount = problem.tests ? problem.tests.length : 0;
        badgeTests.textContent = testCount + ' tests';

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

        // Load saved code or stub
        const savedCode = loadCode(problem.id);
        editor.setValue(savedCode || problem.stub);

        // Clear console
        consoleOutput.innerHTML = `
            <div class="console-placeholder">
                <i class="fa-solid fa-code"></i>
                <p>Write your solution and press <kbd>Run Tests</kbd> or <kbd>Ctrl+Enter</kbd></p>
            </div>
        `;

        // Highlight active in sidebar
        document.querySelectorAll('.problem-item').forEach(el => {
            el.classList.toggle('active', el.dataset.id === problem.id);
        });

        // Close sidebar on mobile
        sidebar.classList.remove('open');

        // Focus editor
        editor.focus();
    }

    // ===== Run Tests =====
    async function runTests() {
        if (!currentProblem || !pyodide) {
            if (!pyodide) {
                consoleOutput.innerHTML = '<div class="test-line test-error"><span class="icon"><i class="fa-solid fa-exclamation-triangle"></i></span><span class="detail">Pyodide is still loading. Please wait...</span></div>';
            }
            return;
        }

        const tests = currentProblem.tests;
        if (!tests || tests.length === 0) {
            consoleOutput.innerHTML = '<div class="test-line test-error"><span class="icon"><i class="fa-solid fa-info-circle"></i></span><span class="detail">No test cases available for this problem.</span></div>';
            return;
        }

        btnRun.classList.add('running');
        btnRun.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> <span>Running...</span>';
        consoleOutput.innerHTML = '';

        const userCode = editor.getValue();
        let passed = 0;
        let failed = 0;
        let error = false;

        // First, try to define the user's function
        try {
            await pyodide.runPythonAsync(userCode);
        } catch (err) {
            consoleOutput.innerHTML = `
                <div class="test-line test-error">
                    <span class="icon"><i class="fa-solid fa-xmark"></i></span>
                    <span class="detail">Error in your code:</span>
                </div>
                <pre style="color:var(--red);margin:8px 0;padding:8px;background:var(--red-bg);border-radius:4px;font-size:12px;overflow-x:auto;">${escapeHTML(err.message)}</pre>
            `;
            btnRun.classList.remove('running');
            btnRun.innerHTML = '<i class="fa-solid fa-play"></i> <span>Run Tests</span>';
            return;
        }

        // Run each test
        for (let i = 0; i < tests.length; i++) {
            const test = tests[i];
            const line = document.createElement('div');
            line.style.animationDelay = (i * 30) + 'ms';

            try {
                const result = await pyodide.runPythonAsync(`
result = ${test.call}
repr(result)
`);
                const expectedRepr = await pyodide.runPythonAsync(`repr(${test.expected})`);

                if (result === expectedRepr) {
                    passed++;
                    line.className = 'test-line test-pass';
                    line.innerHTML = `
                        <span class="icon"><i class="fa-solid fa-check"></i></span>
                        <span class="detail"><code>${escapeHTML(test.call)}</code> → ${escapeHTML(test.expected)}</span>
                    `;
                } else {
                    failed++;
                    // Get the actual display value
                    const actualDisplay = await pyodide.runPythonAsync(`str(${test.call})`);
                    line.className = 'test-line test-fail';
                    line.innerHTML = `
                        <span class="icon"><i class="fa-solid fa-xmark"></i></span>
                        <span class="detail"><code>${escapeHTML(test.call)}</code> → expected <strong>${escapeHTML(test.expected)}</strong>, got <strong>${escapeHTML(actualDisplay)}</strong></span>
                    `;
                }
            } catch (err) {
                failed++;
                line.className = 'test-line test-error';
                line.innerHTML = `
                    <span class="icon"><i class="fa-solid fa-exclamation-triangle"></i></span>
                    <span class="detail"><code>${escapeHTML(test.call)}</code> → Error: ${escapeHTML(err.message.split('\n').pop())}</span>
                `;
            }

            consoleOutput.appendChild(line);
        }

        // Summary
        const summary = document.createElement('div');
        const allPassed = failed === 0 && passed > 0;
        summary.className = 'test-summary ' + (allPassed ? 'all-pass' : 'has-fail');
        summary.innerHTML = `
            <i class="fa-solid ${allPassed ? 'fa-circle-check' : 'fa-circle-xmark'}"></i>
            <span>${passed}/${passed + failed} tests passed${allPassed ? ' — All correct! 🎉' : ''}</span>
        `;
        consoleOutput.appendChild(summary);

        // Mark as solved
        if (allPassed) {
            solved[currentProblem.id] = true;
            localStorage.setItem('codingbat_solved', JSON.stringify(solved));
            renderSidebar();
            // Re-highlight active problem
            document.querySelectorAll('.problem-item').forEach(el => {
                el.classList.toggle('active', el.dataset.id === currentProblem.id);
            });
        }

        btnRun.classList.remove('running');
        btnRun.innerHTML = '<i class="fa-solid fa-play"></i> <span>Run Tests</span>';
    }

    // ===== LocalStorage Helpers =====
    function saveCode(problemId) {
        const code = editor.getValue();
        localStorage.setItem('codingbat_code_' + problemId, code);
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

    btnClear.addEventListener('click', () => {
        consoleOutput.innerHTML = `
            <div class="console-placeholder">
                <i class="fa-solid fa-code"></i>
                <p>Write your solution and press <kbd>Run Tests</kbd> or <kbd>Ctrl+Enter</kbd></p>
            </div>
        `;
    });

    sidebarToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });

    // ===== Init =====
    async function init() {
        renderSidebar();

        // Open first category
        const firstHeader = categoriesList.querySelector('.category-header');
        if (firstHeader) {
            firstHeader.classList.add('active');
            firstHeader.nextElementSibling.classList.add('expanded');
        }

        // Load Monaco and Pyodide in parallel
        await Promise.all([initMonaco(), initPyodide()]);
    }

    init();
})();
