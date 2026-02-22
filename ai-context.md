# Python Course Website (02340128) - AI Context Documentation

This document contains a comprehensive architectural and technical overview of the Python Course Website (02340128) companion platform. It is designed to provide immediate context, understanding, and guidelines for any AI system or developer interacting with this codebase.

## 1. Project Overview
- **Purpose**: A visually stunning, RTL (Right-to-Left) companion website for the Technion's introductory Python course (02340128).
- **Technology Stack**: Pure Vanilla HTML, CSS, JavaScript (No frameworks like React or Tailwind).
- **Core Features**: 
  - Dynamic scroll animations (Intersection Observer).
  - Glassmorphism UI with a space/dark theme.
  - Semester-based accent color switching (Winter, Spring, Summer).
  - Google Sign-In (Google Identity Services API).
  - Google Pay Integration (Mocked premium locking system).
- **Language**: Hebrew (`lang="he"`, `dir="rtl"`). All text and layout are oriented Right-to-Left.

## 2. File Structure & Responsibilities

### `index.html`
- **Purpose**: Structure and content of the page.
- **Key Sections**:
  - `<nav>`: Sticky navigation bar containing the logo, anchors, semester selector, and Google Sign-In button/user profile.
  - `#home`: Hero section with animated background, course title, and a mockup code editor.
  - `#homework`: Placeholder list for HW cards (populated by JS). Cards 3-6 are "premium" locked.
  - `#exercises`: Timeline of course exercises.
  - `#theory`: Theory summaries and video links.
  - `#exams`: Information on course exams.
- **External Dependencies included**: 
  - FontAwesome (Icons).
  - Google Fonts (Assistant).
  - Google Identity Services (`https://accounts.google.com/gsi/client`).
  - Google Pay (`https://pay.google.com/gp/p/js/pay.js`).

### `styles.css`
- **Purpose**: Styling, theming, and layout.
- **Key Technical Details**:
  - **CSS Variables**: Core theme variables (colors, glass backgrounds) defined in `:root`. JavaScript manipulates `--acc-color` and `--acc-hover` for the semester themes.
  - **Glassmorphism**: Built using `backdrop-filter: blur(16px)` and semi-transparent borders.
  - **Animations**: Custom `@keyframes` (drift) for the floating background shapes, and `.fade-in` / `.fade-in-up` utility classes for scroll reveals.
  - **RTL Handeling**: Explicit use of `flex-direction`, padding, and transforms tailored for right-to-left. Example: `transform: translateX(-100px)` is used on `.hero-content` to push it visually leftwards.
  - **Premium System**: Utilizes `::before` pseudo-elements on `.premium-locked` cards to create the blurred mock-lock effect.

### `script.js`
- **Purpose**: DOM Manipulation, State, and APIs.
- **State Management**:
  - `user`: Holds the parsed profile object from Google Sign-In.
  - `hasPaidSemesterAccess`: Boolean flag tracking mock payment status.
- **Key Capabilities**:
  - **Dynamic Rendering**: `renderHomeworks()` generates the homework grid. It recalculates the lock state (hw0-hw2 open, hw3+ locked if not paid).
  - **Google Identity (OAuth)**: Uses `google.accounts.oauth2.initTokenClient` binding to the custom `#custom-google-signin` button. Has a fallback pseudo-login object if executed locally without a valid Client ID.
  - **Google Pay**: Fully written mock integration using `google.payments.api.PaymentsClient`. Triggers on locked HW clicks if logged in.
  - **Scroll Effects**: IntersectionObserver adds `.visible` classes to trigger CSS fades.

## 3. Modifying Guidelines for AI

1. **RTL Awareness**: Always consider that margins, paddings, and transforms act in reverse on the X-axis (`margin-right` pushes from the visual left side of the block).
2. **Vanilla Constraint**: Do not propose or output React components or Tailwind classes. Stick to modifying vanilla HTML nodes, `document.createElement`, and raw CSS selectors.
3. **Authentication Flows**:
   - The system is built around a custom Google button (`#custom-google-signin`).
   - If attempting to alter the lock system, ensure `renderHomeworks()` is called after state changes (`user` or `hasPaidSemesterAccess`).
4. **Theming**: When adding new elements, use the CSS variables like `var(--acc-color)` or `var(--glass-bg)` rather than hardcoding colors, as the semester dropdown completely changes the site's accent colors.
5. **Code Windows (VS Code-Style Line Numbers)**:
   - All `<pre><code>` blocks are post-processed by `addLineNumbers()` in `script.js` to inject line numbers.
   - Each line is wrapped: `<span class="code-line"><span class="line-number">N</span><span class="line-content">...</span></span>`.
   - **Critical rules to avoid visual bugs**:
     - Join lines with `''` (empty string), **never** `'\n'`. A `<pre>` tag preserves whitespace, so `'\n'` causes double-spacing.
     - Use `display: flex; flex-direction: column` on the `<code>` element so lines stack tightly with no gaps.
     - Use fixed `width` (not `min-width`) on `.line-number` so the gutter doesn't shift when line counts go from 1→2 digits.
     - The vertical gutter border must be `border-right` on `.line-number` (numbers LEFT of the line, code RIGHT).
     - `.line-number` must have `user-select: none` so numbers aren't copied when selecting code.
6. **Exam Prep Section (`#exam-prep`)**:
   - Contains 4 tabbed algorithm patterns generated dynamically in `script.js` from the `algorithms` array.
   - Tab switching uses event delegation on `.exam-prep-tabs` container.
   - Each algorithm has syntax-highlighted code using `<span>` classes: `.comment`, `.keyword`, `.func`, `.built-in`, `.number`, `.string`, `.operator`.
   - When adding new algorithm patterns, follow the existing object structure in the `algorithms` array (id, title, desc, icon, iconClass, returnTag, tags, code).
