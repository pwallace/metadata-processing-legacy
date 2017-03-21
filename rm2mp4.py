import urllib2
import urlparse
import os
import commands
import sys

# this script requires mplayer and ffmpeg

argv = sys.argv
infile = open(argv[1], 'r')
# script assumes input (per argv[1]) is a plaintext 
# list of HTTP URLs separated by UNIX style newlines

for url in infile:
  path = urlparse.urlparse(url).path
  ext = os.path.splitext(path)[1].rstrip()
  rmfile = url.split('/')[-1]
  mpegfile = rmfile.replace(ext, '.mp4')
  dumpCommand = 'mplayer -dumpstream '+str(urllib2.urlopen(url).read().rstrip())
  convCommand = 'ffmpeg -i stream.dump -c:v libx264 -c:a libfaac -b:a 32k '+ mpegfile
  cleanCommand = 'rm stream.dump'
  os.system(dumpCommand)
  os.system(convCommand)
  os.system(cleanCommand)
