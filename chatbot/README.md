<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f7f3ea">
  <title>chatbot</title>
  <link rel="preconnect" href="https://script.google.com">
  <link rel="preconnect" href="https://cdn.jsdelivr.net">
  <script src="https://cdn.jsdelivr.net/npm/lucide@latest/dist/umd/lucide.min.js" defer></script>
  <style>
    :root {
      color-scheme: light;
      --paper: #f7f3ea;
      --surface: rgba(255, 255, 255, 0.78);
      --surface-strong: rgba(255, 255, 255, 0.94);
      --ink: #20201d;
      --muted: #69665f;
      --line: rgba(49, 45, 38, 0.11);
      --accent: #2c6f67;
      --accent-deep: #164d47;
      --warm: #c06f48;
      --shadow: 0 22px 70px rgba(45, 38, 27, 0.14);
      --radius-lg: 34px;
      --radius-md: 26px;
      --radius-sm: 18px;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC", "PingFang TC", "Microsoft JhengHei", sans-serif;
    }

    * {
      box-sizing: border-box;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background:
        radial-gradient(circle at 14% 12%, rgba(214, 148, 95, 0.20), transparent 32rem),
        radial-gradient(circle at 86% 10%, rgba(44, 111, 103, 0.18), transparent 30rem),
        linear-gradient(145deg, #f7f3ea 0%, #eef4ef 58%, #f9efe6 100%);
      color: var(--ink);
    }

    button,
    textarea {
      font: inherit;
    }

    button {
      border: 0;
      cursor: pointer;
    }

    .page {
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 28px;
    }

    .shell {
      width: min(1120px, 100%);
      height: min(860px, calc(100vh - 56px));
      min-height: 620px;
      display: grid;
      grid-template-rows: auto 1fr auto;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.72);
      border-radius: var(--radius-lg);
      background: linear-gradient(180deg, rgba(255, 255, 255, 0.82), rgba(255, 255, 255, 0.58));
      box-shadow: var(--shadow);
      backdrop-filter: blur(24px);
    }

    .topbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 18px;
      padding: 22px 24px 18px;
      border-bottom: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.58);
    }

    .identity {
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 0;
    }

    .avatar {
      width: 50px;
      height: 50px;
      display: grid;
      place-items: center;
      flex: 0 0 auto;
      border-radius: 20px;
      background: linear-gradient(135deg, var(--accent), #7b8e56);
      color: white;
      box-shadow: 0 12px 30px rgba(44, 111, 103, 0.24);
    }

    .avatar svg,
    .icon-button svg,
    .send-button svg {
      width: 21px;
      height: 21px;
      stroke-width: 2.15;
    }

    h1 {
      margin: 0;
      font-size: clamp(1.25rem, 2.4vw, 1.72rem);
      line-height: 1.1;
      letter-spacing: 0;
      font-weight: 800;
    }

    .subtitle {
      margin: 5px 0 0;
      color: var(--muted);
      font-size: 0.94rem;
      line-height: 1.5;
    }

    .status {
      display: flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      color: var(--accent-deep);
      font-size: 0.92rem;
      font-weight: 650;
      padding: 10px 14px;
      border-radius: 999px;
      background: rgba(44, 111, 103, 0.10);
    }

    .status::before {
      content: "";
      width: 9px;
      height: 9px;
      border-radius: 50%;
      background: #2f9f79;
      box-shadow: 0 0 0 5px rgba(47, 159, 121, 0.13);
    }

    .messages {
      min-height: 0;
      overflow-y: auto;
      padding: 26px;
      scroll-behavior: smooth;
    }

    .messages::-webkit-scrollbar {
      width: 10px;
    }

    .messages::-webkit-scrollbar-thumb {
      border: 3px solid transparent;
      border-radius: 99px;
      background: rgba(40, 39, 35, 0.22);
      background-clip: content-box;
    }

    .day-marker {
      width: fit-content;
      margin: 0 auto 20px;
      padding: 7px 13px;
      border: 1px solid var(--line);
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.58);
      color: var(--muted);
      font-size: 0.82rem;
      font-weight: 650;
    }

    .message-row {
      display: flex;
      margin: 14px 0;
    }

    .message-row.user {
      justify-content: flex-end;
    }

    .bubble-wrap {
      max-width: min(690px, 78%);
    }

    .message-row.user .bubble-wrap {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
    }

    .speaker {
      margin: 0 0 6px 4px;
      color: var(--muted);
      font-size: 0.78rem;
      font-weight: 750;
    }

    .bubble {
      padding: 15px 17px;
      border-radius: 24px;
      line-height: 1.72;
      white-space: pre-wrap;
      word-break: break-word;
      font-size: 1rem;
      box-shadow: 0 12px 28px rgba(45, 38, 27, 0.07);
    }

    .message-row.bot .bubble {
      border-top-left-radius: 10px;
      background: var(--surface-strong);
      border: 1px solid rgba(255, 255, 255, 0.92);
    }

    .message-row.user .bubble {
      border-top-right-radius: 10px;
      color: white;
      background: linear-gradient(135deg, var(--accent), var(--accent-deep));
    }

    .time {
      margin-top: 6px;
      color: var(--muted);
      font-size: 0.77rem;
    }

    .message-row.user .time {
      color: rgba(32, 32, 29, 0.54);
    }

    .composer {
      padding: 18px 22px 22px;
      border-top: 1px solid var(--line);
      background: rgba(255, 255, 255, 0.68);
    }

    .input-shell {
      display: grid;
      grid-template-columns: auto 1fr auto;
      align-items: end;
      gap: 12px;
      padding: 12px;
      border: 1px solid rgba(32, 32, 29, 0.11);
      border-radius: 30px;
      background: rgba(255, 255, 255, 0.86);
      box-shadow: 0 18px 44px rgba(45, 38, 27, 0.09);
    }

    textarea {
      width: 100%;
      max-height: 150px;
      min-height: 48px;
      resize: none;
      border: 0;
      outline: 0;
      padding: 13px 4px 10px;
      background: transparent;
      color: var(--ink);
      line-height: 1.55;
      font-size: 1rem;
    }

    textarea::placeholder {
      color: rgba(71, 68, 61, 0.58);
    }

    .icon-button,
    .send-button {
      width: 48px;
      height: 48px;
      display: grid;
      place-items: center;
      flex: 0 0 auto;
      border-radius: 19px;
      transition: transform 160ms ease, background 160ms ease, box-shadow 160ms ease;
    }

    .icon-button {
      color: var(--accent-deep);
      background: rgba(44, 111, 103, 0.10);
    }

    .icon-button:hover,
    .icon-button.listening {
      transform: translateY(-1px);
      background: rgba(192, 111, 72, 0.16);
      color: #8d4427;
    }

    .send-button {
      color: white;
      background: var(--ink);
      box-shadow: 0 13px 28px rgba(32, 32, 29, 0.24);
    }

    .send-button:hover {
      transform: translateY(-1px);
      background: #11110f;
    }

    .send-button:disabled,
    .icon-button:disabled {
      cursor: not-allowed;
      opacity: 0.48;
      transform: none;
      box-shadow: none;
    }

    .typing {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      min-width: 54px;
    }

    .typing span {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: rgba(44, 111, 103, 0.64);
      animation: pulse 1s infinite ease-in-out;
    }

    .typing span:nth-child(2) {
      animation-delay: 0.16s;
    }

    .typing span:nth-child(3) {
      animation-delay: 0.32s;
    }

    .notice {
      min-height: 22px;
      margin: 10px 16px 0;
      color: var(--muted);
      font-size: 0.84rem;
    }

    @keyframes pulse {
      0%, 80%, 100% {
        opacity: 0.35;
        transform: translateY(0);
      }
      40% {
        opacity: 1;
        transform: translateY(-4px);
      }
    }

    @media (max-width: 720px) {
      .page {
        padding: 0;
      }

      .shell {
        width: 100%;
        height: 100vh;
        min-height: 100vh;
        border-radius: 0;
        border: 0;
      }

      .topbar {
        align-items: flex-start;
        padding: 17px 17px 14px;
      }

      .avatar {
        width: 44px;
        height: 44px;
        border-radius: 17px;
      }

      .subtitle {
        display: none;
      }

      .status {
        padding: 8px 10px;
        font-size: 0.8rem;
      }

      .messages {
        padding: 18px 14px;
      }

      .bubble-wrap {
        max-width: 88%;
      }

      .composer {
        padding: 13px 12px 14px;
      }

      .input-shell {
        grid-template-columns: auto 1fr auto;
        border-radius: 25px;
        gap: 8px;
      }

      .icon-button,
      .send-button {
        width: 43px;
        height: 43px;
        border-radius: 16px;
      }
    }
  </style>
