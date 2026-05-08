from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "index.html"


HTML = r"""<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>肥皂分子的兩面性 | 互動化學</title>
  <style>
    :root {
      --ink: #102027;
      --muted: #5a6872;
      --paper: #fffaf1;
      --panel: #ffffff;
      --line: #dbe7e4;
      --water: #2c9ab7;
      --water-soft: #d9f2f7;
      --tail: #f0a43a;
      --head: #2e7d64;
      --oil: #d95743;
      --violet: #6b5ac8;
      --shadow: 0 18px 50px rgba(16, 32, 39, 0.12);
    }

    * {
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      margin: 0;
      color: var(--ink);
      font-family: "Microsoft JhengHei", "PingFang TC", "Noto Sans TC", system-ui, sans-serif;
      background:
        linear-gradient(180deg, rgba(217, 242, 247, 0.92), rgba(255, 250, 241, 0.98) 48%, #f7fbf8);
      line-height: 1.6;
      letter-spacing: 0;
    }

    button,
    input,
    select {
      font: inherit;
    }

    .app-shell {
      min-height: 100vh;
    }

    .hero {
      min-height: 78vh;
      display: grid;
      grid-template-columns: minmax(0, 1.02fr) minmax(320px, 0.98fr);
      gap: clamp(24px, 5vw, 64px);
      align-items: center;
      padding: clamp(28px, 5vw, 64px);
      position: relative;
      overflow: hidden;
    }

    .hero::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        linear-gradient(120deg, rgba(255, 255, 255, 0.82), rgba(255, 255, 255, 0.16)),
        radial-gradient(circle at 86% 18%, rgba(44, 154, 183, 0.16), transparent 34%),
        radial-gradient(circle at 8% 88%, rgba(217, 87, 67, 0.11), transparent 32%);
      pointer-events: none;
    }

    .hero > * {
      position: relative;
      z-index: 1;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 16px;
      color: #23586b;
      font-weight: 800;
      letter-spacing: 0;
    }

    .eyebrow::before {
      content: "";
      width: 34px;
      height: 3px;
      border-radius: 999px;
      background: var(--oil);
    }

    h1 {
      max-width: 780px;
      margin: 0;
      font-size: clamp(42px, 7vw, 86px);
      line-height: 0.98;
      letter-spacing: 0;
    }

    .hero-copy {
      max-width: 720px;
      margin: 22px 0 0;
      color: #344651;
      font-size: clamp(18px, 2vw, 23px);
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 30px;
    }

    .button {
      border: 0;
      border-radius: 8px;
      padding: 12px 16px;
      color: #fff;
      background: var(--ink);
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 10px 26px rgba(16, 32, 39, 0.18);
      transition: transform 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      min-height: 46px;
    }

    .button:hover {
      transform: translateY(-2px);
      box-shadow: 0 14px 34px rgba(16, 32, 39, 0.22);
    }

    .button.secondary {
      color: var(--ink);
      background: rgba(255, 255, 255, 0.78);
      border: 1px solid rgba(16, 32, 39, 0.15);
      box-shadow: none;
    }

    .hero-visual {
      min-height: 430px;
      display: grid;
      place-items: center;
    }

    .molecule-stage {
      width: min(100%, 620px);
      aspect-ratio: 1.16;
      position: relative;
      border: 1px solid rgba(16, 32, 39, 0.11);
      border-radius: 8px;
      background:
        linear-gradient(180deg, rgba(255, 255, 255, 0.84), rgba(217, 242, 247, 0.56)),
        repeating-linear-gradient(135deg, rgba(44, 154, 183, 0.09) 0 2px, transparent 2px 18px);
      box-shadow: var(--shadow);
      overflow: hidden;
    }

    .waterline {
      position: absolute;
      inset: 56% 0 0;
      background: linear-gradient(180deg, rgba(44, 154, 183, 0.2), rgba(44, 154, 183, 0.5));
    }

    .oil-drop {
      position: absolute;
      left: 12%;
      top: 54%;
      width: 152px;
      aspect-ratio: 1;
      border-radius: 46% 54% 51% 49% / 42% 44% 56% 58%;
      background: linear-gradient(135deg, #ffb563, var(--oil));
      box-shadow: inset 16px 18px 28px rgba(255, 255, 255, 0.28), 0 16px 26px rgba(217, 87, 67, 0.2);
    }

    .big-molecule {
      position: absolute;
      left: 28%;
      top: 21%;
      width: 58%;
      height: 30%;
      transform: rotate(-8deg);
    }

    .tail-bond {
      position: absolute;
      left: 0;
      right: 172px;
      top: 50%;
      height: 12px;
      transform: translateY(-50%);
      border-radius: 99px;
      background: repeating-linear-gradient(90deg, var(--tail) 0 27px, #ffd28b 27px 36px);
      box-shadow: 0 7px 18px rgba(240, 164, 58, 0.28);
    }

    .carbon {
      position: absolute;
      top: 50%;
      width: 34px;
      height: 34px;
      transform: translateY(-50%);
      display: grid;
      place-items: center;
      border-radius: 50%;
      color: #5c3a00;
      background: #ffe3ad;
      border: 2px solid #e7941d;
      font-weight: 900;
      font-size: 14px;
    }

    .head-group {
      position: absolute;
      right: 0;
      top: 50%;
      width: 174px;
      transform: translateY(-50%);
      border-radius: 8px;
      padding: 14px 16px;
      color: #fff;
      background: linear-gradient(135deg, var(--head), #3fb495);
      box-shadow: 0 14px 28px rgba(46, 125, 100, 0.24);
      text-align: center;
      font-weight: 900;
    }

    .head-group small {
      display: block;
      font-size: 12px;
      opacity: 0.92;
      margin-top: 2px;
    }

    .formula-strip {
      position: absolute;
      left: 28px;
      right: 28px;
      bottom: 24px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
    }

    .formula-pill {
      min-width: 0;
      padding: 12px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.82);
      border: 1px solid rgba(16, 32, 39, 0.12);
    }

    .formula-pill b {
      display: block;
      font-size: 20px;
      line-height: 1.1;
    }

    .formula-pill span {
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
    }

    .sticky-tabs {
      position: sticky;
      top: 0;
      z-index: 20;
      display: flex;
      gap: 8px;
      overflow-x: auto;
      padding: 10px clamp(16px, 4vw, 44px);
      background: rgba(255, 250, 241, 0.92);
      backdrop-filter: blur(14px);
      border-block: 1px solid rgba(16, 32, 39, 0.1);
    }

    .tab-link {
      white-space: nowrap;
      min-height: 40px;
      padding: 9px 12px;
      border-radius: 8px;
      color: var(--ink);
      text-decoration: none;
      font-weight: 800;
      border: 1px solid transparent;
    }

    .tab-link:hover,
    .tab-link:focus-visible {
      background: #fff;
      border-color: var(--line);
      outline: none;
    }

    main {
      padding: 34px clamp(16px, 4vw, 44px) 70px;
    }

    .section {
      max-width: 1180px;
      margin: 0 auto 34px;
      padding-block: 28px;
    }

    .section h2 {
      margin: 0 0 10px;
      font-size: clamp(28px, 4vw, 44px);
      line-height: 1.1;
      letter-spacing: 0;
    }

    .section-lead {
      max-width: 820px;
      margin: 0 0 22px;
      color: var(--muted);
      font-size: 18px;
    }

    .grid {
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 18px;
    }

    .panel {
      grid-column: span 6;
      border-radius: 8px;
      background: var(--panel);
      border: 1px solid var(--line);
      box-shadow: 0 16px 42px rgba(16, 32, 39, 0.08);
      padding: clamp(18px, 3vw, 28px);
    }

    .panel.wide {
      grid-column: span 12;
    }

    .panel.third {
      grid-column: span 4;
    }

    .condition-detail {
      grid-column: span 8;
    }

    .panel h3 {
      margin: 0 0 12px;
      font-size: 22px;
      line-height: 1.2;
    }

    .select-row,
    .control-row {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 12px;
      margin: 12px 0 18px;
    }

    label {
      font-weight: 800;
      color: #263b44;
    }

    select,
    input[type="range"] {
      accent-color: var(--head);
    }

    select {
      min-height: 42px;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 8px 36px 8px 12px;
      background: #fff;
      color: var(--ink);
      font-weight: 700;
    }

    .formula-display {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 14px;
      align-items: center;
      margin-top: 14px;
      padding: 18px;
      border-radius: 8px;
      background: linear-gradient(135deg, #f6fffc, #fff7e8);
      border: 1px solid #d7e7df;
    }

    .formula-main {
      margin: 0;
      font-size: clamp(30px, 5vw, 50px);
      line-height: 1.05;
      font-weight: 900;
      overflow-wrap: anywhere;
    }

    sub,
    sup {
      line-height: 0;
    }

    .atom-count {
      display: grid;
      grid-template-columns: repeat(4, minmax(58px, 1fr));
      gap: 8px;
      min-width: 300px;
    }

    .atom {
      padding: 10px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid rgba(16, 32, 39, 0.12);
      text-align: center;
    }

    .atom b {
      display: block;
      font-size: 22px;
    }

    .atom span {
      color: var(--muted);
      font-size: 12px;
      font-weight: 800;
    }

    .split-formula {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
      margin-top: 16px;
    }

    .split-part {
      padding: 16px;
      border-radius: 8px;
      border: 1px solid var(--line);
      background: #fff;
    }

    .split-part strong {
      display: block;
      font-size: 24px;
      line-height: 1.15;
      overflow-wrap: anywhere;
    }

    .split-part.tail {
      border-color: rgba(240, 164, 58, 0.5);
      background: #fff8ec;
    }

    .split-part.head {
      border-color: rgba(46, 125, 100, 0.42);
      background: #f1fff9;
    }

    .split-part.ion {
      border-color: rgba(107, 90, 200, 0.35);
      background: #f6f3ff;
    }

    .molecule-lab {
      min-height: 290px;
      display: grid;
      align-items: center;
      overflow: hidden;
      border-radius: 8px;
      background:
        linear-gradient(180deg, #ffffff, #eef9fb);
      border: 1px solid var(--line);
      padding: 22px;
    }

    .soap-chain {
      position: relative;
      min-height: 142px;
      display: flex;
      align-items: center;
      gap: 0;
      transition: filter 0.18s ease;
    }

    .soap-chain.dim-tail .chain-dot,
    .soap-chain.dim-tail .zig {
      opacity: 0.18;
    }

    .soap-chain.dim-head .head-bubble,
    .soap-chain.dim-head .ion-bubble {
      opacity: 0.2;
    }

    .zig {
      width: min(46vw, 390px);
      height: 94px;
      background:
        linear-gradient(135deg, transparent 46%, var(--tail) 47% 54%, transparent 55%) 0 0 / 42px 42px,
        linear-gradient(45deg, transparent 46%, var(--tail) 47% 54%, transparent 55%) 21px 21px / 42px 42px;
      filter: drop-shadow(0 6px 6px rgba(240, 164, 58, 0.18));
      flex: 1 1 auto;
      min-width: 160px;
    }

    .chain-dot {
      width: 34px;
      height: 34px;
      flex: 0 0 34px;
      display: grid;
      place-items: center;
      border-radius: 50%;
      background: #ffe1a6;
      border: 2px solid #e5951b;
      font-weight: 900;
      color: #6f4300;
      margin-inline: -3px;
      z-index: 1;
      transition: opacity 0.18s ease, transform 0.18s ease;
    }

    .head-bubble,
    .ion-bubble {
      flex: 0 0 auto;
      display: grid;
      place-items: center;
      min-width: 82px;
      min-height: 74px;
      border-radius: 8px;
      color: #fff;
      font-weight: 900;
      text-align: center;
      transition: opacity 0.18s ease, transform 0.18s ease;
    }

    .head-bubble {
      background: var(--head);
      box-shadow: 0 10px 20px rgba(46, 125, 100, 0.22);
    }

    .ion-bubble {
      margin-left: 8px;
      background: var(--violet);
      box-shadow: 0 10px 20px rgba(107, 90, 200, 0.18);
    }

    .legend {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 18px;
    }

    .legend-item {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 8px 10px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.78);
      border: 1px solid var(--line);
      font-weight: 800;
      color: #37464d;
    }

    .swatch {
      width: 14px;
      height: 14px;
      border-radius: 4px;
      background: var(--head);
    }

    .swatch.tail {
      background: var(--tail);
    }

    .swatch.oil {
      background: var(--oil);
    }

    .segmented {
      display: inline-grid;
      grid-auto-flow: column;
      gap: 4px;
      padding: 4px;
      border-radius: 8px;
      background: #edf5f3;
      border: 1px solid var(--line);
    }

    .segmented button {
      border: 0;
      border-radius: 6px;
      padding: 8px 11px;
      background: transparent;
      font-weight: 900;
      cursor: pointer;
      color: #41525a;
    }

    .segmented button.active {
      color: #fff;
      background: var(--ink);
    }

    .canvas-wrap {
      position: relative;
      min-height: 420px;
      border-radius: 8px;
      background: linear-gradient(180deg, #e2f6fb, #bce5ef);
      border: 1px solid #b7dde5;
      overflow: hidden;
    }

    canvas {
      width: 100%;
      height: 420px;
      display: block;
    }

    .sim-status {
      position: absolute;
      left: 16px;
      right: 16px;
      bottom: 16px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }

    .status-chip {
      padding: 10px 12px;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid rgba(16, 32, 39, 0.1);
      font-weight: 800;
      min-width: 0;
    }

    .status-chip small {
      display: block;
      color: var(--muted);
      font-size: 12px;
      font-weight: 800;
    }

    .range-wrap {
      display: grid;
      grid-template-columns: 130px minmax(130px, 1fr) 44px;
      gap: 12px;
      align-items: center;
      width: min(100%, 560px);
    }

    input[type="range"] {
      width: 100%;
    }

    .reaction-board {
      display: grid;
      grid-template-columns: 1fr;
      gap: 12px;
    }

    .reaction {
      padding: 14px;
      border-radius: 8px;
      border: 1px solid var(--line);
      background: #fff;
    }

    .reaction .equation {
      display: block;
      margin-bottom: 6px;
      font-weight: 900;
      color: #20323b;
      overflow-wrap: anywhere;
    }

    .quiz {
      display: grid;
      gap: 16px;
    }

    .question {
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      padding: 16px;
    }

    .question p {
      margin: 0 0 12px;
      font-weight: 900;
      color: #263b44;
    }

    .choices {
      display: grid;
      gap: 8px;
    }

    .choice {
      text-align: left;
      border: 1px solid #d5e2df;
      border-radius: 8px;
      background: #f9fcfb;
      padding: 10px 12px;
      cursor: pointer;
      color: var(--ink);
    }

    .choice.correct {
      border-color: rgba(46, 125, 100, 0.55);
      background: #effff8;
    }

    .choice.wrong {
      border-color: rgba(217, 87, 67, 0.5);
      background: #fff2ee;
    }

    .feedback {
      min-height: 24px;
      margin-top: 8px;
      font-weight: 800;
    }

    .score-bar {
      height: 14px;
      border-radius: 8px;
      background: #e5ecea;
      overflow: hidden;
      margin-top: 14px;
    }

    .score-fill {
      width: 0%;
      height: 100%;
      background: linear-gradient(90deg, var(--head), var(--water));
      transition: width 0.28s ease;
    }

    .callout {
      border-left: 5px solid var(--oil);
      padding: 14px 16px;
      background: #fff8ef;
      border-radius: 0 8px 8px 0;
      color: #3b2b17;
      font-weight: 750;
    }

    footer {
      max-width: 1180px;
      margin: 0 auto;
      padding: 20px clamp(16px, 4vw, 44px) 42px;
      color: var(--muted);
      font-size: 14px;
    }

    @media (max-width: 930px) {
      .hero {
        grid-template-columns: 1fr;
        min-height: auto;
      }

      .hero-visual {
        min-height: 360px;
      }

      .molecule-stage {
        max-width: 620px;
      }

      .panel,
      .panel.third,
      .condition-detail {
        grid-column: span 12;
      }

      .formula-display,
      .split-formula {
        grid-template-columns: 1fr;
      }

      .atom-count {
        min-width: 0;
      }
    }

    @media (max-width: 620px) {
      .hero {
        padding: 24px 16px 30px;
      }

      .hero-actions,
      .select-row,
      .control-row {
        align-items: stretch;
        flex-direction: column;
      }

      .button,
      select {
        width: 100%;
      }

      .formula-strip {
        grid-template-columns: repeat(2, 1fr);
        left: 14px;
        right: 14px;
      }

      .big-molecule {
        left: 12%;
        width: 82%;
      }

      .tail-bond {
        right: 132px;
      }

      .head-group {
        width: 132px;
        font-size: 14px;
      }

      .range-wrap,
      .sim-status {
        grid-template-columns: 1fr;
      }

      .segmented {
        grid-auto-flow: row;
      }

      .soap-chain {
        transform: scale(0.86);
        transform-origin: left center;
      }
    }
  </style>
</head>
<body>
  <div class="app-shell">
    <section class="hero" id="top">
      <div>
        <p class="eyebrow">國中自然互動化學</p>
        <h1>肥皂分子的兩面性</h1>
        <p class="hero-copy">從 <strong>C<sub>17</sub>H<sub>35</sub>COONa</strong> 拆開看：長碳鏈尾端怕水愛油，羧酸鹽頭端愛水。真正清潔的關鍵不是把油直接溶進水裡，而是讓分子排成微胞，把油污包住帶走。</p>
        <div class="hero-actions">
          <a class="button" href="#formula">拆解化學式</a>
          <a class="button secondary" href="#micelle">操作微胞模擬</a>
        </div>
      </div>

      <div class="hero-visual" aria-label="肥皂分子示意圖">
        <div class="molecule-stage">
          <div class="waterline"></div>
          <div class="oil-drop"></div>
          <div class="big-molecule">
            <div class="tail-bond"></div>
            <span class="carbon" style="left: 2%">C</span>
            <span class="carbon" style="left: 15%">C</span>
            <span class="carbon" style="left: 28%">C</span>
            <span class="carbon" style="left: 41%">C</span>
            <span class="carbon" style="left: 54%">C</span>
            <div class="head-group">COO<sup>-</sup> Na<sup>+</sup><small>親水頭端</small></div>
          </div>
          <div class="formula-strip">
            <div class="formula-pill"><b>C<sub>17</sub>H<sub>35</sub></b><span>疏水碳氫尾</span></div>
            <div class="formula-pill"><b>COO<sup>-</sup></b><span>羧酸鹽頭</span></div>
            <div class="formula-pill"><b>Na<sup>+</sup></b><span>鈉離子</span></div>
            <div class="formula-pill"><b>微胞</b><span>包油分散</span></div>
          </div>
        </div>
      </div>
    </section>

    <nav class="sticky-tabs" aria-label="頁面區段">
      <a class="tab-link" href="#formula">化學式</a>
      <a class="tab-link" href="#molecule">分子頭尾</a>
      <a class="tab-link" href="#micelle">微胞模擬</a>
      <a class="tab-link" href="#conditions">水質與酸鹼</a>
      <a class="tab-link" href="#quiz">小測驗</a>
    </nav>

    <main>
      <section class="section" id="formula">
        <h2>把化學式拆成會說話的零件</h2>
        <p class="section-lead">同一個肥皂分子常有兩種寫法：<strong>C<sub>17</sub>H<sub>35</sub>COONa</strong> 強調「尾端 + 頭端 + 金屬離子」；<strong>C<sub>18</sub>H<sub>35</sub>NaO<sub>2</sub></strong> 則是把原子總數合併。</p>

        <div class="grid">
          <article class="panel wide">
            <div class="select-row">
              <label for="soapType">選一種常見肥皂鹽</label>
              <select id="soapType">
                <option value="stearate">硬脂酸鈉 Sodium stearate</option>
                <option value="palmitate">棕櫚酸鈉 Sodium palmitate</option>
                <option value="oleate">油酸鉀 Potassium oleate</option>
              </select>
            </div>
            <div class="formula-display">
              <p class="formula-main" id="formulaMain">C<sub>17</sub>H<sub>35</sub>COONa</p>
              <div class="atom-count" aria-label="原子數">
                <div class="atom"><b id="atomC">18</b><span>碳 C</span></div>
                <div class="atom"><b id="atomH">35</b><span>氫 H</span></div>
                <div class="atom"><b id="atomO">2</b><span>氧 O</span></div>
                <div class="atom"><b id="atomM">Na</b><span>金屬</span></div>
              </div>
            </div>
            <div class="split-formula">
              <div class="split-part tail">
                <strong id="tailPart">C<sub>17</sub>H<sub>35</sub></strong>
                <span>長碳氫鏈，非極性，容易靠近油脂。</span>
              </div>
              <div class="split-part head">
                <strong>COO<sup>-</sup></strong>
                <span>羧酸鹽，帶電，能和水分子互相吸引。</span>
              </div>
              <div class="split-part ion">
                <strong id="ionPart">Na<sup>+</sup></strong>
                <span>平衡負電荷；鈉皂較硬，鉀皂通常較軟。</span>
              </div>
            </div>
          </article>

          <article class="panel">
            <h3>碳鏈長度會改變性質</h3>
            <div class="range-wrap">
              <label for="tailLength">尾端碳數</label>
              <input id="tailLength" type="range" min="11" max="19" value="17">
              <strong id="tailLengthValue">17</strong>
            </div>
            <p id="chainInsight">C<sub>17</sub>H<sub>35</sub>COO<sup>-</sup> 的尾端夠長，親油性明顯，適合包住油污。</p>
            <div class="callout">易混淆點：肥皂不是單純讓油「變成水溶性」，而是用一端抓油、一端留在水中的排列方式，把油污分散成小顆粒。</div>
          </article>

          <article class="panel">
            <h3>一眼分辨兩種寫法</h3>
            <p><strong>結構式寫法：</strong><span id="structuralText">C17H35COONa</span></p>
            <p><strong>分子式寫法：</strong><span id="molecularText">C18H35NaO2</span></p>
            <p>前者保留學習線索，讓你看出「碳氫尾 + COO<sup>-</sup> + Na<sup>+</sup>」。後者適合統計原子種類與數量。</p>
          </article>
        </div>
      </section>

      <section class="section" id="molecule">
        <h2>點選頭端或尾端，看看分子怎麼站隊</h2>
        <p class="section-lead">水分子偏愛帶電或極性的部位；油脂偏愛非極性的碳氫鏈。肥皂分子同時擁有這兩種個性，因此能站在油和水的交界處。</p>

        <div class="grid">
          <article class="panel wide">
            <div class="control-row">
              <div class="segmented" role="group" aria-label="分子部位">
                <button class="active" data-focus="all">完整</button>
                <button data-focus="tail">疏水尾端</button>
                <button data-focus="head">親水頭端</button>
              </div>
              <span id="focusText">完整分子：尾端靠油，頭端朝水。</span>
            </div>
            <div class="molecule-lab">
              <div class="soap-chain" id="soapChain" aria-label="肥皂分子頭尾互動示意">
                <span class="chain-dot">C</span>
                <div class="zig"></div>
                <span class="chain-dot">C</span>
                <div class="head-bubble">COO<sup>-</sup></div>
                <div class="ion-bubble">Na<sup>+</sup></div>
              </div>
            </div>
            <div class="legend">
              <span class="legend-item"><span class="swatch tail"></span>疏水、親油</span>
              <span class="legend-item"><span class="swatch"></span>親水、帶電</span>
              <span class="legend-item"><span class="swatch oil"></span>油污</span>
            </div>
          </article>
        </div>
      </section>

      <section class="section" id="micelle">
        <h2>微胞模擬：把油污包住再帶走</h2>
        <p class="section-lead">調整肥皂量和攪動程度，觀察分子如何圍住油滴。尾端朝內接觸油，頭端朝外留在水裡，這就是清潔能發生的核心。</p>

        <div class="grid">
          <article class="panel wide">
            <div class="control-row">
              <div class="range-wrap">
                <label for="soapAmount">肥皂量</label>
                <input id="soapAmount" type="range" min="0" max="100" value="56">
                <strong id="soapAmountValue">56</strong>
              </div>
              <div class="range-wrap">
                <label for="scrubPower">攪動程度</label>
                <input id="scrubPower" type="range" min="0" max="100" value="42">
                <strong id="scrubPowerValue">42</strong>
              </div>
              <button class="button" id="pulseButton" type="button">攪動一次</button>
            </div>
            <div class="canvas-wrap">
              <canvas id="micelleCanvas" width="980" height="420" aria-label="肥皂微胞清潔模擬"></canvas>
              <div class="sim-status">
                <div class="status-chip"><small>油污狀態</small><span id="oilStatus">被部分包覆</span></div>
                <div class="status-chip"><small>分子排列</small><span id="micelleStatus">正在形成微胞</span></div>
                <div class="status-chip"><small>清潔提示</small><span id="cleanStatus">增加攪動可分散油滴</span></div>
              </div>
            </div>
          </article>
        </div>
      </section>

      <section class="section" id="conditions">
        <h2>水質與酸鹼會改變清潔力</h2>
        <p class="section-lead">同一個肥皂分子在不同環境中表現不同。硬水中的鈣鎂離子會讓肥皂形成沉澱；酸性環境會讓羧酸鹽變回脂肪酸。</p>

        <div class="grid">
          <article class="panel third">
            <h3>選擇水的情境</h3>
            <select id="conditionSelect" aria-label="水質情境">
              <option value="soft">一般水</option>
              <option value="hard">硬水：含 Ca2+ / Mg2+</option>
              <option value="acid">酸性：含較多 H+</option>
            </select>
            <p id="conditionSummary">肥皂分子可形成微胞，頭端留在水中，尾端包住油污。</p>
          </article>
          <article class="panel condition-detail">
            <h3>反應觀察</h3>
            <div class="reaction-board">
              <div class="reaction">
                <span class="equation" id="reactionEquation">RCOO<sup>-</sup> Na<sup>+</sup> → RCOO<sup>-</sup> + Na<sup>+</sup></span>
                <span id="reactionMeaning">肥皂在水中解離，帶電頭端能和水互動。</span>
              </div>
              <div class="reaction">
                <span class="equation" id="effectTitle">清潔力：穩定</span>
                <span id="effectMeaning">足夠肥皂分子會排列成微胞，油污被包覆後較容易沖走。</span>
              </div>
            </div>
          </article>
        </div>
      </section>

      <section class="section" id="quiz">
        <h2>三題檢查：你抓到關鍵了嗎？</h2>
        <p class="section-lead">點選答案後會立即回饋。答對越多，進度條越滿。</p>
        <div class="grid">
          <article class="panel wide">
            <div class="quiz" id="quizBox"></div>
            <div class="score-bar" aria-label="答題進度"><div class="score-fill" id="scoreFill"></div></div>
          </article>
        </div>
      </section>
    </main>

    <footer>
      內容重點：肥皂通常是高級脂肪酸鈉鹽或鉀鹽；以硬脂酸鈉為例，結構寫法 C17H35COONa，分子式 C18H35NaO2。
    </footer>
  </div>

  <script>
    const soaps = {
      stearate: {
        name: "硬脂酸鈉",
        formula: "C<sub>17</sub>H<sub>35</sub>COONa",
        structural: "C17H35COONa",
        molecular: "C18H35NaO2",
        tail: "C<sub>17</sub>H<sub>35</sub>",
        tailPlain: "C17H35",
        metal: "Na",
        metalHtml: "Na<sup>+</sup>",
        c: 18,
        h: 35,
        o: 2,
        unsat: false
      },
      palmitate: {
        name: "棕櫚酸鈉",
        formula: "C<sub>15</sub>H<sub>31</sub>COONa",
        structural: "C15H31COONa",
        molecular: "C16H31NaO2",
        tail: "C<sub>15</sub>H<sub>31</sub>",
        tailPlain: "C15H31",
        metal: "Na",
        metalHtml: "Na<sup>+</sup>",
        c: 16,
        h: 31,
        o: 2,
        unsat: false
      },
      oleate: {
        name: "油酸鉀",
        formula: "C<sub>17</sub>H<sub>33</sub>COOK",
        structural: "C17H33COOK",
        molecular: "C18H33KO2",
        tail: "C<sub>17</sub>H<sub>33</sub>",
        tailPlain: "C17H33",
        metal: "K",
        metalHtml: "K<sup>+</sup>",
        c: 18,
        h: 33,
        o: 2,
        unsat: true
      }
    };

    const formulaMain = document.querySelector("#formulaMain");
    const atomC = document.querySelector("#atomC");
    const atomH = document.querySelector("#atomH");
    const atomO = document.querySelector("#atomO");
    const atomM = document.querySelector("#atomM");
    const tailPart = document.querySelector("#tailPart");
    const ionPart = document.querySelector("#ionPart");
    const structuralText = document.querySelector("#structuralText");
    const molecularText = document.querySelector("#molecularText");

    function updateSoap(value) {
      const soap = soaps[value];
      formulaMain.innerHTML = soap.formula;
      atomC.textContent = soap.c;
      atomH.textContent = soap.h;
      atomO.textContent = soap.o;
      atomM.textContent = soap.metal;
      tailPart.innerHTML = soap.tail;
      ionPart.innerHTML = soap.metalHtml;
      structuralText.textContent = soap.structural;
      molecularText.textContent = soap.molecular;
    }

    document.querySelector("#soapType").addEventListener("change", (event) => updateSoap(event.target.value));

    const tailLength = document.querySelector("#tailLength");
    const tailLengthValue = document.querySelector("#tailLengthValue");
    const chainInsight = document.querySelector("#chainInsight");

    function updateTailLength() {
      const n = Number(tailLength.value);
      const h = 2 * n + 1;
      tailLengthValue.textContent = n;
      const totalC = n + 1;
      const behavior = n < 14
        ? "尾端較短，親油性較弱，形成微胞的能力較不明顯。"
        : n > 17
          ? "尾端很長，親油性強，但水中分散性可能下降。"
          : "尾端夠長，親油性明顯，適合包住油污。";
      chainInsight.innerHTML = `C<sub>${n}</sub>H<sub>${h}</sub>COO<sup>-</sup> 可合併成 C<sub>${totalC}</sub>H<sub>${h}</sub>O<sub>2</sub><sup>-</sup>。${behavior}`;
    }

    tailLength.addEventListener("input", updateTailLength);

    const focusButtons = document.querySelectorAll("[data-focus]");
    const soapChain = document.querySelector("#soapChain");
    const focusText = document.querySelector("#focusText");
    const focusCopy = {
      all: "完整分子：尾端靠油，頭端朝水。",
      tail: "疏水尾端：大多是 C 和 H，非極性，喜歡靠近油脂。",
      head: "親水頭端：COO- 帶電，容易和水分子互相吸引。"
    };

    focusButtons.forEach((button) => {
      button.addEventListener("click", () => {
        focusButtons.forEach((item) => item.classList.remove("active"));
        button.classList.add("active");
        const mode = button.dataset.focus;
        soapChain.classList.toggle("dim-tail", mode === "head");
        soapChain.classList.toggle("dim-head", mode === "tail");
        focusText.textContent = focusCopy[mode];
      });
    });

    const canvas = document.querySelector("#micelleCanvas");
    const ctx = canvas.getContext("2d");
    const soapAmount = document.querySelector("#soapAmount");
    const scrubPower = document.querySelector("#scrubPower");
    const soapAmountValue = document.querySelector("#soapAmountValue");
    const scrubPowerValue = document.querySelector("#scrubPowerValue");
    const oilStatus = document.querySelector("#oilStatus");
    const micelleStatus = document.querySelector("#micelleStatus");
    const cleanStatus = document.querySelector("#cleanStatus");
    let pulse = 0;
    let frame = 0;

    function moleculePoint(cx, cy, angle, distance, length) {
      const tailX = cx + Math.cos(angle) * (distance - length);
      const tailY = cy + Math.sin(angle) * (distance - length);
      const headX = cx + Math.cos(angle) * distance;
      const headY = cy + Math.sin(angle) * distance;
      return { tailX, tailY, headX, headY };
    }

    function drawMolecule(cx, cy, angle, distance, length, opacity) {
      const p = moleculePoint(cx, cy, angle, distance, length);
      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.lineWidth = 7;
      ctx.lineCap = "round";
      ctx.strokeStyle = "#f0a43a";
      ctx.beginPath();
      ctx.moveTo(p.tailX, p.tailY);
      ctx.lineTo(p.headX, p.headY);
      ctx.stroke();
      ctx.fillStyle = "#2e7d64";
      ctx.beginPath();
      ctx.arc(p.headX, p.headY, 9, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = "rgba(255,255,255,0.88)";
      ctx.font = "700 11px Microsoft JhengHei, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("-", p.headX, p.headY + 4);
      ctx.restore();
    }

    function drawFreeMolecule(index, total, soap, scrub) {
      const x = 80 + (index * 73) % 820;
      const y = 66 + ((index * 47) % 210);
      const wobble = Math.sin(frame / 22 + index) * (6 + scrub * 0.03);
      const angle = Math.sin(index * 1.7) * 0.8 + wobble * 0.02;
      drawMolecule(x + wobble, y, angle, 34, 42, Math.min(0.75, 0.25 + soap / 160));
    }

    function drawScene() {
      frame += 1;
      const soap = Number(soapAmount.value);
      const scrub = Number(scrubPower.value) + pulse;
      soapAmountValue.textContent = soap;
      scrubPowerValue.textContent = Number(scrubPower.value);

      const coverage = Math.min(1, (soap * 0.72 + scrub * 0.28) / 100);
      const cx = canvas.width * 0.55;
      const cy = canvas.height * 0.47;
      const oilRadius = 70 - coverage * 18 + Math.sin(frame / 20) * 2;
      const droplets = coverage > 0.78 ? 5 : coverage > 0.52 ? 3 : 1;

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const water = ctx.createLinearGradient(0, 0, 0, canvas.height);
      water.addColorStop(0, "#e5f8fc");
      water.addColorStop(1, "#9bd3e1");
      ctx.fillStyle = water;
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.strokeStyle = "rgba(44,154,183,0.28)";
      ctx.lineWidth = 2;
      for (let i = 0; i < 12; i += 1) {
        const y = 36 + i * 31 + Math.sin(frame / 18 + i) * 4;
        ctx.beginPath();
        for (let x = 0; x < canvas.width; x += 32) {
          const waveY = y + Math.sin(x / 70 + frame / 34 + i) * 5;
          if (x === 0) ctx.moveTo(x, waveY);
          else ctx.lineTo(x, waveY);
        }
        ctx.stroke();
      }

      for (let i = 0; i < droplets; i += 1) {
        const offset = droplets === 1 ? 0 : (i - (droplets - 1) / 2) * 76;
        const localRadius = droplets === 1 ? oilRadius : Math.max(23, oilRadius * (0.45 + i * 0.04));
        const dx = cx + offset + Math.sin(frame / 24 + i) * scrub * 0.06;
        const dy = cy + Math.cos(frame / 29 + i) * scrub * 0.04;
        const oil = ctx.createRadialGradient(dx - 18, dy - 18, 8, dx, dy, localRadius);
        oil.addColorStop(0, "#ffd58d");
        oil.addColorStop(1, "#d95743");
        ctx.fillStyle = oil;
        ctx.beginPath();
        ctx.arc(dx, dy, localRadius, 0, Math.PI * 2);
        ctx.fill();

        const count = Math.round(8 + coverage * 24);
        for (let j = 0; j < count; j += 1) {
          const angle = (Math.PI * 2 * j) / count + frame / 120;
          const show = j / count < coverage || coverage > 0.62;
          if (show) {
            drawMolecule(dx, dy, angle, localRadius + 29, 35, 0.95);
          }
        }
      }

      const freeCount = Math.max(4, Math.round(18 - coverage * 10));
      for (let i = 0; i < freeCount; i += 1) {
        drawFreeMolecule(i, freeCount, soap, scrub);
      }

      if (coverage < 0.35) {
        oilStatus.textContent = "油滴仍聚在一起";
        micelleStatus.textContent = "分子不足";
        cleanStatus.textContent = "增加肥皂量";
      } else if (coverage < 0.72) {
        oilStatus.textContent = "被部分包覆";
        micelleStatus.textContent = "正在形成微胞";
        cleanStatus.textContent = "增加攪動可分散油滴";
      } else {
        oilStatus.textContent = "油污被分散";
        micelleStatus.textContent = "微胞穩定";
        cleanStatus.textContent = "可被水流帶走";
      }

      pulse *= 0.94;
      requestAnimationFrame(drawScene);
    }

    document.querySelector("#pulseButton").addEventListener("click", () => {
      pulse = 56;
    });

    const conditionSelect = document.querySelector("#conditionSelect");
    const conditionSummary = document.querySelector("#conditionSummary");
    const reactionEquation = document.querySelector("#reactionEquation");
    const reactionMeaning = document.querySelector("#reactionMeaning");
    const effectTitle = document.querySelector("#effectTitle");
    const effectMeaning = document.querySelector("#effectMeaning");

    const conditionCopy = {
      soft: {
        summary: "肥皂分子可形成微胞，頭端留在水中，尾端包住油污。",
        equation: "RCOO<sup>-</sup> Na<sup>+</sup> → RCOO<sup>-</sup> + Na<sup>+</sup>",
        meaning: "肥皂在水中解離，帶電頭端能和水互動。",
        title: "清潔力：穩定",
        effect: "足夠肥皂分子會排列成微胞，油污被包覆後較容易沖走。"
      },
      hard: {
        summary: "鈣、鎂離子會抓住羧酸鹽頭端，形成不易溶的皂垢。",
        equation: "2 RCOO<sup>-</sup> + Ca<sup>2+</sup> → (RCOO)<sub>2</sub>Ca(s)",
        meaning: "肥皂分子被消耗，能形成微胞的分子變少。",
        title: "清潔力：下降",
        effect: "會看到泡沫少、皂垢多，常需要更多肥皂或改用合成清潔劑。"
      },
      acid: {
        summary: "酸中的 H+ 會讓 RCOO- 變回 RCOOH，親水性下降。",
        equation: "RCOO<sup>-</sup> + H<sup>+</sup> → RCOOH",
        meaning: "脂肪酸較不易溶於水，分子不容易穩定包覆油污。",
        title: "清潔力：變不穩",
        effect: "酸性太強時，肥皂的帶電頭端消失，乳化油污的能力下降。"
      }
    };

    conditionSelect.addEventListener("change", (event) => {
      const copy = conditionCopy[event.target.value];
      conditionSummary.textContent = copy.summary;
      reactionEquation.innerHTML = copy.equation;
      reactionMeaning.textContent = copy.meaning;
      effectTitle.textContent = copy.title;
      effectMeaning.textContent = copy.effect;
    });

    const questions = [
      {
        prompt: "C17H35COONa 中，哪一段最能代表疏水、親油的長尾端？",
        choices: ["C17H35", "COO-", "Na+"],
        answer: 0,
        feedback: "對。C 和 H 組成的長碳氫鏈大多非極性，因此偏親油。"
      },
      {
        prompt: "肥皂清潔油污時，最精準的說法是什麼？",
        choices: ["肥皂讓油直接溶解在水中", "肥皂形成微胞把油污包住並分散", "肥皂把水變成油"],
        answer: 1,
        feedback: "正確。尾端朝油、頭端朝水的微胞排列，讓油污能被水流帶走。"
      },
      {
        prompt: "硬水為什麼會讓肥皂比較不好用？",
        choices: ["Ca2+ 或 Mg2+ 會形成不易溶的皂垢", "水分子會分解成氫氣", "碳鏈會全部變成氧氣"],
        answer: 0,
        feedback: "沒錯。鈣鎂離子會和 RCOO- 結合，消耗肥皂並形成沉澱。"
      }
    ];

    const quizBox = document.querySelector("#quizBox");
    const scoreFill = document.querySelector("#scoreFill");
    const answered = new Map();

    function updateScore() {
      const correct = [...answered.values()].filter(Boolean).length;
      scoreFill.style.width = `${(correct / questions.length) * 100}%`;
    }

    function renderQuiz() {
      questions.forEach((question, index) => {
        const wrapper = document.createElement("div");
        wrapper.className = "question";
        const prompt = document.createElement("p");
        prompt.textContent = `${index + 1}. ${question.prompt}`;
        const choices = document.createElement("div");
        choices.className = "choices";
        const feedback = document.createElement("div");
        feedback.className = "feedback";

        question.choices.forEach((choice, choiceIndex) => {
          const button = document.createElement("button");
          button.className = "choice";
          button.type = "button";
          button.textContent = choice;
          button.addEventListener("click", () => {
            choices.querySelectorAll("button").forEach((item) => {
              item.classList.remove("correct", "wrong");
            });
            const isCorrect = choiceIndex === question.answer;
            button.classList.add(isCorrect ? "correct" : "wrong");
            if (!isCorrect) {
              choices.children[question.answer].classList.add("correct");
            }
            feedback.textContent = isCorrect ? question.feedback : `再想一下。${question.feedback}`;
            feedback.style.color = isCorrect ? "#2e7d64" : "#a6402f";
            answered.set(index, isCorrect);
            updateScore();
          });
          choices.appendChild(button);
        });

        wrapper.appendChild(prompt);
        wrapper.appendChild(choices);
        wrapper.appendChild(feedback);
        quizBox.appendChild(wrapper);
      });
    }

    updateSoap("stearate");
    updateTailLength();
    renderQuiz();
    drawScene();
  </script>
</body>
</html>
"""


def main() -> None:
    OUTPUT.write_text(HTML, encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
