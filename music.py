import os
from pathlib import Path

from mutagen.id3 import ID3
from mutagen.id3._frames import (
    APIC,
    TALB,
    TDRC,  # noqa: F401
    TDRL,  # noqa: F401
    TIT2,
    TPE1,
    TPE2,
    TPOS,  # noqa: F401
    TRCK,  # noqa: F401
    TSO2,
    TYER,
)
from mutagen.mp3 import MP3
from PIL import Image

ALB_ARTIST = "Various"
ALBUM = "Various Pop Hits"
ALB_PART = None  # Use if single disc
# ALB_PART = "1" # Use if multi disc
YEAR = "2017"


def id3_pic(cover: Path) -> APIC:
    """Creates a Cover picture from a given image for files using ID3 tags.

    Args:
        cover (Path): Path to the image used for cover. File must exist (not checked in function).

    Returns:
        APIC: Mutagen APIC type picture to be stored in ID3 tags.
    """
    imgfile = Image.open(cover)
    w, h = imgfile.size
    if w > 500 or h > 500:
        print(f"Consider resizing cover from {w}x{h} to 500x500")
        exit(1)
    img = APIC(
        encoding=3,  # 3 is for utf-8
        mime="image/jpeg",  # image/jpeg or image/png
        type=18,  # 3 is for the cover image
        desc="Cover",
        data=open(cover, "rb").read(),
    )
    return img


def main():
    music = Path(".").glob("*.mp3")

    print(f"Album: {ALBUM} - Artist: {ALB_ARTIST}")

    coverpath = None
    for m in music:
        filename = m.stem

        # If format is "1. Artist - Title" use this line
        # track, artitle = filename.split(".", 1)
        # Otherwise if format is "Artist - Title" use this line
        artitle, track = filename, None

        if " - " not in artitle:
            title = artitle.strip()
            artist = ALB_ARTIST
        else:
            artist, title = artitle.split(" - ", 1)
            # If format is "Title - Artist" use this line
            # title, artist = artitle.split(" - ", 1)
            title = title.strip()

        FEAT = [" feat. ", " ft. ", " featuring ", " feat ", " ft "]
        for f in FEAT:
            if f in artist:
                main_artist, feat = map(str.strip, artist.split(f, 1))
                artist = f"{main_artist} ft {feat}"
                break
        else:  # Only executed if the loop is NOT broken
            artist = artist.strip()
            main_artist = artist

        if track is None:
            print(f"{artist:25s} - {title}")
        else:
            print(f"{int(track):2d}. {artist:25s} - {title}")

        mp3file = MP3(m)
        if mp3file.tags is None:
            mp3file.tags = ID3()
            mp3file.save()
        id3 = ID3(m)

        id3.delall("TPE1")
        id3.add(TPE1(encoding=3, text=artist))  # Artist
        id3.delall("TIT2")
        id3.add(TIT2(encoding=3, text=title))  # Title
        id3.delall("TPE2")
        id3.add(TPE2(encoding=3, text=ALB_ARTIST))  # Album Artist
        id3.delall("TSO2")
        id3.add(TSO2(encoding=3, text=ALB_ARTIST))  # Album Artist

        id3.delall("TRCK")
        # id3.add(TRCK(encoding=3, text=str(int(track))))  # Track

        id3.delall("TALB")
        id3.add(TALB(encoding=3, text=ALBUM))  # Album

        id3.delall("TYER")
        id3.delall("TDRL")
        id3.delall("TDRC")
        id3.add(TYER(encoding=3, text=YEAR))  # Year
        id3.add(TDRL(encoding=3, text=YEAR))  # Year
        id3.add(TDRC(encoding=3, text=YEAR))  # Year

        id3.delall("TPOS")
        if ALB_PART is not None:
            id3.add(TPOS(encoding=3, text=ALB_PART))  # Disc number

        id3.delall("APIC")
        coverpath = None
        # if a jpg with the album name exists
        if Path(f"{ALBUM}.jpg").exists():
            coverpath = Path(f"{ALBUM}.jpg")
        # elif a jpg with the song name exists
        elif Path(f"{m.stem}.jpg").exists():
            coverpath = Path(f"{m.stem}.jpg")
        # otherwise use cover.jpg if it exists
        else:
            coverpath = Path("cover.jpg") if Path("cover.jpg").exists() else None

        cover = id3_pic(coverpath) if coverpath else None
        id3.add(cover)

        id3.save()

        # rename file to "Main Artist - Title.mp3" to avoid long filenames
        os.rename(m, f"{main_artist} - {title}.mp3")

    if coverpath is not None and coverpath == Path("cover.jpg"):
        os.rename(coverpath, f"{main_artist} - {title}.jpg")


if __name__ == "__main__":
    main()
