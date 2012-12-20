DownloadMagnetFlexget
=====================

Drop in replacement for download plugin handling magnet link.
- only simple configuration 
- create torrent file from the magnet uri

```
tasks:
  test download magnet:
    all_series: yes
    rss: http://....espaces=true&magnets=true
    download_magnet: ~/torrent/path
```