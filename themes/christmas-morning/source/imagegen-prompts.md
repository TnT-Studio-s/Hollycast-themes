# Christmas Morning imagegen sources

The four illustrated production PNGs were generated with the built-in `image_gen` tool. Their final PNG pixels and alpha channels are retained unchanged. The landscape image is the style reference for the portrait composition; the full concept is the reference for the decorative heading and toolbar logo. No game art or live controls are baked into these assets. The CRT effect textures are separate procedural assets authored by `generate_crt.py`, with no image inputs.

## Landscape: `assets/christmas-room.png`

```text
Use case: stylized-concept
Asset type: production background skin for the Hollycast game-library UI, landscape 16:9, 1920x1080.
Primary request: Create an exquisite Christmas morning late-1990s console-gaming living room, tactile miniature diorama / premium stop-motion set photographed straight on. This is an actual interface background asset; the interactive game list and all typography will be drawn by the application.
Scene: midnight forest-green painted room, warm amber Christmas lights, a beautiful softly glowing Christmas tree at the extreme right, ruby and cream wrapped presents along the bottom right, faint snow outside a small window high in the right background, walnut cabinet. A small off-white late-1990s disc console and wired controller rest on the lower-right cabinet. Charming, sophisticated nostalgic holiday atmosphere, realistic felt, wood, satin ribbon, molded plastic and brass textures, soft grain.
Composition constraints that are essential for the application:
- The entire LEFT 44 percent of the canvas must be quiet, very dark forest green wall with extremely subtle texture, no objects or lettering there. This is negative space for a live list. Keep the central area of that left wall unobstructed from y=0.22 through y=0.88.
- At RIGHT CENTER place a large cream rounded CRT television viewed exactly straight on, no perspective on the front. Its outer body spans approximately x=0.49 to x=0.86 and y=0.19 to y=0.69. Its screen is a flat near-black rectangle, approximately x=0.525 to x=0.825 and y=0.245 to y=0.625, unobstructed, with only subtle glass texture. The screen MUST be empty. No pictures, UI, symbols or reflection objects on the screen. The app places a real cover in this region.
- The tree occupies the rightmost strip x=0.87 to 1, framing the CRT without covering its screen. Garland with small warm-white bulbs runs along the TOP EDGE only.
- Leave a quiet dark green horizontal area below the CRT between x=0.50 and x=0.85 and y=0.72 to y=0.97 for live metadata and native Play controls.
- A subtle warm light falloff and vignette visually unify the dark left wall and the dimensional festive set at right. The scene should fill the whole canvas edge to edge.
Color palette: deep spruce #102c25, warm ivory #fff3d7, cranberry #b63a42, muted brass #d9b777, amber lights.
Lighting/mood: cosy Christmas anticipation, warm miniature practical lighting, carefully controlled highlights, excellent rich shadow detail.
Text: none. Do not bake any text, UI, menus, game cover art, placeholder graphics, borders around the whole image, logos or watermarks into this asset. Do not include people. Output a single landscape background.
```

## Portrait: `assets/christmas-room-portrait.png`

```text
Use case: stylized-concept
Asset type: production PORTRAIT 2:3 background skin for Hollycast's Christmas Morning interactive game-library theme, 1024x1536.
Input image 1: style and material reference ONLY, the landscape background of the same theme. Create a new portrait composition of that same warm Christmas room.
Primary request: a beautifully art-directed miniature late-1990s Christmas console gaming room at the TOP of a portrait game-library screen; the LOWER HALF is deliberate empty deep forest-green textured negative space for the application's native list and controls.
Keep the reference's premium tactile photographic miniature aesthetic, dark spruce wall, amber fairy lights, ivory CRT television, walnut cabinet, tiny off-white disc console/controller, cranberry and cream gift wrap, tree ornaments and rich soft shadows.
Composition is crucial:
- Portrait 2:3, edge-to-edge with no outer border.
- A thin evergreen garland with warm tiny lights at the very top edge.
- A straight-on ivory CRT television occupies x=0.13 to 0.78 and y=0.13 to 0.41. Screen is a blank near-black rectangle approximately x=0.19 to 0.70 and y=0.17 to 0.36, unobstructed with no image or writing. All screen content will be native application UI.
- Tiny decorated Christmas tree down the right edge of this TOP vignette, a few gifts at the base; a console on the small cabinet under the TV. Keep this vignette within y=0.08 to 0.46.
- From y=0.48 all the way to y=1, the entire canvas is extremely quiet dark spruce-green, with a very subtle premium felt/paper texture and soft edge vignette. NO OBJECTS, furniture, floorboards, presents, ornaments or bright lights in this LOWER HALF. The transition from room vignette to quiet lower green area is artistically seamless and deliberately designed as a software backdrop.
- Leave the top y=0.04 to 0.11 mostly dark for a live one-line theme heading.
Palette: #102c25 deep green, #fff3d7 ivory, #b63a42 cranberry and #d9b777 brass.
Text: none. No typography, no logos, no menu, no controls, no baked-in game artwork, no watermarks, no people. This must be a usable production background with an empty television and empty lower half, not a complete fake application screenshot.
```


