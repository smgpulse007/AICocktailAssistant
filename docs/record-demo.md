# UI recording

The README GIF uses screenshots from the running local Streamlit app in an
isolated Microsoft Edge browser. It shows an empty input, `Negroni` results, the
documented case-sensitive rejection for `negroni`, and the successful results
again. No generated UI, model response, external account, or user data is used.

To recreate it, follow the README start command, set a 1280 x 820 browser viewport,
and save those four states as `output/playwright/gif-01.png` through `gif-04.png`.
Press Enter after filling the text box and wait for the recommendation list or
unknown-name message before capturing each state. With Playwright CLI, resolve
the textbox from a fresh snapshot before using `fill` and `press Enter`.

Install Pillow into the development environment and run
`python scripts/assemble_demo.py`. The script preserves screenshot content and
records source/image hashes and dependency versions in `demo-recording.json`.
Playback pauses are adjusted for reading. Raw captures stay in ignored local
directories. The recorded recommendation order is illustrative: tied cosine
scores have no dedicated tie-breaking policy in the existing engine.

The local flow was checked with UTF-8 mode and Streamlit usage statistics disabled.
The repository's existing Streamlit Community Cloud hook may refresh the hosted
app after pushes; the local recording by itself does not verify hosted uptime.
