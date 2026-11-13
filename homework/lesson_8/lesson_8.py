# Задание 1
statuses = ["queued", "running", "testing", "deploy", "done"]
first, *middle, last = statuses
new_statuses = [*middle, *["failed", "skipped"]]
print(f"first: {first}, last: {last}, новый_список: {new_statuses}")


# Задание 2
browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}


def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


config = {**browser, **options}
result = start_session(**config)
print(f"{config}\n{result}")
