document.addEventListener('DOMContentLoaded', () => {
    // Auth & Premium State
    let user = null;
    let hasPaidSemesterAccess = false;

    // 1. Generate Content Dynamically to save HTML space
    const hwTitles = [
        { id: 0, weight: 1, title: "היכרות עם סביבת העבודה, התקנת הקומפיילר וכתיבת תוכנית ראשונה." },
        { id: 1, weight: 1, title: "משתנים, תנאים, לולאות בסיסיות ופונקציות פשוטות." },
        { id: 2, weight: 1, title: "מחרוזות, רשימות, וטיפוסים מורכבים." },
        { id: 3, weight: 3, title: "מילונים, קבוצות, וסיבוכיות זמן וזכרון." },
        { id: 4, weight: 3, title: "רקורסיה ושימושים מתקדמים בפונקציות." },
        { id: 5, weight: 4, title: "תכנות מונחה עצמים (OOP), מחלקות, וירושה." },
        { id: 6, weight: 2, title: "מבני נתונים מתקדמים רשימות מקושרות ועצים." }
    ];

    const renderHomeworks = () => {
        const hwContainer = document.getElementById('homework-grid');
        if (!hwContainer) return;
        hwContainer.innerHTML = ''; // Clear existing

        hwTitles.forEach((hw, i) => {
            const isPremium = hw.id >= 3;
            const isLocked = isPremium && !hasPaidSemesterAccess;

            const card = document.createElement('div');
            card.className = `card glass fade-in-up ${isLocked ? 'premium-locked' : ''}`;
            card.style.transitionDelay = `${i * 0.1}s`;

            let premiumBadgeHtml = '';
            if (isPremium) {
                premiumBadgeHtml = isLocked
                    ? `<div class="premium-badge"><i class="fa-solid fa-lock"></i> החל משבוע זה נדרשת גישת פרימיום</div>`
                    : '<div class="locked-icon" title="נרכש פרימיום"><i class="fa-solid fa-unlock"></i></div>';
            }

            card.innerHTML = `
                ${isLocked ? premiumBadgeHtml : ''}
                <div class="card-header">
                    <div class="card-icon"><i class="fa-solid fa-code"></i></div>
                    <h3>גליון ${hw.id} (hw${hw.id})</h3>
                    ${!isLocked && isPremium ? premiumBadgeHtml : ''}
                </div>
                <p>${hw.title}</p>
                <div class="hw-weight"><i class="fa-solid fa-weight-hanging"></i> ${hw.weight}% מהציון הסופי</div>
            `;
            hwContainer.appendChild(card);
        });
    };

    renderHomeworks();

    const exTitles = [
        { id: 1, name: "סביבת עבודה", desc: "סביבת עבודה, שפת פייתון 3. אופן הכנה והגשה של תרגילי בית." },
        { id: 2, name: "משתנים וטיפוסים", desc: "קבועים, משתנים, טיפוסים. המרה (אוטומטית, מכוונת). אופרטורים אריתמטיים. הפקודה input()." },
        { id: 3, name: "לוגיקה ופלט", desc: "ערכי אמת. אופרטורים לוגיים. ביטויים לוגיים. סדר קדימויות. פלט מעוצב." },
        { id: 4, name: "Unicode ותנאים", desc: "המרת ל/ממספר (Unicode). משפטי תנאי." },
        { id: 5, name: "לולאות ורשימות", desc: "לולאות while. לולאות מקוננות. מחרוזות. רשימות." },
        { id: 6, name: "לולאות for ו-slicing", desc: "לולאות for. פעולות slicing ברשימות ומחרוזות. לולאות מקוננות." },
        { id: 8, name: "פונקציות", desc: "פונקציות. מחסנית הקריאות. העברת פרמטרים לפונקציה. Scope. Mutable/Immutable." },
        { id: 9, name: "ספריות וגרפיקה", desc: "ספריות, היסטוגרמה. פלט גרפי." },
        { id: 10, name: "סיבוכיות וחיפוש", desc: "ניתוח סיבוכיות זמן. חיפוש ליניארי וחיפוש בינארי ברשימה ממוינת." },
        { id: 11, name: "רקורסיה", desc: "רקורסיה." },
        { id: 12, name: "מיונים", desc: "מיונים. מיון רקורסיבי. מיזוג רשימות ממוינות." },
        { id: 13, name: "מבני נתונים והכנה למבחן", desc: "מבני נתונים נוספים (dict). שאלות מהמבחנים להכנה למבחן הקורס." }
    ];

    const exContainer = document.getElementById('exercises-timeline');
    if (exContainer) {
        exTitles.forEach((ex, i) => {
            const item = document.createElement('div');
            item.className = 'timeline-item fade-in-up';
            item.style.transitionDelay = `${i * 0.1}s`;
            item.innerHTML = `
                <div class="timeline-dot"></div>
                <div class="timeline-content glass">
                    <h3>תרגול ${ex.id}: ${ex.name}</h3>
                    <p>${ex.desc}</p>
                    <a href="javascript:void(0)" class="link-btn"><i class="fa-solid fa-file-pdf"></i> צפה במצגת</a>
                </div>
            `;
            exContainer.appendChild(item);
        });
    }

    const exams = [
        "מבחן סמסטר אביב תשפ\"ד - מועד א'",
        "מבחן סמסטר אביב תשפ\"ד - מועד ב'",
        "מבחן סמסטר חורף תשפ\"ד - מועד א'",
        "מבחן סמסטר קיץ תשפ\"ג - מועד א'"
    ];

    const examsList = document.getElementById('exams-list');
    if (examsList) {
        exams.forEach((exam, i) => {
            const link = document.createElement('a');
            link.href = 'javascript:void(0)';
            link.className = 'exam-link';
            link.innerHTML = `
                <span class="exam-title">${exam}</span>
                <i class="fa-solid fa-download"></i>
            `;
            examsList.appendChild(link);
        });
    }

    // Exam Prep - Algorithm patterns
    const algorithms = [
        {
            id: 'count',
            title: 'כמות דרכים',
            desc: 'ספירת מספר הדרכים לבחור תת-קבוצה שסכומה שווה ליעד',
            icon: 'fa-solid fa-hashtag',
            iconClass: 'count',
            returnTag: 'מחזיר: int (סכום)',
            tags: ['רקורסיה', 'subset sum'],
            code: `<span class="comment">## amount of ways to do something</span>
<span class="keyword">def</span> <span class="func">rec</span>(lst, summ):
    <span class="keyword">if not</span> lst:
        <span class="keyword">if</span> summ <span class="operator">==</span> <span class="number">0</span>:
            <span class="keyword">return</span> <span class="number">1</span>
        <span class="keyword">else</span>:
            <span class="keyword">return</span> <span class="number">0</span>

    option1 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ)
    option2 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ<span class="operator">-</span>lst[<span class="number">0</span>])

    <span class="keyword">return</span> option1<span class="operator">+</span>option2

lst <span class="operator">=</span> [<span class="number">1</span>,<span class="number">5</span>,<span class="number">3</span>,<span class="number">2</span>,<span class="number">6</span>,<span class="number">8</span>,<span class="number">3</span>]
summ <span class="operator">=</span> <span class="number">9</span>

<span class="built-in">print</span>(<span class="func">rec</span>(lst,summ))`
        },
        {
            id: 'max',
            title: 'מקסימום שמתאים',
            desc: 'מציאת מספר הפריטים המקסימלי שסכומם שווה בדיוק ליעד',
            icon: 'fa-solid fa-arrow-up-wide-short',
            iconClass: 'max',
            returnTag: 'מחזיר: int (מקסימום) / -1',
            tags: ['רקורסיה', 'אופטימיזציה'],
            code: `<span class="comment">## maximum amount that fit something</span>

<span class="keyword">def</span> <span class="func">rec</span>(lst, summ):
    <span class="keyword">if not</span> lst:
        <span class="keyword">if</span> summ <span class="operator">==</span> <span class="number">0</span>:
            <span class="keyword">return</span> <span class="number">0</span>
        <span class="keyword">else</span>:
            <span class="keyword">return</span> <span class="number">-1</span>

    option1 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ)
    option2 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ<span class="operator">-</span>lst[<span class="number">0</span>])

    <span class="keyword">if</span> option2 <span class="operator">>=</span> <span class="number">0</span>:
        option2<span class="operator">+=</span><span class="number">1</span>

    <span class="keyword">return</span> <span class="built-in">max</span>(option1,option2)

lst <span class="operator">=</span> [<span class="number">1</span>,<span class="number">5</span>,<span class="number">3</span>,<span class="number">2</span>,<span class="number">6</span>,<span class="number">8</span>,<span class="number">3</span>]
summ <span class="operator">=</span> <span class="number">9</span>

<span class="built-in">print</span>(<span class="func">rec</span>(lst,summ))`
        },
        {
            id: 'bool',
            title: 'האם אפשרי',
            desc: 'בדיקה האם קיימת תת-קבוצה שסכומה שווה ליעד',
            icon: 'fa-solid fa-circle-check',
            iconClass: 'bool',
            returnTag: 'מחזיר: True / False',
            tags: ['רקורסיה', 'בוליאני'],
            code: `<span class="comment">## if something is possible</span>

<span class="keyword">def</span> <span class="func">rec</span>(lst, summ):
    <span class="keyword">if not</span> lst:
        <span class="keyword">if</span> summ <span class="operator">==</span> <span class="number">0</span>:
            <span class="keyword">return</span> <span class="built-in">True</span>
        <span class="keyword">else</span>:
            <span class="keyword">return</span> <span class="built-in">False</span>

    option1 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ)
    option2 <span class="operator">=</span> <span class="func">rec</span>(lst[<span class="number">1</span>:], summ<span class="operator">-</span>lst[<span class="number">0</span>])

    <span class="keyword">return</span> option1 <span class="keyword">or</span> option2

lst <span class="operator">=</span> [<span class="number">1</span>,<span class="number">5</span>,<span class="number">3</span>,<span class="number">2</span>,<span class="number">6</span>,<span class="number">8</span>,<span class="number">3</span>]

<span class="built-in">print</span>(<span class="func">rec</span>(lst,<span class="number">8</span>))
<span class="built-in">print</span>(<span class="func">rec</span>(lst,<span class="number">135</span>))`
        },
        {
            id: 'closest',
            title: 'סכום קרוב מתחת למקסימום',
            desc: 'מציאת הסכום הגדול ביותר שלא חורג מערך מקסימלי נתון',
            icon: 'fa-solid fa-bullseye',
            iconClass: 'closest',
            returnTag: 'מחזיר: int (סכום מקסימלי) / -1',
            tags: ['רקורסיה', 'אקומולטור'],
            code: `<span class="comment">## closest sum to something or under some max value</span>
<span class="keyword">def</span> <span class="func">sum_under_max</span>(lst,max_val,value<span class="operator">=</span><span class="number">0</span>):
    <span class="keyword">if not</span> lst:
        <span class="keyword">if</span> value<span class="operator"><=</span>max_val:
            <span class="keyword">return</span> value
        <span class="keyword">else</span>:
            <span class="keyword">return</span> <span class="number">-1</span>

    option1 <span class="operator">=</span> <span class="func">sum_under_max</span>(lst[<span class="number">1</span>:],max_val,value)
    option2 <span class="operator">=</span> <span class="func">sum_under_max</span>(lst[<span class="number">1</span>:],max_val,value<span class="operator">+</span>lst[<span class="number">0</span>])

    <span class="keyword">return</span> <span class="built-in">max</span>(option1,option2)

lst <span class="operator">=</span> [<span class="number">5</span>,<span class="number">3</span>,<span class="number">9</span>,<span class="number">4</span>]
val <span class="operator">=</span> <span class="number">11</span>

<span class="built-in">print</span>(<span class="func">sum_under_max</span>(lst,val))`
        }
    ];

    const examPrepTabs = document.getElementById('exam-prep-tabs');
    const examPrepContent = document.getElementById('exam-prep-content');

    if (examPrepTabs && examPrepContent) {
        // Build tabs
        algorithms.forEach((algo, i) => {
            const tab = document.createElement('button');
            tab.className = `exam-prep-tab ${i === 0 ? 'active' : ''}`;
            tab.setAttribute('data-algo', algo.id);
            tab.innerHTML = `<span class="tab-number">${i + 1}</span> ${algo.title}`;
            examPrepTabs.appendChild(tab);
        });

        // Build content panels
        algorithms.forEach((algo, i) => {
            const panel = document.createElement('div');
            panel.className = `algorithm-panel ${i === 0 ? 'active' : ''}`;
            panel.setAttribute('data-algo', algo.id);

            const tagsHtml = algo.tags.map(t => `<span class="algo-tag">${t}</span>`).join('');

            panel.innerHTML = `
                <div class="algorithm-card">
                    <div class="algorithm-card-header">
                        <div class="algo-icon ${algo.iconClass}">
                            <i class="${algo.icon}"></i>
                        </div>
                        <div>
                            <h3>${algo.title}</h3>
                            <p>${algo.desc}</p>
                        </div>
                    </div>
                    <div class="algo-code-window">
                        <div class="window-header">
                            <span class="dot red"></span>
                            <span class="dot yellow"></span>
                            <span class="dot green"></span>
                            <span class="file-name">pattern_${i + 1}.py</span>
                        </div>
                        <pre><code>${algo.code}</code></pre>
                    </div>
                    <div class="algorithm-card-footer">
                        ${tagsHtml}
                        <span class="algo-tag return-type">${algo.returnTag}</span>
                    </div>
                </div>
            `;
            examPrepContent.appendChild(panel);
        });

        // Tab switching
        examPrepTabs.addEventListener('click', (e) => {
            const tab = e.target.closest('.exam-prep-tab');
            if (!tab) return;
            const algoId = tab.getAttribute('data-algo');

            examPrepTabs.querySelectorAll('.exam-prep-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            examPrepContent.querySelectorAll('.algorithm-panel').forEach(p => {
                p.classList.remove('active');
                if (p.getAttribute('data-algo') === algoId) {
                    p.classList.add('active');
                }
            });
        });
    }

    // Sort Algorithms
    const sortings = [
        {
            id: 'bucket',
            title: 'Bucket Sort',
            desc: 'מיון באמצעות היסטוגרמה (מערך מונים). רץ בזמן O(n). יעיל במיוחד כאשר טווח הערכים ידוע וקטן יחסית.',
            icon: 'fa-solid fa-bucket',
            iconClass: 'count', // Greenish
            returnTag: 'O(n) זמן | O(k) זכרון',
            tags: ['מיון', 'היסטוגרמה', 'O(n)'],
            code: `<span class="comment">## Bucket Sort using Histogram</span>
<span class="keyword">def</span> <span class="func">bucket_sort</span>(lst, max_val):
    <span class="comment"># Create a histogram (bucket array) initialized to 0</span>
    hist <span class="operator">=</span> [<span class="number">0</span>] <span class="operator">*</span> (max_val <span class="operator">+</span> <span class="number">1</span>)
    
    <span class="comment"># Count occurrences of each element</span>
    <span class="keyword">for</span> num <span class="keyword">in</span> lst:
        hist[num] <span class="operator">+=</span> <span class="number">1</span>
        
    <span class="comment"># Reconstruct the sorted list</span>
    sorted_lst <span class="operator">=</span> []
    <span class="keyword">for</span> i <span class="keyword">in</span> <span class="built-in">range</span>(<span class="built-in">len</span>(hist)):
        <span class="comment"># Append the element 'i' hist[i] times</span>
        sorted_lst <span class="operator">+=</span> [i] <span class="operator">*</span> hist[i]
        
    <span class="keyword">return</span> sorted_lst

lst <span class="operator">=</span> [<span class="number">4</span>, <span class="number">2</span>, <span class="number">2</span>, <span class="number">8</span>, <span class="number">3</span>, <span class="number">3</span>, <span class="number">1</span>]
max_v <span class="operator">=</span> <span class="number">8</span>
<span class="built-in">print</span>(<span class="func">bucket_sort</span>(lst, max_v))`
        },
        {
            id: 'bubble',
            title: 'Bubble Sort',
            desc: 'מיון בועות. רץ בזמן O(n^2). מבעבע את האיבר הגדול ביותר לסוף המערך בכל איטרציה.',
            icon: 'fa-solid fa-soap',
            iconClass: 'bool', // Blueish
            returnTag: 'O(n^2) זמן | O(1) זכרון',
            tags: ['מיון', 'בועות', 'O(n^2)'],
            code: `<span class="comment">## Bubble Sort</span>
<span class="keyword">def</span> <span class="func">bubble_sort</span>(lst):
    n <span class="operator">=</span> <span class="built-in">len</span>(lst)
    <span class="comment"># Traverse through all array elements</span>
    <span class="keyword">for</span> i <span class="keyword">in</span> <span class="built-in">range</span>(n):
        <span class="comment"># Last i elements are already in place</span>
        <span class="keyword">for</span> j <span class="keyword">in</span> <span class="built-in">range</span>(<span class="number">0</span>, n <span class="operator">-</span> i <span class="operator">-</span> <span class="number">1</span>):
            <span class="comment"># Swap if the element found is greater than the next element</span>
            <span class="keyword">if</span> lst[j] <span class="operator">></span> lst[j <span class="operator">+</span> <span class="number">1</span>]:
                lst[j], lst[j <span class="operator">+</span> <span class="number">1</span>] <span class="operator">=</span> lst[j <span class="operator">+</span> <span class="number">1</span>], lst[j]
                
    <span class="keyword">return</span> lst

lst <span class="operator">=</span> [<span class="number">64</span>, <span class="number">34</span>, <span class="number">25</span>, <span class="number">12</span>, <span class="number">22</span>, <span class="number">11</span>, <span class="number">90</span>]
<span class="built-in">print</span>(<span class="func">bubble_sort</span>(lst))`
        },
        {
            id: 'selection',
            title: 'Selection Sort',
            desc: 'מיון בחירה. רץ בזמן O(n^2). מוצא את האיבר הקטן ביותר ומציב אותו בתחילת המערך.',
            icon: 'fa-solid fa-hand-pointer',
            iconClass: 'closest', // Reddish
            returnTag: 'O(n^2) זמן | O(1) זכרון',
            tags: ['מיון', 'בחירה', 'O(n^2)'],
            code: `<span class="comment">## Selection Sort</span>
<span class="keyword">def</span> <span class="func">selection_sort</span>(lst):
    n <span class="operator">=</span> <span class="built-in">len</span>(lst)
    <span class="comment"># Traverse through all array elements</span>
    <span class="keyword">for</span> i <span class="keyword">in</span> <span class="built-in">range</span>(n):
        <span class="comment"># Find the minimum element in remaining unsorted array</span>
        min_idx <span class="operator">=</span> i
        <span class="keyword">for</span> j <span class="keyword">in</span> <span class="built-in">range</span>(i <span class="operator">+</span> <span class="number">1</span>, n):
            <span class="keyword">if</span> lst[min_idx] <span class="operator">></span> lst[j]:
                min_idx <span class="operator">=</span> j
                
        <span class="comment"># Swap the found minimum element with the first element        </span>
        lst[i], lst[min_idx] <span class="operator">=</span> lst[min_idx], lst[i]
        
    <span class="keyword">return</span> lst

lst <span class="operator">=</span> [<span class="number">64</span>, <span class="number">25</span>, <span class="number">12</span>, <span class="number">22</span>, <span class="number">11</span>]
<span class="built-in">print</span>(<span class="func">selection_sort</span>(lst))`
        },
        {
            id: 'merge',
            title: 'Merge Sort',
            desc: 'מיון מיזוג (רקורסיבי). רץ בזמן O(n*log(n)). מחלק את המערך לחצאים, ממיין וממזג אותם חזרה.',
            icon: 'fa-solid fa-code-merge',
            iconClass: 'max', // Yellowish
            returnTag: 'O(n*log(n)) זמן | O(n) זכרון',
            tags: ['מיון', 'מיזוג', 'רקורסיה', 'O(n*log(n))'],
            code: `<span class="comment">## Merge Sort</span>
<span class="keyword">def</span> <span class="func">merge</span>(left, right):
    result <span class="operator">=</span> []
    i <span class="operator">=</span> j <span class="operator">=</span> <span class="number">0</span>
    <span class="comment"># Compare elements and add smaller to result</span>
    <span class="keyword">while</span> i <span class="operator"><</span> <span class="built-in">len</span>(left) <span class="keyword">and</span> j <span class="operator"><</span> <span class="built-in">len</span>(right):
        <span class="keyword">if</span> left[i] <span class="operator"><</span> right[j]:
            result.append(left[i])
            i <span class="operator">+=</span> <span class="number">1</span>
        <span class="keyword">else</span>:
            result.append(right[j])
            j <span class="operator">+=</span> <span class="number">1</span>
            
    <span class="comment"># Add remaining elements</span>
    result.extend(left[i:])
    result.extend(right[j:])
    <span class="keyword">return</span> result

<span class="keyword">def</span> <span class="func">merge_sort</span>(lst):
    <span class="keyword">if</span> <span class="built-in">len</span>(lst) <span class="operator"><=</span> <span class="number">1</span>:
        <span class="keyword">return</span> lst
        
    <span class="comment"># Find middle and sort both halves</span>
    mid <span class="operator">=</span> <span class="built-in">len</span>(lst) <span class="operator">//</span> <span class="number">2</span>
    left_half <span class="operator">=</span> <span class="func">merge_sort</span>(lst[:mid])
    right_half <span class="operator">=</span> <span class="func">merge_sort</span>(lst[mid:])
    
    <span class="comment"># Merge the sorted halves</span>
    <span class="keyword">return</span> <span class="func">merge</span>(left_half, right_half)

lst <span class="operator">=</span> [<span class="number">38</span>, <span class="number">27</span>, <span class="number">43</span>, <span class="number">3</span>, <span class="number">9</span>, <span class="number">82</span>, <span class="number">10</span>]
<span class="built-in">print</span>(<span class="func">merge_sort</span>(lst))`
        }
    ];

    const sortPrepTabs = document.getElementById('sort-prep-tabs');
    const sortPrepContent = document.getElementById('sort-prep-content');

    if (sortPrepTabs && sortPrepContent) {
        // Build tabs
        sortings.forEach((algo, i) => {
            const tab = document.createElement('button');
            tab.className = `exam-prep-tab ${i === 0 ? 'active' : ''}`;
            tab.setAttribute('data-algo', algo.id);
            tab.innerHTML = `<span class="tab-number">${i + 1}</span> ${algo.title}`;
            sortPrepTabs.appendChild(tab);
        });

        // Build content panels
        sortings.forEach((algo, i) => {
            const panel = document.createElement('div');
            panel.className = `algorithm-panel ${i === 0 ? 'active' : ''}`;
            panel.setAttribute('data-algo', algo.id);

            const tagsHtml = algo.tags.map(t => `<span class="algo-tag">${t}</span>`).join('');

            panel.innerHTML = `
                <div class="algorithm-card">
                    <div class="algorithm-card-header">
                        <div class="algo-icon ${algo.iconClass}">
                            <i class="${algo.icon}"></i>
                        </div>
                        <div>
                            <h3>${algo.title}</h3>
                            <p>${algo.desc}</p>
                        </div>
                    </div>
                    <div class="algo-code-window">
                        <div class="window-header">
                            <span class="dot red"></span>
                            <span class="dot yellow"></span>
                            <span class="dot green"></span>
                            <span class="file-name">${algo.id}_sort.py</span>
                        </div>
                        <pre><code>${algo.code}</code></pre>
                    </div>
                    <div class="algorithm-card-footer">
                        ${tagsHtml}
                        <span class="algo-tag return-type">${algo.returnTag}</span>
                    </div>
                </div>
            `;
            sortPrepContent.appendChild(panel);
        });

        // Tab switching
        sortPrepTabs.addEventListener('click', (e) => {
            const tab = e.target.closest('.exam-prep-tab');
            if (!tab) return;
            const algoId = tab.getAttribute('data-algo');

            sortPrepTabs.querySelectorAll('.exam-prep-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            sortPrepContent.querySelectorAll('.algorithm-panel').forEach(p => {
                p.classList.remove('active');
                if (p.getAttribute('data-algo') === algoId) {
                    p.classList.add('active');
                }
            });
        });
    }

    // Search Algorithms
    const searches = [
        {
            id: 'binary_search',
            title: 'Binary Search (Iterative)',
            desc: 'חיפוש בינארי בלולאה (איטרטיבי). רץ בזמן O(log n) על מערך ממוין.',
            icon: 'fa-solid fa-magnifying-glass',
            iconClass: 'bool', // Blueish
            returnTag: 'O(log n) זמן | O(1) זכרון',
            tags: ['חיפוש', 'בינארי', 'לולאה'],
            code: `<span class="comment">## Binary Search (Iterative)</span>
<span class="keyword">def</span> <span class="func">binary_search</span>(lst, target):
    low <span class="operator">=</span> <span class="number">0</span>
    high <span class="operator">=</span> <span class="built-in">len</span>(lst) <span class="operator">-</span> <span class="number">1</span>

    <span class="keyword">while</span> low <span class="operator"><=</span> high:
        mid <span class="operator">=</span> (low <span class="operator">+</span> high) <span class="operator">//</span> <span class="number">2</span>

        <span class="keyword">if</span> lst[mid] <span class="operator">==</span> target:
            <span class="keyword">return</span> mid
        <span class="keyword">elif</span> lst[mid] <span class="operator">></span> target:
            high <span class="operator">=</span> mid <span class="operator">-</span> <span class="number">1</span>
        <span class="keyword">else</span>:
            low <span class="operator">=</span> mid <span class="operator">+</span> <span class="number">1</span>

    <span class="keyword">return</span> <span class="number">-1</span>

lst <span class="operator">=</span> [<span class="number">2</span>, <span class="number">3</span>, <span class="number">4</span>, <span class="number">10</span>, <span class="number">40</span>]
target <span class="operator">=</span> <span class="number">10</span>
<span class="built-in">print</span>(<span class="func">binary_search</span>(lst, target))`
        },
        {
            id: 'binary_search_rec',
            title: 'Binary Search (Recursive)',
            desc: 'חיפוש בינארי רקורסיבי. גם רץ בזמן O(log n) על מערך ממוין, מעביר אינדקסים או חותך מערכים.',
            icon: 'fa-solid fa-code-branch',
            iconClass: 'count', // Greenish
            returnTag: 'O(log n) זמן | O(log n) זכרון',
            tags: ['חיפוש', 'בינארי', 'רקורסיה'],
            code: `<span class="comment">## Binary Search (Recursive)</span>
<span class="keyword">def</span> <span class="func">binary_search_rec</span>(lst, target, low, high):
    <span class="keyword">if</span> low <span class="operator">></span> high:
        <span class="keyword">return</span> <span class="number">-1</span>

    mid <span class="operator">=</span> (low <span class="operator">+</span> high) <span class="operator">//</span> <span class="number">2</span>

    <span class="keyword">if</span> lst[mid] <span class="operator">==</span> target:
        <span class="keyword">return</span> mid
    <span class="keyword">elif</span> lst[mid] <span class="operator">></span> target:
        <span class="keyword">return</span> <span class="func">binary_search_rec</span>(lst, target, low, mid <span class="operator">-</span> <span class="number">1</span>)
    <span class="keyword">else</span>:
        <span class="keyword">return</span> <span class="func">binary_search_rec</span>(lst, target, mid <span class="operator">+</span> <span class="number">1</span>, high)

lst <span class="operator">=</span> [<span class="number">2</span>, <span class="number">3</span>, <span class="number">4</span>, <span class="number">10</span>, <span class="number">40</span>]
target <span class="operator">=</span> <span class="number">10</span>
<span class="built-in">print</span>(<span class="func">binary_search_rec</span>(lst, target, <span class="number">0</span>, <span class="built-in">len</span>(lst)<span class="operator">-</span><span class="number">1</span>))`
        }
    ];

    const searchPrepTabs = document.getElementById('search-prep-tabs');
    const searchPrepContent = document.getElementById('search-prep-content');

    if (searchPrepTabs && searchPrepContent) {
        // Build tabs
        searches.forEach((algo, i) => {
            const tab = document.createElement('button');
            tab.className = `exam-prep-tab ${i === 0 ? 'active' : ''}`;
            tab.setAttribute('data-algo', algo.id);
            tab.innerHTML = `<span class="tab-number">${i + 1}</span> ${algo.title}`;
            searchPrepTabs.appendChild(tab);
        });

        // Build content panels
        searches.forEach((algo, i) => {
            const panel = document.createElement('div');
            panel.className = `algorithm-panel ${i === 0 ? 'active' : ''}`;
            panel.setAttribute('data-algo', algo.id);

            const tagsHtml = algo.tags.map(t => `<span class="algo-tag">${t}</span>`).join('');

            panel.innerHTML = `
                <div class="algorithm-card">
                    <div class="algorithm-card-header">
                        <div class="algo-icon ${algo.iconClass}">
                            <i class="${algo.icon}"></i>
                        </div>
                        <div>
                            <h3>${algo.title}</h3>
                            <p>${algo.desc}</p>
                        </div>
                    </div>
                    <div class="algo-code-window">
                        <div class="window-header">
                            <span class="dot red"></span>
                            <span class="dot yellow"></span>
                            <span class="dot green"></span>
                            <span class="file-name">${algo.id}.py</span>
                        </div>
                        <pre><code>${algo.code}</code></pre>
                    </div>
                    <div class="algorithm-card-footer">
                        ${tagsHtml}
                        <span class="algo-tag return-type">${algo.returnTag}</span>
                    </div>
                </div>
            `;
            searchPrepContent.appendChild(panel);
        });

        // Tab switching
        searchPrepTabs.addEventListener('click', (e) => {
            const tab = e.target.closest('.exam-prep-tab');
            if (!tab) return;
            const algoId = tab.getAttribute('data-algo');

            searchPrepTabs.querySelectorAll('.exam-prep-tab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');

            searchPrepContent.querySelectorAll('.algorithm-panel').forEach(p => {
                p.classList.remove('active');
                if (p.getAttribute('data-algo') === algoId) {
                    p.classList.add('active');
                }
            });
        });
    }

    // 2. Intersection Observer for scroll animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, observerOptions);

    // Observe immediately, and after a short timeout to catch dynamically generated elements
    const observeElements = () => {
        const animObjects = document.querySelectorAll('.fade-in, .fade-in-up');
        animObjects.forEach(obj => observer.observe(obj));
    };

    // Add VS Code-style line numbers to all code blocks
    const addLineNumbers = () => {
        document.querySelectorAll('pre code').forEach(codeBlock => {
            if (codeBlock.querySelector('.code-line')) return; // already processed
            const html = codeBlock.innerHTML;
            const lines = html.split('\n');
            // Remove trailing empty line if present
            if (lines[lines.length - 1].trim() === '') lines.pop();

            codeBlock.innerHTML = lines.map((line, i) => {
                return `<span class="code-line"><span class="line-number">${i + 1}</span><span class="line-content">${line}</span></span>`;
            }).join('');
        });
    };

    addLineNumbers();

    observeElements();
    setTimeout(observeElements, 500);

    // 3. Smooth Scrolling for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });

                document.querySelectorAll('.nav-links a').forEach(a => a.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });

    // 4. Navbar background on scroll
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(11, 16, 30, 0.95)';
            navbar.style.boxShadow = '0 4px 20px rgba(0,0,0,0.5)';
        } else {
            navbar.style.background = 'rgba(11, 16, 30, 0.8)';
            navbar.style.boxShadow = 'none';
        }

        let current = '';
        const sections = document.querySelectorAll('section');
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        document.querySelectorAll('.nav-links a').forEach(a => {
            a.classList.remove('active');
            if (a.getAttribute('href') === `#${current}`) {
                a.classList.add('active');
            }
        });
    });

    // 5. Semester Selector interaction
    const semSelect = document.getElementById('semester-select');
    if (semSelect) {
        semSelect.addEventListener('change', (e) => {
            const semester = e.target.value;
            const root = document.documentElement;
            // Switch color themes slightly based on semester to feel interactive
            if (semester === 'winter') {
                root.style.setProperty('--acc-color', '#3b82f6');
                root.style.setProperty('--acc-hover', '#60a5fa');
            } else if (semester === 'spring') {
                root.style.setProperty('--acc-color', '#10b981');   // emerald
                root.style.setProperty('--acc-hover', '#34d399');
            } else if (semester === 'summer') {
                root.style.setProperty('--acc-color', '#f59e0b');   // amber
                root.style.setProperty('--acc-hover', '#fbbf24');
            }
        });
    }

    // Trigger initial appearance for elements above fold
    setTimeout(() => {
        const heroElems = document.querySelectorAll('.hero .fade-in, .hero .fade-in-up');
        heroElems.forEach(el => el.classList.add('visible'));
    }, 100);

    // 6. Auth and Payments Implementation
    const customGoogleBtn = document.getElementById('custom-google-signin');
    let tokenClient;

    if (typeof google !== 'undefined' && google.accounts && google.accounts.oauth2) {
        tokenClient = google.accounts.oauth2.initTokenClient({
            client_id: 'YOUR_GOOGLE_CLIENT_ID_HERE', // Update this client ID
            scope: 'email profile openid',
            callback: (tokenResponse) => {
                if (tokenResponse && tokenResponse.access_token) {
                    fetch('https://www.googleapis.com/oauth2/v3/userinfo', {
                        headers: { Authorization: `Bearer ${tokenResponse.access_token}` }
                    })
                        .then(res => res.json())
                        .then(profile => {
                            user = {
                                name: profile.name || "משתמש",
                                picture: profile.picture || "",
                                email: profile.email || ""
                            };
                            updateAuthUI();
                            console.log("User signed in:", user);
                        });
                }
            }
        });
    }

    if (customGoogleBtn) {
        customGoogleBtn.addEventListener('click', () => {
            if (tokenClient) {
                tokenClient.requestAccessToken();
            } else {
                // Fallback mock sign-in for local testing without valid Client ID
                user = {
                    name: "ישראל ישראלי",
                    picture: "https://lh3.googleusercontent.com/a/default-user=s96-c",
                    email: "student@campus.technion.ac.il"
                };
                updateAuthUI();
            }
        });
    }

    function updateAuthUI() {
        document.getElementById('auth-container').classList.add('hidden');
        document.getElementById('user-profile').classList.remove('hidden');
        document.getElementById('user-name').textContent = user.name;
        document.getElementById('user-avatar').src = user.picture;
    }

    const handlePremiumAccessRequest = () => {
        if (!user) {
            alert('כדי לרכוש גישת סמסטר (99 ש"ח), יש להתחבר קודם לחשבון גוגל.');
            if (customGoogleBtn) customGoogleBtn.click();
            return;
        }

        // Trigger Google Pay
        onGooglePayLoaded();
    };

    document.getElementById('btn-logout')?.addEventListener('click', () => {
        user = null;
        hasPaidSemesterAccess = false;
        document.getElementById('auth-container').classList.remove('hidden');
        document.getElementById('user-profile').classList.add('hidden');
        renderHomeworks(); // re-render to lock cards
    });

    // --- Google Pay Mock Flow ---
    const baseRequest = {
        apiVersion: 2,
        apiVersionMinor: 0
    };

    const tokenizationSpecification = {
        type: 'PAYMENT_GATEWAY',
        parameters: {
            'gateway': 'example',
            'gatewayMerchantId': 'exampleGatewayMerchantId'
        }
    };

    const allowedCardNetworks = ["AMEX", "DISCOVER", "INTERAC", "JCB", "MASTERCARD", "VISA"];
    const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];

    const baseCardPaymentMethod = {
        type: 'CARD',
        parameters: {
            allowedAuthMethods: allowedCardAuthMethods,
            allowedCardNetworks: allowedCardNetworks
        }
    };

    const cardPaymentMethod = Object.assign(
        {},
        baseCardPaymentMethod,
        { tokenizationSpecification: tokenizationSpecification }
    );

    let paymentsClient = null;

    function getGoogleIsReadyToPayRequest() {
        return Object.assign(
            {},
            baseRequest,
            { allowedPaymentMethods: [baseCardPaymentMethod] }
        );
    }

    function getGooglePaymentDataRequest() {
        const paymentDataRequest = Object.assign({}, baseRequest);
        paymentDataRequest.allowedPaymentMethods = [cardPaymentMethod];
        paymentDataRequest.transactionInfo = {
            totalPriceStatus: 'FINAL',
            totalPrice: '99.00',
            currencyCode: 'ILS',
            countryCode: 'IL'
        };
        paymentDataRequest.merchantInfo = {
            merchantName: 'Python Course 02340128',
            merchantId: '12345678901234567890'
        };
        return paymentDataRequest;
    }

    function onGooglePayLoaded() {
        paymentsClient = new google.payments.api.PaymentsClient({ environment: 'TEST' });
        const isReadyToPayRequest = getGoogleIsReadyToPayRequest();

        paymentsClient.isReadyToPay(isReadyToPayRequest)
            .then(function (response) {
                if (response.result) {
                    processPayment();
                } else {
                    alert('Google Pay אינו נתמך בדפדפן זה.');
                }
            })
            .catch(function (err) {
                console.error(err);
            });
    }

    function processPayment() {
        const paymentDataRequest = getGooglePaymentDataRequest();
        paymentsClient.loadPaymentData(paymentDataRequest)
            .then(function (paymentData) {
                // Success!
                console.log('Payment Approved', paymentData);
                hasPaidSemesterAccess = true;
                alert('התשלום בוצע בהצלחה! גישת סמסטר פרימיום הופעלה.');
                renderHomeworks(); // Re-render to unlock cards
            })
            .catch(function (err) {
                if (err.statusCode === 'CANCELED') {
                    console.log('Payment canceled');
                } else {
                    console.error('Payment error', err);
                    alert('אירעה שגיאה בתשלום. ניתן לנסות שנית.');
                }
            });
    }
});