## Decorative heading: `assets/christmas-title.png`

The complete Christmas Morning concept is a visual reference. The first generation extracts only the static title and holly; the targeted edit flattens the lettering. Final PNG alpha is preserved unchanged.

```text
Use case: background-extraction
Asset type: transparent PNG decorative title lockup for the Hollycast Christmas Morning game-library theme.
Input image 1 is the exact style and design reference. Recreate ONLY its upper-left title lockup, with transparent alpha everywhere else.
Include the small uppercase brass-gold "C H R I S T M A S   E D I T I O N" eyebrow and its thin ornamental horizontal rules above the two-line large warm-ivory serif title. Exact title text: "Christmas" on line 1 and "Morning" on line 2. Match the reference's elegant very bold old-style serif lettering, tight optical line spacing and warm ivory color #fff0cf. The word Christmas is slightly wider than Morning. A small pair of dark green holly leaves with three glossy red berries sits just to the right of the end of Morning, exactly as in the reference. Keep it restrained and sharp, with no extra ornament.
Composition: wide rectangular tightly framed title asset, approximately 2.6:1 width-to-height. Small consistent transparent margin. All lettering and holly must be fully within the image, absolutely no clipping. Preserve the reference's arrangement, typography, letter shapes, proportions and colors as closely as possible. Production quality edges at high resolution.
Remove the room, background, toolbar, game list, game artwork, TV, metadata and all controls entirely. Background MUST be genuine transparent alpha, not a dark-green rectangle or a drawn checkerboard. No extra text or watermark. This asset contains only the eyebrow/rules, title, and its small holly sprig.
```

Final edit:

```text
Use case: precise-object-edit
Edit target: input image 1, the transparent Christmas Morning title lockup.
Primary request: change ONLY the lettering treatment. Remove ALL gold outlines, beveled edges, 3D extrusion, metallic shading, highlights, gradients, white glows and drop shadows. The title "Christmas" / "Morning" must be perfectly FLAT solid warm ivory #fff0cf, like printed book typography. The small CHRISTMAS EDITION eyebrow and rules must be perfectly FLAT solid muted brass #d9b777 with no outlines or depth.
Keep the exact wording, letter shapes, two-line layout, dimensions, transparent background and holly sprig placement. Keep the holly leaves/berries illustrated naturally. Preserve true alpha everywhere outside letters/rules/holly. No new objects, text, background or margin. It is minimalist flat typographic graphic design; absolutely no metallic or embossed lettering.
```

## Toolbar branding: `assets/hollycast-christmas.png`

The concept is a visual reference. Extract the static logo, then flatten its lettering. No live application controls are part of the PNG.

```text
Use case: background-extraction
Asset type: transparent PNG toolbar logo for Hollycast's Christmas Morning library theme.
Input image 1 is the exact visual reference. Recreate ONLY the logo in the TOP-LEFT toolbar: the exact word "Hollycast" in refined warm ivory bold old-style serif type with the small green holly leaves and glossy red berries immediately to its left. Match the reference lettering, palette and proportions. Word spelled H-o-l-l-y-c-a-s-t. This is a horizontal logo lockup about 5:1 width-to-height, tightly framed with a small transparent safety margin.
Remove the complete rest of the interface and background. Genuine transparent alpha everywhere around the logo. No colored rectangle, no checkerboard drawing, no extra text, no watermark. Crisp production-ready edges suitable for a native application toolbar.
```

Final edit:

```text
Use case: precise-object-edit
Edit target: input image 1, the transparent Hollycast logo.
Primary request: change ONLY the lettering treatment. Remove ALL gold outlines, bevels, 3D extrusion, metallic shading, highlights, gradients, white glows and shadows. The exact word "Hollycast" must be perfectly FLAT solid warm ivory #fff0cf, as plain printed book typography.
Keep the same bold old-style serif letter shapes, exact spelling, holly leaves/berries, horizontal arrangement and true transparent alpha. Tightly frame the actual logo with minimal transparent padding. No background or new object. Absolutely no metallic/embossed lettering.
```
