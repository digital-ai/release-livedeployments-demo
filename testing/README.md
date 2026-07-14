# Testing Framework

A single Python framework for spinning up the Live Deployments demo stack,
verifying that all containers and services are healthy, and (optionally)
running Playwright-based UI validation of the demo flow — all through one
entry point: `testing/run.py`.

It reuses the repo's existing `up.sh` / `down.sh` scripts (via subprocess)
rather than reimplementing them, so those remain the canonical way to
start/stop the stack.

It also automatically installs and test the `./cli setup`

## Setup

From the repo root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r testing/requirements.txt
playwright install --with-deps
```

### for cluster setup

Additionally, for cluster to work you will need to install the following:

- k3d
- kubectl
- docker with compose
- flux

## Usage

```bash
# Start the stack and wait for it to become healthy, then leave it running.
python testing/run.py

# Same, but also run the Playwright UI tests.
python testing/run.py --with-ui

# Tear the stack down again once done.
python testing/run.py --down

# Also run extra cluster setup of `./cli setup`.
python testing/run.py --cli-setup

# Stack already running? Skip straight to readiness checks / UI tests.
python testing/run.py --skip-up --with-ui

# Custom readiness timeout (seconds).
python testing/run.py --timeout 600

# Pass a custom Release/Deploy zip through to up.sh.
python testing/run.py --release-zip /path/to/release.zip --deploy-zip /path/to/deploy.zip
```

Run `python testing/run.py -h` for the full list of flags.

## Failure artifacts (screenshots)

`testing/ui/pytest.ini` enables `--screenshot=only-on-failure`, so a failed
test leaves a `.png` screenshot under
`testing/ui/test-results/<test-name>/test-failed.png` (gitignored).
Passing tests leave nothing behind.

Tests that use `authenticated_page` (the shared, logged-in-once session)
bypass pytest-playwright's built-in capture, since that only instruments
contexts created via its own `page`/`context` fixtures. `conftest.py`
implements the same on-failure screenshot capture for
`authenticated_page`-based tests instead.
