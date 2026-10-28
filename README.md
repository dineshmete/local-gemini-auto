# Local Gemini (Auto) 🚀

An automated multi-model intent router built for **Open WebUI** and powered by local **Ollama** weights. This project routes user prompts dynamically across different local model tiers (Lite, Standard, Reasoning) depending on the intent.

---

## 📂 Project Structure

* **`gemini_smart_router.py`** — The Python custom tool logic (**Gemini Smart Router**) that analyzes prompt intent and fires API requests to Ollama.
* **`gemini_auto_model.json`** — The exported Open WebUI model configuration (**gemini (Auto)**) containing system prompts and parameters.

---

## 🛠️ How to Import & Run on Your Wife's Laptop

### Step 1: Install Prerequisites
1. Ensure [Ollama](https://ollama.com) and [Open WebUI](https://docs.openwebui.com) are running on her laptop.
2. Download the required model weights via terminal:
   ```bash
   ollama pull gemma2:2b
   ollama pull gemma2:9b
   ollama pull deepseek-r1:7b