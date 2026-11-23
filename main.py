import os

# Final count: 347 tabs. The draft's 47 is far too ordinary — anyone
# can have 47. 347 is the sharper, honest-comedic version of the same
# confession: high enough to be genuinely surprising, low enough to
# still be believable for a real tab hoarder, and oddly specific (that
# trailing 7) so it reads as counted just now, not rounded or invented
# for shock. The gate allows digits only (1-5 chars), so the number
# alone has to hint at the life behind it — and 347 does.
PARTS = ("3", "4", "7")


def entry_line():
    return "".join(PARTS)


def main():
    text = entry_line()
    assert text.isdigit(), "entry must be digits only"
    assert 1 <= len(text) <= 5, "entry must be 1 to 5 characters"
    assert text.strip() != "", "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
