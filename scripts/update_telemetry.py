#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.github.com"
API_VERSION = "2022-11-28"
ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "telemetry.svg"


def github_get(path: str, token: str):
    url = f"{API}{path}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "RenoX23-profile-telemetry",
        },
    )

    last_error = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
            last_error = exc
            if attempt < 2:
                time.sleep(2 ** attempt)

    raise RuntimeError(f"GitHub API request failed: {url} :: {last_error}")


def get_metrics(username: str, token: str) -> dict[str, int]:
    encoded = urllib.parse.quote(username)
    user = github_get(f"/users/{encoded}", token)

    if not isinstance(user, dict):
        raise RuntimeError("Unexpected /users response")

    repos_count = int(user.get("public_repos", 0))
    followers = int(user.get("followers", 0))

    stars = 0
    page = 1

    while True:
        repos = github_get(
            f"/users/{encoded}/repos?per_page=100&page={page}&type=owner&sort=updated",
            token,
        )

        if not isinstance(repos, list) or not repos:
            break

        for repo in repos:
            if not repo.get("fork", False):
                stars += int(repo.get("stargazers_count", 0))

        if len(repos) < 100:
            break

        page += 1

    return {
        "repos": repos_count,
        "stars": stars,
        "followers": followers,
    }


def esc(value: object) -> str:
    return (
        str(value)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
        .replace("'", "&apos;")
    )


def bar_width(value: int, maximum: int, min_width: int = 140, max_width: int = 430) -> int:
    if maximum <= 0:
        return min_width
    ratio = min(1.0, max(0.0, value / maximum))
    return round(min_width + ratio * (max_width - min_width))


def render_svg(username: str, metrics: dict[str, int]) -> str:
    repos = metrics["repos"]
    stars = metrics["stars"]
    followers = metrics["followers"]

    open_source_width = bar_width(stars, max(stars, 25))
    public_data_width = bar_width(followers, max(followers, 25))
    ai_systems_width = bar_width(repos, max(repos, 50))
    username_lower = esc(username.lower())

    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="430" viewBox="0 0 1200 430">
  <defs>
    <style>
      .mono { font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace; }
      .body { font-size: 17px; fill: #e7edf2; }
      .label { font-size: 16px; font-weight: 700; fill: #e7edf2; }
      .muted { fill: #83919e; }
      .accent { fill: #39d6c0; }
    </style>
  </defs>

  <rect width="1200" height="430" rx="22" fill="#090d12"/>
  <rect x="2" y="2" width="1196" height="426" rx="22" fill="none" stroke="#233442" stroke-width="2"/>

  <rect x="20" y="20" width="1160" height="44" rx="10" fill="#141c25"/>
  <circle cx="42" cy="42" r="6" fill="#ff5f56"/>
  <circle cx="64" cy="42" r="6" fill="#ffbd2e"/>
  <circle cx="86" cy="42" r="6" fill="#27d16f"/>

  <text x="600" y="47" text-anchor="middle" class="mono muted" font-size="15">
    __USERNAME__@github: ~ — ./telemetry.sh
  </text>

  <text x="46" y="100" class="mono accent" font-size="17" font-weight="700">
    __USERNAME__:~$ ./telemetry.sh
  </text>

  <text x="46" y="146" class="mono label">PROFILE</text>
  <line x1="46" y1="162" x2="1090" y2="162" stroke="#233442" stroke-width="1"/>

  <text x="46" y="198" class="mono body">PUBLIC REPOS</text>
  <text x="310" y="198" class="mono body">__REPOS__</text>

  <text x="46" y="232" class="mono body">STARS</text>
  <text x="310" y="232" class="mono body">__STARS__</text>

  <text x="46" y="266" class="mono body">FOLLOWERS</text>
  <text x="310" y="266" class="mono body">__FOLLOWERS__</text>

  <text x="46" y="310" class="mono label">SHIPPED</text>
  <text x="1116" y="310" text-anchor="end" class="mono accent" font-size="24" font-weight="700">✓</text>

  <text x="46" y="344" class="mono body">OPEN-SOURCE TOOLS</text>
  <rect x="310" y="326" width="__OPEN_SOURCE_WIDTH__" height="22" rx="3" fill="#39d6c0"/>

  <text x="46" y="376" class="mono body">PUBLIC DATASETS</text>
  <rect x="310" y="358" width="__PUBLIC_DATA_WIDTH__" height="22" rx="3" fill="#28756f"/>

  <text x="46" y="408" class="mono body">AI SYSTEMS</text>
  <rect x="310" y="390" width="__AI_SYSTEMS_WIDTH__" height="22" rx="3" fill="#4a6f8e"/>

  <text x="800" y="348" class="mono label">CURRENT MODE</text>
  <text x="800" y="380" class="mono accent" font-size="18" font-weight="700">
    BUILD · SHIP · ITERATE
  </text>
</svg>"""

    replacements = {
        "__USERNAME__": username_lower,
        "__REPOS__": str(repos),
        "__STARS__": str(stars),
        "__FOLLOWERS__": str(followers),
        "__OPEN_SOURCE_WIDTH__": str(open_source_width),
        "__PUBLIC_DATA_WIDTH__": str(public_data_width),
        "__AI_SYSTEMS_WIDTH__": str(ai_systems_width),
    }

    for key, value in replacements.items():
        svg = svg.replace(key, value)

    return svg


def main() -> int:
    token = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME", "RenoX23")

    if not token:
        print("ERROR: GITHUB_TOKEN is missing.", file=sys.stderr)
        return 1

    try:
        print(f"Fetching GitHub telemetry for {username}...")
        metrics = get_metrics(username, token)
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(render_svg(username, metrics), encoding="utf-8")

        print(
            f"Telemetry updated successfully: repos={metrics['repos']}, "
            f"stars={metrics['stars']}, followers={metrics['followers']}"
        )
        return 0

    except Exception as exc:
        print(f"Telemetry generation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
