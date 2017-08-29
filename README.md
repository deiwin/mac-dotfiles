# Deiwin's Mac dotfiles

Set up instructions:
- `xcode-select --install`
- Set host name:
```
sudo scutil --set HostName deiwin-mac
sudo scutil --set LocalHostName deiwin-mac
sudo scutil --set ComputerName deiwin-mac
dscacheutil -flushcache
sudo shutdown -r now
```
- Install Homebrew
- `brew install git`
- Set up ssh keys
- `ssh-add`
- `brew install vcsh`
- `vcsh clone git@github.com:deiwin/git-dotfiles.git git`
- `vcsh clone git@github.com:deiwin/mac-dotfiles.git mac`
- `brew bundle`
- Set up MacPass
- Install and sync Firefox
  - Disable "Remember logins for sites"
- Install chrome
- Install prezto, as explained in https://github.com/deiwin/prezto#installation
- Install iTerm 3: https://www.iterm2.com/downloads.html
  - Set iTerm conf URL to: `~/.config/iterm`
- `vcsh clone git@github.com:deiwin/tmux-dotfiles.git tmux`
  - `git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm`
- `vcsh clone git@github.com:deiwin/vim-dotfiles.git vim`
  - `pip2 install neovim`
  - `pip3 install neovim`
  - Install RVM
  - `rvm install ruby-2.4.1`
  - `rvm @global do gem install neovim`
- Check Karabiner-Elements configuration
- Configure Amethyst:
  - Start on boot
  - Add to accessibility
  - Disable Layout HUD on Space Change
- Disable "Swipe between pages" gesture
- Add Estonian Input Source
- Set "Select next source in Input menu" to Shift+Command+K
- Enable "Switch to Desktop 1" 1-6 shortcuts
- Set top right hot corner for locking screen
- Set `simple_rocket` background
- Configure Keyboard "Key Repeat" and "Delay Until Repeat"
- Enable FileVaul
