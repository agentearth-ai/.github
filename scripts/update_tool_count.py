"""把 profile/README.md 里的工具数量更新为线上实时值。

数据来自 https://agentearth.ai/api/client/tools/statistics 的 data.tool_count，
按百位向下取整后加 "+"（与官网展示一致，例如 2465 -> 2,400+）。
只替换 <!--TOOL_COUNT_FORMATTED-->...<!--/TOOL_COUNT_FORMATTED--> 之间的内容。
"""
import json
import re
import sys
import urllib.request

API = "https://agentearth.ai/api/client/tools/statistics"
README = "profile/README.md"
MARKER = re.compile(r"(<!--TOOL_COUNT_FORMATTED-->)(.*?)(<!--/TOOL_COUNT_FORMATTED-->)")


def fetch_count() -> int:
    req = urllib.request.Request(API, headers={"User-Agent": "agentearth-ai-profile-updater"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    count = data["data"]["tool_count"]
    if not isinstance(count, int) or count < 100:
        raise ValueError(f"unexpected tool_count: {count!r}")
    return count


def main() -> int:
    count = fetch_count()
    label = f"{count // 100 * 100:,}+"
    with open(README, encoding="utf-8") as f:
        text = f.read()
    if not MARKER.search(text):
        print("no TOOL_COUNT marker found", file=sys.stderr)
        return 1
    updated = MARKER.sub(lambda m: m.group(1) + label + m.group(3), text)
    if updated != text:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(updated)
    print(f"tool_count={count} label={label} changed={updated != text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
