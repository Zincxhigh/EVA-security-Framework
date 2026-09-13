# Day 1: Reading AUR for archiso

This is the documentation for my 1st day thirdspace 14 September 2026.
> I started at 1 am lol

# Steps taken

- I downloaded archiso from AUR mirror

- Extracted using this command:

```bash
tar -xzf file.pkg.tar.zst
```

- Added new profile folder, and copied releng profile to it. (README.profile.rst is helpful btw)

- Edited profiledef.sh to change our identity (EVA OS)

- edited pacman-conf to include custom repo which is not ready yet, refer to CHECKLIST.md)
  - Dont forget repo-add, the tooling branch need to be turned to db.tar.zst

That conclude the "archiso" part of documentation for today.

**Last section was 2.3**

## NOTE

The airootfs directory is used as the starting point for the root directory (/) of the live system on the image.

To add a file to the install user's home directory, place it in archlive/airootfs/root/. To add a file to all other users home directories, place it in archlive/airootfs/etc/skel/
