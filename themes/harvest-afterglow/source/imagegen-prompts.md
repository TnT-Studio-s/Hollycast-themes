<!-- Portions Copyright 2026 The Hollycast Authors -->
# Harvest Afterglow image generation

All five calls used the built-in image generation tool, not the API/CLI fallback.
The original landscape is retained by the generation tool; only the refined
landscape is shipped. The final four PNG assets are copied unchanged into
`assets/`. No post-generation image editing or alpha reconstruction was used.

## Landscape foundation

Output: `Original generation, superseded by the refinement below`

New image; no input reference.

```text
Use case: stylized-concept
Asset type: production background illustration for an importable Hollycast game-library theme named Harvest Afterglow.
Primary request: a wonderfully festive, sophisticated autumn and Thanksgiving illustrated interface backdrop, landscape 16:9, ideally 1920x1080 or larger. Full-bleed artwork, not a screenshot or device mockup.
Scene: a cozy Thanksgiving harvest supper on a walnut table beside the windows of a woodland lodge at dusk. Hand-painted storybook realism with exquisite carved wood, luminous amber candlelight, copper maple leaves, cranberry berries, wheat, tiny acorns, velvet pumpkins, a cornucopia of pears and apples, a delicious lattice pie and a steaming ceramic cider mug. A charming small decorative turkey with a fan of autumn feathers sits at the lower right. Outside the upper windows is an atmospheric copper-and-russet forest, a small warm harvest moon, and deep muted petrol twilight. Tiny warm lanterns and natural maple-leaf garlands at the upper edges. Premium detailed illustration, painterly material texture, pleasing visual hierarchy, magical but tasteful, neither cartoon clipart nor photorealistic clutter.
CRITICAL composition for real UI overlays: the main middle region from x=5% to 95%, y=23% to 85% must be very dark warm walnut/chestnut and largely quiet empty negative space. No large props, windows, candles or illustrations in that central region. The lower foreground feast forms an inviting richly detailed band in the bottom 12-15% only, larger at the extreme lower corners. Upper forest/window/garland imagery concentrated in the top 20%. Keep the left upper quarter darker for the theme title. Slim decorative side edges, with no intrusions into the main central space. No pre-drawn UI cards or fake game covers; runtime draws controls and content. The art should feel like a cohesive lavishly illustrated holiday poster around a generous empty center, not a simple gradient with clipart stickers.
Palette: deep chestnut brown #21150f and muted ink teal #112d2c, burnished copper #ba683a, cranberry #7d2e3d, golden pear #e6bd72, warm ivory #fff1d7. Delicate localized light, no white hotspots in the center.
Text: none. No words, lettering, labels, logo, watermark, black border, characters in costumes, Halloween objects, Christmas objects, or modern UI elements. Fill the whole image.
```

## Landscape refinement

Output: `assets/harvest-lodge.png`

The landscape foundation is the sole edit target.

```text
Use case: precise-object-edit
Asset type: final production background for Harvest Afterglow, an autumn Thanksgiving game-library theme.
Input image 1 is the edit target. Preserve exactly its landscape dimensions, hand-painted style, color, lighting, window architecture, forest, moon, upper garlands, lanterns, and central walnut material.
Change ONLY the lower feast band: shrink and lower all foreground holiday props so they sit entirely in the bottom 18 percent of the image. The turkey, velvet pumpkin, cornucopia, pie, cider mug, leaves and wheat must remain fully visible and detailed, with their highest points no higher than y=82% of the image. Keep their left-to-right arrangement and charming hand-painted details. Reduce their size naturally and extend the empty walnut area behind where their tops used to be. This is needed because the interactive library occupies y=24% to 79%. Everything between x=5% and 95%, y=24% and 79% must remain unobstructed walnut. The resulting still-life band should feel abundant, jewel-like and richly textured, not squashed. No text, UI, labels, additional props, watermark, or other changes.
```

## Portrait companion

Output: `assets/harvest-portrait.png`

The landscape foundation is the composition edit target and visual reference.

```text
Use case: stylized-concept
Asset type: portrait companion background for the Hollycast Harvest Afterglow theme.
Input image 1: visual reference and composition edit target: the existing landscape Thanksgiving woodland-lodge illustration.
Recompose this same world for a tall 2:3 portrait canvas. Preserve the hand-painted material realism, carved walnut, copper maple garlands, muted teal evening sky, little amber lanterns, harvest moon, cranberry velvet, pumpkins, lattice pie, cider, cornucopia and friendly decorative turkey. This must feel like the exact same premium coordinated theme.
CRITICAL usable UI region: keep x=7% to 93%, y=17% to 85% very dark, quiet, and empty walnut background for native game-library content. Top window and garland band occupies only the upper 14%; tall narrow decorated side borders occupy the extreme outer 5%; the rich feast occupies only the lower 12%, with the turkey small at lower right. Do not place a giant lantern, window, chair, pumpkin, or turkey in the central region. Favor delightful intricate corners and generous empty center. Full-bleed artwork.
No text, words, logos, UI, cards, buttons, interface labels, watermark, fake screenshots, Halloween or Christmas ornaments. Keep all scenery warm and Thanksgiving-specific.
```

## Maple leaf

Output: `assets/maple-leaf.png`

New image; transparent_background=true.

```text
Use case: stylized-concept
Asset type: a single isolated autumn maple leaf sprite for a premium illustrated Thanksgiving game-library theme.
Primary request: one beautifully hand-painted copper and amber maple leaf, with natural curved edges, delicate golden veins, a slightly curled pointed tip and fine stem, viewed mostly face-on at a gentle diagonal. Rich tactile illustration, elegant and readable at small sizes, soft painted highlights, warm russet shadow on the leaf itself. It belongs with carved walnut, golden lanterns and Thanksgiving harvest scenery.
Composition: exactly one leaf, fully visible and centered, occupying about 75% of a square image, clean empty space around the silhouette.
Background: genuinely transparent RGBA. Preserve fine serrated edges. No background color, scenery, square, checkerboard, text, watermark, labels, border, cast shadow or glow outside the leaf.
```

## Storybook fallback

Output: `assets/storybook-cover.png`

New image; no input reference.

```text
Use case: stylized-concept
Asset type: square cover-art placeholder for a polished Thanksgiving and autumn game-library theme called Harvest Afterglow.
Primary request: a beautiful vintage bound storybook cover seen perfectly straight on, square composition, dark oxblood and chestnut leather with delicately embossed brass-gold botanical border, tiny oak leaves and acorns at the corners, and a wonderfully detailed raised autumn maple leaf and small acorn medallion at the center. Subtle golden tooling, tactile handmade leather, muted copper, cranberry and candlelit ivory. Premium hand-painted illustration matching a cozy carved-walnut woodland lodge at Thanksgiving. Festive, charming and sophisticated. A small gilded star motif adds a sense of play. No scene or landscape behind the book. The cover surface fills the entire square; no perspective tilt.
Text: no text, lettering, numbers, logo, labels or watermark. No game screenshots, existing game IP, Halloween or Christmas imagery. No transparency; solid deep burgundy leather background.
```
