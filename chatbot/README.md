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
