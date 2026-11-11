# Portions Copyright 2026 The Hollycast Authors
# SPDX-License-Identifier: GPL-2.0-or-later
"""Build the antique Play Archive reading-room package."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo
ROOT = Path(__file__).resolve().parents[1]
INK, GOLD, CREAM, RED = '351c12', 'c7a665', 'f3e4bd', '681e18'
def e(kind, rect, **fields):
    return dict(type=kind, rect=rect, **fields)
def text(rect, label, size, **fields):
    return e('text', rect, text=label, fontSize=size, color=fields.pop('color', INK), wrap=False, zIndex=2, **fields)
def meta(rect, source, size, **fields):
    return e('metadata', rect, source=source, fontSize=size, color=INK, zIndex=2, **fields)
ELEMENTS = [
 e('image',[0,0,1,1],source='assets/archive-reading-room.png',fit='stretch',zIndex=-100,bleed=True),
 e('image',[.075,.055,.20,.062],source='assets/hollycast-banner.png',fit='contain',zIndex=2),
 text([.385,.044,.31,.075],'The Play Archive',.062,color=CREAM,slant=.12),
 text([.757,.078,.15,.025],'GAME LIBRARY',.021,color=CREAM,align='center'),
 e('panel',[.05,.181,.14,.047],color='d0b477',rounding=3,zIndex=1),
 text([.055,.183,.13,.042],'COLLECTION',.027,bold=True,align='center'),
 text([.23,.17,.16,.04],'GAME INDEX',.028,bold=True),
 e('stat',[.43,.17,.055,.04],source='gameCount',fontSize=.025,color=INK,align='right',zIndex=2),
 text([.49,.174,.047,.035],'games',.021),
 e('panel',[.225,.216,.315,.0015],color='9a743c',zIndex=1),
 e('artwork',[.594,.23,.162,.35],source='case',fallback='cover',fit='contain',zIndex=2),
 meta([.775,.265,.185,.14],'title',.048,bold=True,wrap=True,text='Select a game'),
 e('panel',[.775,.425,.185,.0015],color='9a743c',zIndex=1),
 text([.78,.444,.17,.035],'RELEASE DATE',.023,color='696039'),
 meta([.78,.49,.17,.055],'releaseDate',.034,wrap=False),
 e('panel',[.585,.617,.14,.04],color='d9c698',rounding=3,zIndex=1),
 text([.59,.62,.13,.035],'OVERVIEW',.026,bold=True,align='center'),
 e('panel',[.73,.642,.23,.0015],color='9a743c',zIndex=1),
 e('details',[.60,.68,.355,.13],fields=['description'],autoFit=True,fontSize=.029,color=INK,zIndex=2),
 e('panel',[.59,.825,.37,.0015],color='9a743c',zIndex=1),
 e('panel',[.662,.868,.232,.077],color=GOLD,rounding=8,zIndex=2),
 e('button',[.665,.872,.226,.069],action='activate',text='▶  PLAY',fontSize=.037,bold=True,color=CREAM,background=RED,borderColor=GOLD,rounding=.10,zIndex=5),
]
THEME = dict(formatVersion=1,id='play-archive',name='Play Archive',author='The Hollycast Authors',
 description='An antique reading room with a live game index, parchment pages and scraped case artwork. Requires the new Play Archive-enabled Hollycast development build.',baseTheme=0,
 fonts=dict(body='assets/Alegreya-Regular.ttf',bold='assets/Alegreya-Bold.ttf'),
 colors=dict(Text=CREAM,TextDisabled='b7a684',WindowBg='26160e',ChildBg='00000000',PopupBg='312519',Border=GOLD,
 FrameBg='493b26',FrameBgHovered='675237',FrameBgActive=RED,Button='443b2700',ButtonHovered='79502daa',ButtonActive=RED,
 Header=RED,HeaderHovered='813427',HeaderActive=RED,Separator='b49861',ScrollbarBg='b4976030',ScrollbarGrab='8d673c',
 ScrollbarGrabHovered='a87b49',ScrollbarGrabActive=RED,CheckMark=GOLD,NavCursor=GOLD,TextSelectedBg='a98a4c88'),
 layouts=[dict(id='archive-reading-room',name='Reading Room',mode='list',browser=[.225,.225,.315,.72],navigation=[.039,.255,.16,.40],
 showArtwork=True,rowHeight=.085,fontSize=.029,list=dict(selectOnHover=False,releaseYear=True),spacing=8,activation='doubleClick',
 toolbar='hidden',background='26160e',textColor=INK,selectedTextColor=CREAM,selectorColor='681e18ed',selectorStyle='fill',
 selectorBorderColor=GOLD,separatorColor='b79b6c88',rounding=3,artworkSource='cover',requiredMedia=['cover','case'],
 showItemActions=False,showFavouriteMarker=False,hoverDetails=False,showInfoTooltip=False,elements=ELEMENTS)])
def main():
    (ROOT/'theme.json').write_text(json.dumps(THEME,indent=2)+'\n',encoding='utf-8',newline='\n')
    files=sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    destination=ROOT.parent/'play-archive-1.0.0.zip'
    with ZipFile(destination,'w',compression=ZIP_DEFLATED,compresslevel=9) as archive:
        for path in files:
            entry=ZipInfo(path.relative_to(ROOT).as_posix(),(2026,11,10,0,0,0))
            entry.compress_type=ZIP_DEFLATED
            entry.create_system=3
            entry.external_attr=0o100644<<16
            archive.writestr(entry,path.read_bytes(),compresslevel=9)
    print(f'Created {destination} ({destination.stat().st_size:,} bytes; {len(files)} files)')
if __name__=='__main__':
    main()
