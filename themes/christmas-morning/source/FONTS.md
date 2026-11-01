# Bundled serif fonts

Upstream: [Libre Baskerville, Google Fonts](https://github.com/google/fonts/tree/main/ofl/librebaskerville).
Downloaded 1 November 2026 from
`https://raw.githubusercontent.com/google/fonts/main/ofl/librebaskerville/LibreBaskerville%5Bwght%5D.ttf`.

The unchanged upstream variable font is retained at
`fonts/LibreBaskerville-variable.ttf`, SHA-256:
`05a95421961341c5b2556285e8415df9db27dab4f4abe22b446b3c6a8b916c5d`.

`prepare_fonts.py` instantiates weights 400 and 700 with FontTools, renames the
derivatives to **Hollycast Christmas Serif** to respect the reserved upstream
family name, and adds a small outline triangle at U+25B6 for the native Play
button. The font files remain licensed under the SIL Open Font License; the
complete upstream copyright and license are in
[../assets/OFL-LibreBaskerville.txt](../assets/OFL-LibreBaskerville.txt).

Rebuild with FontTools installed:

```sh
python3 source/prepare_fonts.py
```

The prebuilt regular and bold TTFs in `assets/` work without FontTools or a system
font installation. The theme does not download fonts at runtime.
