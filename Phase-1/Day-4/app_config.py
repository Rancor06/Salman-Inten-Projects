# app_config.py
# Task 2 -- App Config Lock (Tuple)
# Real-world use: fixed settings that must never change while the app is running.

APP_CONFIG = ("v1.0.3", "en", 30)  # (version, language, session_timeout_minutes)

version, language, session_timeout_minutes = APP_CONFIG

print(f"Version: {version}")
print(f"Language: {language}")
print(f"Session Timeout: {session_timeout_minutes} minutes")

# APP_CONFIG[0] = "v2.0.0"  # ❌ would crash -- tuples are immutable, items can't be reassigned