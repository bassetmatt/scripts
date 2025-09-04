# Pacman Scripts/Hooks
## Content
- `pacman.conf`: Main pacman configuration file. Main changes:
  - Parallel downloads
  - Colors
  - Multilib
  - Alternative hook dir
- `package_count`: Counts the official and AUR packages and stores the values in `/var/lib/pacman`
- `doki_command`: Runs a command that I have to run each time I update VSCode for the DokiTheme extension to work

- `hooks/`: Pacman hook files
  - `clean_cahe`: Limits the number of cached old package version to 1
  - `doki_theme`: Runs `doki_command` script when updating VSCode
  - `package_count`: Counts packages
