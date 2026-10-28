"""
title: Gemini Multi-Model Coder Router
author: Local AI Developer
description: Universal intent routing across local Ollama tiers optimized for code, math, and daily text inputs.
version: 5.1.0
"""

import json
import requests
from typing import Dict, Any


class Tools:
    def __init__(self):
        # Maps directly to your local Ollama port setup
        self.ollama_url = "http://localhost:11434/api/chat"
        self.lite_model = "gemma2:2b"
        self.standard_model = "gemma2:9b"
        self.reasoning_model = "deepseek-r1:7b"

    def run_smart_gemini_routing(self, __user_message__: str) -> str:
        """
        Natively reads customer text requests, maps intents across local Ollama tags,
        and prints responses directly into the active chat bubble.
        """
        query = __user_message__.lower().strip()
        words = query.split()

        # 1. Classify Customer Intent & Match Core Model
        reasoning_triggers = [
            "think step by step",
            "reasoning",
            "prove",
            "solve",
            "calculate",
            "math",
            "logic",
            "riddle",
            "why does",
        ]
        writing_triggers = [
            "write an email",
            "summarize",
            "creative writing",
            "translate",
            "draft",
            "hello",
            "greetings",
            "bullet points",
            "paraphrase",
        ]

        if any(trigger in query for trigger in reasoning_triggers):
            target_model = self.reasoning_model
            badge = "🎯 [DeepSeek-R1 7B - Premium Reasoning]"
        elif any(trigger in query for trigger in writing_triggers) or (
            len(words) < 6
            and not any(w in query for w in ["code", "run", "fix", "script"])
        ):
            target_model = self.lite_model
            badge = "⚡ [Gemma 2 2B - Flash-Lite]"
        else:
            target_model = self.standard_model
            badge = "💻 [Gemma 2 9B - Flash Standard]"

        # 2. Communicate Natively with the Ollama Backend Service
        payload = {
            "model": target_model,
            "messages": [{"role": "user", "content": __user_message__}],
            "stream": False,
        }

        try:
            response = requests.post(self.ollama_url, json=payload, timeout=90)
            response.raise_for_status()
            result_data = response.json()

            output_content = result_data.get("message", {}).get(
                "content", "Error: No text generated."
            )
            return f"{badge}\n\n{output_content}"

        except Exception as e:
            return (
                f"❌ Local Engine Connection Error targeting `{target_model}`: {str(e)}"
            )
