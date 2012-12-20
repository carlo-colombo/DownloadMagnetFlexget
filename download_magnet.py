from contextlib import closing
import os, re

class DownloadMagnet(object):
    def __init__(self):
        self.regex = re.compile("urn:btih:([^&]*)")

    def validator(self):
        """Return config validator"""
        from flexget import validator
        root = validator.factory('root')
        root.accept('path', allow_replacement=True)
        root.accept('boolean')
        return root

    def on_task_output(self,task):
        config = task.config['download_magnet']
        for entry in task.entries:
            if entry.get('urls'):
                urls = entry.get('urls')
            else:
                urls = [entry['url']]
            for url in [u for u in urls if u.startswith('magnet:')]:
                content = "d10:magnet-uri%s:%se" % (len(url),url)
                filename = '%s-%s.torrent' % (entry['title'].replace(' ','_'),self.regex.findall(url)[0])
                filename = os.path.join(config,filename)
                filename = os.path.expanduser(filename)
                with open(filename,'w+') as f:
                    f.write(content)

try:
    from flexget.plugin import register_plugin
    register_plugin(DownloadMagnet, 'download_magnet')
except:
    pass
