---
layout: post
title:  "Build my Ubuntu 20.04 (focal)"
date:   2021-3-18 18:04:17 -0500
categories: tools

---

This blog records how I install and configure my Ubuntu 20.04 ![](https://assets.ubuntu.com/v1/1be42010-cof_orange_hex.jpg){:  width="20px"}. All the codes should be run in a terminal.

**Contents**

* TOC
{:toc}
# Hardware

- Model: AlienWare R11
- CPU: Intel Core i7 10700kF
- GPU: NVIDIA 3060Ti
- Pre-installed system: Windows 10

# Dual boot 

There are already lots of blogs on how to install Ubuntu and dual boot with Windows 10. For example,

https://www.linuxtechi.com/dual-boot-ubuntu-20-04-lts-along-with-windows-10/

One more thing on AlienWare, we have to change the SATA operation from RAID to AHCI. Then reboot the Windows with safe mode. The steps are

1. Run `cmd` as administrator (not PowerShell, you would have to escape `{...}`)

2. Copy-paste this command, which will start Windows in Safe Mode the next time you reboot:

   ```bash
   bcdedit /set {current} safeboot minimal
   ```

3. Restart the computer and enter UEFI/BIOS setup.

4. Change the SATA operation mode from RAID to AHCI.

5. Save changes and exit Setup and Windows will automatically boot to Safe Mode.

6. Launch `cmd` again, as in step #1.

7. Copy-paste this command, which will start Windows in Normal Mode the next time you reboot:

   ```bash
   bcdedit /deletevalue {current} safeboot
   ```

8. Reboot and Windows will automatically start with AHCI drivers enabled.

# Softwares/packages

Use the following command if installation failed due to dependencies are not installed.

```bash
sudo apt -f install
```



- ![git](https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png){:  width="30px" style='float:left; margin-right: 5px'} [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git): a tool for version control.

  ```bash
  sudo apt install git-all
  ```

- ![Curl](https://curl.se/logo/curl-logo.svg){:  width="60px" style='float:left; margin-right: 5px'}: a tool to download or transfer files/data from or to a server using FTP, HTTP, HTTPS, SCP, SFTP, SMB and other supported protocols on Linux or Unix-like system.

  ```bash
  sudo apt install curl
  ```

- ![](https://lh4.googleusercontent.com/AZJfBIr-AXnw1DMB6yjljQCczzUv7Q0Vj9ENmDAWzdLsTv--rW3C0oejCY0gzUBmPcHsTQ=w1280){:  width="30px" style='float:left; margin-right: 5px'} Terminal multiplexer: [byobu](https://www.byobu.org/) 

  ```bash
  sudo apt-get install byobu
  ```

- bash: [zsh](https://www.zsh.org/) and [oh-my-zsh](https://ohmyz.sh/) ![](https://ohmyz.sh/img/OMZLogo_BnW.png){:  width="60px" margin-right: 0'} for plugins/personalization. Powerful yet elegant.

  ```bash
   sudo apt install zsh
   sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
  ```

  A lot of articles/configurations available online, e.g. Github.

  My terminal appearance:

  ![image-20210318185826012]({% link /assets/img/my_zsh.png %})

- Web browser: [Chrome](https://www.google.com/chrome/). I'd suggest Chrome though Firefox is default in Ubuntu. The reason is that Chrome is supported by Google and has a larger community and tools, such as gmail, google drive. 

  1. Integral with Google Drive on Ubuntu 20.04
     - Add online account to GNOME in the setting, but this way doesn't work well if we have to interact frequently, like read and write file.
     - As an alternative, try [google-drive-ocamlfuse](https://github.com/astrada/google-drive-ocamlfuse). Installation and usage on the homepage are easy to follow. 
  2. Chrome plugins
     - Ad block, etc.
     - OneTab for tab management
     - Momentum for customized new tab
     - Tampermonkey for user script

- ![](https://github.com/typora/wiki-website/blob/gh-pages/assets/img/favicon-32.png?raw=true){:  width="30px" style='float:left; margin-right: 5px'} Markdown: [Typora](typora.io). Best markdown editor I've experienced. Support $\LaTeX$ and exporting to PDF, html, tex, rST, word, etc.

  ```bash
  # or run:
  # sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
  wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
  # add Typora's repository
  sudo add-apt-repository 'deb https://typora.io/linux ./'
  sudo apt-get update
  # install typora
  sudo apt-get install typora
  ```

  If failed due to [gpg: invalid key](https://askubuntu.com/questions/1246031/gpg-invalid-key-resource-url-following-docker-official-guide), remove the file in the "/etc/apt/trusted.gpg.d/home:manuelschneid3r.gpg".

- Text editor for general use: [Sublime text 3](https://www.sublimetext.com/). 

  ```bash
  wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
  sudo apt-get install apt-transport-https
  sudo add-apt-repository "deb https://download.sublimetext.com/ apt/stable/"
  sudo apt-get update
  sudo apt install sublime-text
  ```

- IDE: [Jetbrain toolbox](https://www.jetbrains.com/toolbox-app/) and PyCharm. Best for Python and Java.

- Desktop automation utility: [AutoKey](https://github.com/autokey/autokey). 

  Install by package manager or `pip`. 

- Dictionary: [GoldenDict](http://goldendict.org/). Support select words from screen. Support search from online source like WiKi and Google.

  ```bash
  sudo apt-get install goldendict
  ```

  Off-line dictionaries: [StarDict](http://download.huzheng.org/)

- PDF reader: [Okular](https://okular.kde.org/). Support annotations like text, highlighter, hand-draw. Support multiple tabs. Support index and search.

  `Warning`: Try to install from Ubuntu software store, current stable release(20.12.3) on kde channel has some bug. 

- [Zoom](https://support.zoom.us/hc/en-us/articles/204206269-Installing-or-updating-Zoom-on-Linux)

  `Problem:` When use a high solution monitor, need to change the configuration file to match the font size. See [here](https://superuser.com/questions/1381054/how-to-enable-hidpi-support-on-zoom-us-linux-client).

# Configure GNOME

This somehow quite personal. Anyhow if you want to do so, `Tweak` is the starting point, and Chrome-gnome plugin helps you manage the extensions.

```bash
sudo apt install gnome-tweak-tool
sudo apt install chrome-gnome-shell
```

Some popular extensions

- [Dash to dock](https://extensions.gnome.org/extension/307/dash-to-dock/)
- Put windows

Also, find themes [here](https://www.pling.com/s/Gnome/browse).

# Configure my Python environment

## Intro

I decide not to use [Anaconda](https://www.anaconda.com/) in this computer, since currently I use [Python](python.org) for research purpose and stick on a fairly stable version, say 3.8 or 3.9. I don't need many different virtue environments and different versions of packages. Otherwise, it would be a good choice to manage the environments for beginners. 

## Install Python

```bash
sudo apt install python3.8
```

## Packages

Note that `pip` is not installed by default. So we have to install pip first.

```bash
sudo apt install python3-pip
```

The binary file for `pip` is `pip3`, we can set an alias if we will not use Python 2.

```
alias pip=pip3
```

The following list is from most frequent/important for me to less frequent. Most of them can be installed by

```bash
pip install package_name
```



- [`jupyter`](https://jupyter.org/) Favorite tool for developing. A true notebook.

  1. Installation (for notebook only)

     ```bash
     pip install notebook
     ```

  2. Extensions, almost necessary for me to use jupyter note book. Provide functions like notifying idle, highlighting, moving chunks, etc.

     ```bash
     pip install jupyter-contrib-nbextensions
     ```

- `Numpy`, fundamental package for scientific computing.

- `Scipy`, fundamental package for scientific computing.

- `pandas`, data frame manipulation.

- `scikit-learn`, machine learning algorithms.

- `pytorch`, deep learning package developed by Facebook.

  I installed the GPU version. For your CUDA and CUDNN version, try

  ```bash
  nvidia-smi
  ```

  Some how `nvcc` is not installed but nvidia driver and CUDA are already installed in my computer, so I didn't bother install them this time.

  For pytoch, please refer to its homepage.

- `matplotlib`, visualization.

- `seaborn`, for better visualization

- `Sphinx`, for writing documentations. For usage see my another post [here]({% post_url 2021-3-5-How-to-publish-a-Python-package %}).

- `statsmodels`, for statistical analysis.

- `thefuck`, a command line tool.

# Others

1. Font

   - Install Font manager

     ```bash
     sudo apt install font-manager
     ```

   - My favorite font: [Monaco](). Used for Overleaf as well.  Download the font by:

     ```bash
     wget http://www.gringod.com/wp-upload/software/Fonts/Monaco_Linux.ttf
     ```

2. Wallpaper

   Unfortunately, haven't find a good solution for multiple monitors.

3. Albert

   Doesn't work very well with Google drive.