# Required Hollycast support

Theme format: **1**. The theme requires these shared renderer features:

- `layouts[].list.systemBadge`, `favouriteBadge`, `favouriteColor` and
  `selectOnHover` parsing and rendering.
- Keyboard and controller focus changes update the active list selection,
  artwork and metadata immediately when `selectOnHover` is false. A resting
  mouse pointer must not restore the old selection.
- The existing image `onSelection` timer and `tileSeconds` animation used by
  the 0.65-second TV retune effect.

The native validation build was macOS arm64
`ci-dev-41243457232-18-g01330d784`, based on commit
`01330d78428d1bd82a65d86dfce043d7e3789a6c` **plus the uncommitted Christmas
Morning shared list changes**. That commit or version label alone does not
identify a compatible build. The tested original executable SHA-256 is:

```text
d8f9b8b265782c52601a8086c418fb4f229742320446a0f867cac322d4e83f12
```

The app changes remain separate from this theme repository. Older parsers
reject the `list` field. There is no claim of compatibility with an older
release and no minimum-app-version field in the current catalogue. The listing
description repeats this dependency so it is visible before download.

Release this catalogue entry after the required app support is available to
users. Until then, the contribution is prepared for review and local testing.
