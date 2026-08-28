import os


KEY = "PYTHON_STUDY_GUIDE_MODE"
MISSING_KEY = "PYTHON_STUDY_GUIDE_MISSING"
previous_value = os.environ.get(KEY)
previous_missing = os.environ.pop(MISSING_KEY, None)

try:
    os.environ[KEY] = "practice"
    print(f"configured: {os.getenv(KEY)}")
    print(f"fallback: {os.getenv(MISSING_KEY, 'default')}")
finally:
    if previous_value is None:
        os.environ.pop(KEY, None)
    else:
        os.environ[KEY] = previous_value

    if previous_missing is not None:
        os.environ[MISSING_KEY] = previous_missing
