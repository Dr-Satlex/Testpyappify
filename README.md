# Piappify Test App

A minimal Kivy app for smoke-testing the [Piappify](https://piappify.streamlit.app/) build pipeline.

It's intentionally trivial: one screen, one label, one button that counts
taps. If Piappify successfully turns this repo into an installable APK,
the pipeline (workflow dispatch → Buildozer → artifact upload → Streamlit
download) is working end to end.

## Usage

1. Push this repo to GitHub as a **public** repository.
2. Open the Piappify app: https://piappify.streamlit.app/
3. Paste this repo's URL, e.g. `https://github.com/<your-username>/piappify-test-app`
4. Pick any app name (e.g. `Piappify Test`) and package name (e.g. `com.example.piappifytest`).
5. Trigger the build and watch the live log.

## Files

- `main.py` — the Kivy app itself
- `buildozer.spec` — build config (title/package fields get overwritten by
  Piappify's patch step regardless of what's here)
