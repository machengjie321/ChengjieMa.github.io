import json
import os
import signal
from datetime import datetime

from scholarly import scholarly


def _timeout_handler(signum, frame):
    raise TimeoutError("Google Scholar fetch timed out")


def log(message):
    print(message, flush=True)


def main():
    scholar_id = os.environ["GOOGLE_SCHOLAR_ID"]
    timeout_seconds = int(os.environ.get("SCHOLAR_FETCH_TIMEOUT_SECONDS", "480"))

    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(timeout_seconds)

    try:
        log(f"[crawler] Fetching Scholar profile for user={scholar_id}")
        author = scholarly.search_author_id(scholar_id)
        log("[crawler] Filling profile basics, indices, counts, and publications")
        scholarly.fill(author, sections=["basics", "indices", "counts", "publications"])
        signal.alarm(0)
    except Exception as exc:
        signal.alarm(0)
        log(f"[crawler] Failed: {type(exc).__name__}: {exc}")
        raise

    author["updated"] = str(datetime.now())
    author["publications"] = {v["author_pub_id"]: v for v in author["publications"]}

    log(
        f"[crawler] Retrieved {len(author['publications'])} publications and "
        f"{author.get('citedby', 0)} citations"
    )

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": f"{author['citedby']}",
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)

    log("[crawler] Wrote results/gs_data.json and results/gs_data_shieldsio.json")


if __name__ == "__main__":
    main()
