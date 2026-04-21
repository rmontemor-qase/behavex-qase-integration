# behavex-qase-integration

Sample project demonstrating the [Qase TestOps Behave reporter](https://github.com/qase-tms/qase-python/tree/main/qase-behave) running under both plain **Behave** and **BehaveX** (parallel execution).

It contains a tiny "system under test" (a calculator and an in-memory auth service) plus two Gherkin feature files tagged with `@qase.id`, `@qase.fields`, `@qase.suite` and `@qase.ignore` so you can see the whole spectrum of Qase metadata flowing into TestOps.

---

## Project layout

```
.
├── behave.ini                 # Behave defaults (skips @qase.ignore scenarios)
├── qase.config.json           # Qase reporter configuration
├── requirements.txt
├── .env.example               # Template for QASE_* environment variables
├── src/                       # System under test
│   ├── auth.py
│   └── calculator.py
└── features/
    ├── environment.py         # before/after_scenario hooks
    ├── authentication.feature
    ├── calculator.feature
    └── steps/
        ├── authentication_steps.py
        └── calculator_steps.py
```

---

## 1. Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Configure Qase

Create an API token at https://app.qase.io/user/api/token and grab your project **code** (visible in the URL: `app.qase.io/project/<CODE>`).

> **Never commit secrets.** This repo's `qase.config.json` ships with placeholder values. Real credentials live in a local `.env` file, which is gitignored.

```bash
cp .env.example .env
# edit .env and fill in QASE_TESTOPS_PROJECT and QASE_TESTOPS_API_TOKEN
set -a && source .env && set +a
```

Environment variables override `qase.config.json`, so the placeholders in the JSON file are simply ignored once your `.env` is loaded.

Make sure the test case IDs used in the feature files (`@qase.id:1` .. `@qase.id:7`) exist in your Qase project, or remove the tags so the reporter auto-creates them.

## 3. Run the suite

### a) Plain Behave (sequential)

```bash
behave --format=qase.behave.formatter:QaseFormatter
```

### b) BehaveX (parallel by scenario)

```bash
behavex --formatter=qase.behave.formatter:QaseFormatter --parallel-processes=4
```

### c) BehaveX (parallel by feature)

```bash
behavex --formatter=qase.behave.formatter:QaseFormatter \
        --parallel-processes=4 \
        --parallel-scheme=feature
```

### d) Offline (no network) — write a local JSON report only

```bash
QASE_MODE=report behave --format=qase.behave.formatter:QaseFormatter
# -> build/qase-report/*.json
```

---

## What the feature files demonstrate

| Tag                                              | Purpose                                                                   |
| ------------------------------------------------ | ------------------------------------------------------------------------- |
| `@qase.id:N`                                     | Link a scenario to an existing Qase test case                             |
| `@qase.suite:Name`                               | Group scenarios under a suite in TestOps                                  |
| `@qase.fields:{"severity":"...","priority":"..."}` | Attach custom fields (severity, priority, layer, …) — use `_` for spaces |
| `@qase.ignore`                                   | Skip reporting for a scenario (still runs unless filtered out)            |

`calculator.feature` also shows a **Scenario Outline** with a data table — each example row is reported as a separate test result in Qase.

---

## Notes on BehaveX mode

The upstream docs call out a couple of limitations when running under BehaveX:

- `qase.attach()` and `qase.comment()` are **not supported** in BehaveX mode.
- Everything else (test-case linking, metadata, steps, statuses, parallel reporting) works identically to plain Behave.

If you need attachments (e.g. screenshots on failure), run the suite with plain `behave`:

```python
from qase.behave import qase

@when("I take a screenshot")
def step_impl(context):
    png = context.browser.get_screenshot_as_png()
    qase.attach(content=png, file_name="screenshot.png", mime_type="image/png")
```

---

## Status mapping

| Behave result            | Qase status |
| ------------------------ | ----------- |
| Passed                   | passed      |
| Failed (AssertionError)  | failed      |
| Failed (other exception) | invalid     |
| Skipped                  | skipped     |

---

## Further reading

- [qase-behave README](https://github.com/qase-tms/qase-python/tree/main/qase-behave)
- [Full configuration reference (qase-python-commons)](https://github.com/qase-tms/qase-python/tree/main/qase-python-commons)
- [BehaveX](https://github.com/hrcorval/behavex)