</head>
<body>
  <main class="page">
    <section class="shell" aria-label="chatbot 對話頁面">
      <header class="topbar">
        <div class="identity">
          <div class="avatar" aria-hidden="true"><i data-lucide="sparkles"></i></div>
          <div>
            <h1>chatbot</h1>
            <p class="subtitle">陪你整理情緒、理解世界，也一起把問題想清楚。</p>
          </div>
        </div>
        <div class="status" id="status">已連線</div>
      </header>

      <section class="messages" id="messages" aria-live="polite"></section>

      <form class="composer" id="chatForm">
        <div class="input-shell">
          <button class="icon-button" id="voiceButton" type="button" aria-label="語音輸入" title="語音輸入">
            <i data-lucide="mic"></i>
          </button>
          <textarea id="messageInput" rows="1" placeholder="輸入想聊的內容" aria-label="輸入訊息"></textarea>
          <button class="send-button" id="sendButton" type="submit" aria-label="送出訊息" title="送出訊息">
            <i data-lucide="send-horizontal"></i>
          </button>
        </div>
        <div class="notice" id="notice" role="status"></div>
      </form>
    </section>
  </main>

  <script>
    const GAS_ENDPOINT = "https://script.google.com/macros/s/AKfycby6U4Rs-FWcaQoHxlCDq8rc7MDYl-6MPzDg_NzudsPPZyA7_iYfrVxJ0MwbWtiLj3o06Q/exec";
    const MODEL = "gpt-5.4-mini";
    const STORAGE_KEY = "chatbot-session-id";

    const messagesEl = document.querySelector("#messages");
    const inputEl = document.querySelector("#messageInput");
    const formEl = document.querySelector("#chatForm");
    const sendButton = document.querySelector("#sendButton");
    const voiceButton = document.querySelector("#voiceButton");
    const noticeEl = document.querySelector("#notice");
    const statusEl = document.querySelector("#status");

    const sessionId = getSessionId();
    const conversation = [];
    let isSending = false;
    let recognition = null;
    let typingNode = null;

    window.addEventListener("DOMContentLoaded", () => {
      if (window.lucide) {
        window.lucide.createIcons();
      }

      addDayMarker(new Date());
      addMessage({
        role: "bot",
        text: "你好，我是 chatbot。你可以跟我談近況、問時事、討論學科問題，或只是把心裡的話放下來。我會好好接住，也會盡力給你清楚可靠的回應。",
        date: new Date()
      });
      setupSpeechRecognition();
      updateControls();
      inputEl.focus();
    });

    formEl.addEventListener("submit", async (event) => {
      event.preventDefault();
      await sendMessage();
    });

    inputEl.addEventListener("input", () => {
      autoResizeInput();
      sendButton.disabled = isSending || inputEl.value.trim().length === 0;
    });

    inputEl.addEventListener("keydown", async (event) => {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        await sendMessage();
      }
    });

    voiceButton.addEventListener("click", () => {
      if (!recognition) {
        setNotice("此瀏覽器目前不支援語音輸入。");
        return;
      }

      if (voiceButton.classList.contains("listening")) {
        recognition.stop();
      } else {
        setNotice("正在聆聽。");
        recognition.start();
      }
    });

    async function sendMessage() {
      const text = inputEl.value.trim();
      if (!text || isSending) return;

      isSending = true;
      updateControls();
      setStatus("回覆中");
      setNotice("");
      inputEl.value = "";
      autoResizeInput();

      const userMessage = { role: "user", text, date: new Date() };
      conversation.push(toHistoryItem(userMessage));
      addMessage(userMessage);
      showTyping();

      try {
        const reply = await requestReply(text);
        const botMessage = {
          role: "bot",
          text: normalizePlainText(reply),
          date: new Date()
        };
        conversation.push(toHistoryItem(botMessage));
        replaceTyping(botMessage);
        setStatus("已連線");
      } catch (error) {
        replaceTyping({
          role: "bot",
          text: "目前連線不太順利，請稍後再試一次。你的訊息沒有消失，可以重新送出。",
          date: new Date()
        });
        setStatus("待重試");
        setNotice("後台暫時無法回應。");
      } finally {
        isSending = false;
        updateControls();
        inputEl.focus();
      }
    }

    async function requestReply(message) {
      const payload = {
        message,
        model: MODEL,
        sessionId,
        page: "github-pages-chatbot",
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone || "Asia/Taipei",
        timestamp: new Date().toISOString(),
        history: conversation.slice(-16)
      };

      const response = await fetch(GAS_ENDPOINT, {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "text/plain;charset=utf-8" },
        body: JSON.stringify(payload)
      });

      const raw = await response.text();
      if (!response.ok) {
        throw new Error(raw || "Request failed");
      }

      return parseBackendReply(raw);
    }

    function parseBackendReply(raw) {
      if (!raw) return "我收到你的訊息了。";

      try {
        const data = JSON.parse(raw);
        return data.reply || data.message || data.text || data.answer || data.content || String(raw);
      } catch {
        return raw;
      }
    }

    function addDayMarker(date) {
      const marker = document.createElement("div");
      marker.className = "day-marker";
      marker.textContent = formatDate(date);
      messagesEl.appendChild(marker);
    }

    function addMessage(message) {
      const row = document.createElement("article");
      row.className = `message-row ${message.role === "user" ? "user" : "bot"}`;

      const wrap = document.createElement("div");
      wrap.className = "bubble-wrap";

      const speaker = document.createElement("div");
      speaker.className = "speaker";
      speaker.textContent = message.role === "user" ? "你" : "chatbot";

      const bubble = document.createElement("div");
      bubble.className = "bubble";
      bubble.textContent = message.text;

      const time = document.createElement("div");
      time.className = "time";
      time.textContent = formatDateTime(message.date);

      wrap.append(speaker, bubble, time);
      row.appendChild(wrap);
      messagesEl.appendChild(row);
      scrollToBottom();
      return row;
    }

    function showTyping() {
      const row = document.createElement("article");
      row.className = "message-row bot";
      row.innerHTML = `
        <div class="bubble-wrap">
          <div class="speaker">chatbot</div>
          <div class="bubble"><span class="typing"><span></span><span></span><span></span></span></div>
          <div class="time">${formatDateTime(new Date())}</div>
        </div>
      `;
      typingNode = row;
      messagesEl.appendChild(row);
      scrollToBottom();
    }

    function replaceTyping(message) {
      if (typingNode) {
        typingNode.remove();
        typingNode = null;
      }
      addMessage(message);
    }

    function setupSpeechRecognition() {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) {
        voiceButton.disabled = true;
        return;
      }

      recognition = new SpeechRecognition();
      recognition.lang = "zh-TW";
      recognition.interimResults = true;
      recognition.continuous = false;

      recognition.addEventListener("start", () => {
        voiceButton.classList.add("listening");
        voiceButton.setAttribute("aria-label", "停止語音輸入");
      });

      recognition.addEventListener("result", (event) => {
        let transcript = "";
        for (const result of event.results) {
          transcript += result[0].transcript;
        }
        inputEl.value = transcript.trim();
        autoResizeInput();
        updateControls();
      });

      recognition.addEventListener("end", () => {
        voiceButton.classList.remove("listening");
        voiceButton.setAttribute("aria-label", "語音輸入");
        setNotice(inputEl.value.trim() ? "" : "語音輸入已結束。");
      });

      recognition.addEventListener("error", () => {
        voiceButton.classList.remove("listening");
        setNotice("語音輸入暫時無法使用。");
      });
    }

    function normalizePlainText(value) {
      return String(value || "")
        .replace(/```[\s\S]*?```/g, (block) => block.replace(/```/g, ""))
        .replace(/[*_~`>#]/g, "")
        .replace(/\[(.*?)\]\((.*?)\)/g, "$1")
        .trim() || "我收到你的訊息了。";
    }

    function toHistoryItem(message) {
      return {
        role: message.role === "bot" ? "assistant" : "user",
        content: message.text,
        time: formatDateTime(message.date)
      };
    }

    function formatDate(date) {
      return new Intl.DateTimeFormat("zh-TW", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        weekday: "long"
      }).format(date);
    }

    function formatDateTime(date) {
      return new Intl.DateTimeFormat("zh-TW", {
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
      }).format(date);
    }

    function autoResizeInput() {
      inputEl.style.height = "auto";
      inputEl.style.height = `${Math.min(inputEl.scrollHeight, 150)}px`;
    }

    function scrollToBottom() {
      messagesEl.scrollTop = messagesEl.scrollHeight;
    }

    function setStatus(text) {
      statusEl.textContent = text;
    }

    function setNotice(text) {
      noticeEl.textContent = text;
    }

    function updateControls() {
      sendButton.disabled = isSending || inputEl.value.trim().length === 0;
      voiceButton.disabled = isSending || !recognition;
    }

    function getSessionId() {
      const existing = localStorage.getItem(STORAGE_KEY);
      if (existing) return existing;

      const next = crypto.randomUUID ? crypto.randomUUID() : `${Date.now()}-${Math.random().toString(16).slice(2)}`;
      localStorage.setItem(STORAGE_KEY, next);
      return next;
    }
  </script>
</body>
</html>
# chatbot

這是一個可部署到 GitHub Pages 的聊天機器人對話頁面。前端會把使用者訊息、模型名稱、sessionId、時間戳與近期對話紀錄送到已部署的 Google Apps Script 後台。

## 後台

- GAS endpoint: `https://script.google.com/macros/s/AKfycby6U4Rs-FWcaQoHxlCDq8rc7MDYl-6MPzDg_NzudsPPZyA7_iYfrVxJ0MwbWtiLj3o06Q/exec`
- Model: `gpt-5.4-mini`
- 前端預期後台回傳 JSON，例如 `{ "reply": "回覆內容" }`。若後台回傳純文字，也會直接顯示。

## 功能

- 使用者按 Enter 可直接送出，Shift + Enter 可換行。
- 支援瀏覽器 Web Speech API 語音輸入。
- 每則訊息顯示完整日期與 24 小時制時間。
- 對話內容以純文字呈現，不顯示 Markdown 標記。
- GAS 後台可將 payload 寫入指定 Google 試算表。
