import os
import requests

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def trigger_webhook(payload: dict):
    # ✅ HARD GUARD — PREVENT CRASH
    if not WEBHOOK_URL:
        print("⚠️ WEBHOOK_URL not set. Skipping webhook.")
        return

    try:
        print("📡 Webhook payload:", payload)
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except Exception as e:
        print("⚠️ Webhook failed:", e)
