import json
from collections import Counter

level_counts = Counter()
module_counts = Counter()
error_counts = Counter()
slow_requests = 0
total_requests = 0
total_response_time = 0

with open("application.log", "r") as f:
    for line in f:
        total_requests += 1
        
        parts = line.strip().split(" ")

        if len(parts) < 5:
            continue
        
        level = parts[2]                    # INFO / WARNING / ERROR
        module = parts[3]                   # AUTH, DB, CACHE...
        
        # Extract response time
        try:
            response_part = line.split("response=")[1]
            response_time = int(response_part.split("ms")[0])
        except:
            response_time = 0

        level_counts[level] += 1
        module_counts[module] += 1
        total_response_time += response_time

        # Count ERROR messages
        if level == "ERROR":
            try:
                msg = line.split("msg=\"")[1].split("\"")[0]
                error_counts[msg] += 1
            except:
                pass

        # detect slow requests (> 2000ms)
        if response_time > 2000:
            slow_requests += 1

# Build summary
summary = {
    "total_logs": total_requests,
    "INFO": level_counts["INFO"],
    "WARNING": level_counts["WARNING"],
    "ERROR": level_counts["ERROR"],
    "error_rate_percent": round((level_counts['ERROR'] / total_requests) * 100, 2),
    "top_3_errors": error_counts.most_common(3),
    "top_3_modules": module_counts.most_common(3),
    "avg_response_time_ms": round(total_response_time / total_requests, 2),
    "slow_requests": slow_requests,
    "top_error": error_counts.most_common(1)[0][0] if error_counts else "None"
}

with open("summary.json", "w") as f:
    json.dump(summary, f, indent=4)

print("Advanced summary.json generated.")
