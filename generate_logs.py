import random
import datetime

levels = ["INFO", "INFO", "INFO", "WARNING", "ERROR"]  # INFO more common
modules = ["AUTH", "DB", "CACHE", "NETWORK", "API", "PAYMENTS"]
users = [f"user_{i}" for i in range(1, 50)]
ips = [f"192.168.1.{i}" for i in range(1, 50)]

messages = {
    "INFO": [
        "Request served successfully",
        "User authenticated",
        "Cache hit",
        "Fetched data",
        "Background job executed"
    ],
    "WARNING": [
        "High memory usage",
        "Slow response detected",
        "Cache miss",
        "Retrying connection",
        "Deprecated endpoint used"
    ],
    "ERROR": [
        "DB connection failed",
        "Timeout occurred",
        "Server crashed",
        "Null pointer exception",
        "Unexpected token in JSON",
        "Permission denied"
    ]
}

with open("application.log", "a") as f:
    for _ in range(500):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        level = random.choice(levels)
        module = random.choice(modules)
        user = random.choice(users)
        ip = random.choice(ips)
        message = random.choice(messages[level])
        response_time = random.randint(10, 5000)  # ms

        log_line = (
            f"{timestamp} {level} {module} user={user} ip={ip} "
            f"response={response_time}ms msg=\"{message}\""
        )

        f.write(log_line + "\n")

print("Logs appended to application.log")
