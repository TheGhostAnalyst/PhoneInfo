# PhoneInfo

**Repo:** `PhoneInfo`
**Author:** TheGhostAnalyst

---

## 📌 Overview

`PhoneInfo` is a lightweight Python utility for parsing and gathering metadata about international phone numbers. It validates number formats, extracts country and national numbers, detects timezone(s), resolves a human-readable location, identifies the carrier, and classifies the number type (mobile, fixed-line, toll-free, etc.).

Built with `phonenumbers` (Google’s libphonenumber port for Python), this tool is focused on **rapid, offline-friendly reconnaissance** and developer-friendly output.

> **Disclaimer:** Use this tool only for lawful, ethical purposes (research, diagnostics, and testing with consent). Do not use it to invade privacy or commit abuse. The author assumes no responsibility for misuse.

---

## ✨ Features

* Validate international phone numbers (E.164-style input supported)
* Detect timezone(s) associated with the number
* Resolve human-readable location (country/region)
* Identify carrier/service provider (when available)
* Classify number type (Mobile, Fixed Line, Toll Free, VOIP, etc.)
* Append scan results to a local `Number_Scan.txt` logfile for offline review

---

## 🛠️ Requirements

* Python 3.8+ recommended
* `phonenumbers` library

Install dependency with pip:

```bash
pip install phonenumbers
```

---

## 🚀 Usage

1. Save the script as `phoneinfo.py` (or keep the repo file name).
2. Run the script and enter the number in international format (with `+` and country code). Example:

```bash
python3 phoneinfo.py
# Enter number to scan with country code (e.g., +2348012345678): +2348012345678
```

Sample output includes: country code, national number, timezone(s), location, service provider, validity, possibility check, and number type.

Results are also appended to `Number_Scan.txt` in the current working directory.

---

## 🔍 About the input format

The script expects input that matches a permissive international pattern, e.g. `+<countrycode><national>` with optional spacing/dashes. It uses `phonenumbers` parsing and validation under the hood, so unexpected formats may raise a parsing error.

---

## 🧩 Example (pseudo)

```
Enter number to scan with country code (e.g., +234XXXXXXXXXX): +2348012345678
🔎 Searching database...
Country Code: 234
National Number: 8012345678
Timezone: ('Africa/Lagos',)
Location: Nigeria
Service provider: MTN Nigeria
Is Valid Number: True
Is Possible Number: True
Number Type: Mobile
✅ Scan saved to Number_Scan.txt
```

---

## 📁 Output / Logging

Scans are appended to `Number_Scan.txt`. Each entry is separated by a line of `=` characters for easy parsing.

---

## 🧰 Development / Contribution

Contributions, improvements, and bug reports are welcome. If you want to contribute:

1. Fork the repo
2. Create a branch for your feature/fix
3. Submit a pull request with a clear description

Suggested improvements:

* Add CLI argument parsing (argparse) to allow batch processing and file input/output
* Add unit tests for input validation and output formatting
* Provide optional JSON output mode for automated pipelines

---

## ⚖️ License

This repo is released under the **MIT License** — see `LICENSE`.

---

## 🔗 Contact / Attribution

Handle: `TheGhostAnalyst`

If you found a bug or want to collaborate, open an issue or PR on this repo.

---

*Keep it ethical. Keep it quiet.*
