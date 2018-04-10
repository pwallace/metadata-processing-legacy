### Fast image cataloger - depends on TerminalImageViewer (tiv) and Pillow (PIL)

from PIL import Image
from pprint import pprint
#from collections import defaultdict
import sys
import os
import glob
import json
import subprocess
#import csv
#import webbrowser

### Basic Functions

def query_yes_no(question, default):
	valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
	prompt = " [Y/n] "
	while True:
		sys.stdout.write(question + prompt)
		choice = raw_input().lower()
		if default == 'yes' and choice == '':
		  return valid[default]
		if choice in valid:
		  return valid[choice]

def query_empty_field():
  emptyfield = query_yes_no("Leave this field empty?", 'yes')
  return emptyfield
  
def pressAnyKey():
	raw_input("Press Enter to continue...")

def clearScreen():
  print(chr(27) + "[2J")

### Display image file in terminal with tiv


#Use this function for console display (depends on TerminalImageViewer)
#
#def displayImg(imgfile):
#	os.system('tiv -256 ' + imgfile)

def displayImg(imgfile):
  p = subprocess.Popen(["feh", "-g=100x50", imgfile])
  return p

#def displayImg(imgfile):
#  webbrowser.open(imgfile)

### Listing and comparison to start from last known

def getFileList(mypath):
	filelist = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
	return filelist

def jsonFilter(filelist):
	jsonlist = []
	for filename in filelist:
		if filename.endswith(".json"):
			jsonlist.append(filename)
	return jsonlist

def imgFilter(filelist):
	imglist = []
	imgtypes = ['.jpg', '.JPG', '.jpeg', '.JP2', '.jp2', '.tif', '.tiff']
	for filename in filelist:
		for imgtype in imgtypes:
			if filename.endswith(imgtype):
				imglist.append(filename)
	return imglist

def extensionStripper(filelist):
  thislist = []
  for filename in filelist:
    thislist.append(os.path.splitext(filename)[0])
  return thislist

def todoLister(imglist, jsonlist):
  todolist = []
  if jsonlist == []:
    return imglist
  rawtodolist = list(set(extensionStripper(imglist)) - set(extensionStripper(jsonlist)))
  for image in imglist:
    for todoitem in rawtodolist:
      if image.startswith(todoitem):
        todolist.append(image)
  return todolist

def getTodoList(mypath):
	filelist = getFileList(mypath)
	rawjsonlist = jsonFilter(filelist)
	rawimglist = imgFilter(filelist)
	todolist = todoLister(rawimglist, rawjsonlist)
	return todolist

### Read default.json

def readCollectionDefaults(imgfile):
  with open('defaults.json') as default_data:
    defaults = json.load(default_data)
  defaults['filename'] = str(imgfile)
  tempid = str(defaults['id_prefix']) + "_" + os.path.splitext(imgfile)[0]
  defaults['identifier'] = tempid
  return defaults

### Metadata input functions

def getValue(field, checkinput=False):
  fieldvalue = raw_input(field + ": ")
  return fieldvalue
  
def getValueCheck(fieldvalue, inputok=False):
  if fieldvalue == '':
    inputok = query_empty_field()
  if fieldvalue != '':
    fieldquery = "Is this correct?"
    inputok = query_yes_no(fieldquery, 'yes')
  return inputok
  
### Record reviewing
  
def reviewRecord(metadata):
  imgfile = metadata['filename']
  print "\n*****************"
  print "* Record Review *"
  print "*****************\n"
  for key in metadata:
    if key == "subject":
      print key + " : "
      for item in metadata[key]:
        print "  " + item
    else:
      print key + " : " + metadata[key]
  reviewquery = "Is this record correct?"
  reviewresponse = query_yes_no(reviewquery, 'yes')
  return reviewresponse

### Metadata entry

def metadataPopulator(imgfile):
  recordData = readCollectionDefaults(imgfile)
  for key in recordData:
    inputok = False
    
    if key == "subject":
      subjectList = list(recordData['subject'])
      recordData['subject'] = addSubjects(subjectList)
      
#    if key == "date" and inputok is False:
#      dateok = False
#      while dateok is False:
#        newvalue = getValue(key)
#        print newvalue
#        inputok = getValueCheck(newvalue)
#        print newvalue + " is not a valid date! Please use YYYY, YYYY-MM, or YYYY-MM-DD format."

    while recordData[key] == "" and inputok is False:
      while inputok == False:
        newvalue = getValue(key)
        inputok = getValueCheck(newvalue)
        recordData[key] = newvalue
  return recordData

# Add subjects

def addSubjects(subjectList):
  moresubjects = False
  while moresubjects is False:
    inputok = False
    while inputok is False:
      newsubject = getValue('subject')
      inputok = getValueCheck(newsubject)
    subjectList.append(newsubject)
    moresubjects = query_yes_no("Done adding subjects?", 'yes')
  return subjectList

### Creating a new record

def createRecord(opt1, reviewed=False):
	while reviewed is False:
	  p = displayImg(opt1)
	  metadata = metadataPopulator(opt1)
	  reviewed = reviewRecord(metadata)
	  p.kill()
	return metadata

### Spitting out a record

def createJSON(recordData):
  baseName = str(recordData['filename']).split(".")
  jsonFilename = baseName[0] + '.json'
  with open(jsonFilename, 'w') as f:
    json.dump(recordData, f)


### Run that shit

mypath = sys.argv[1]
todolist = getTodoList(mypath)
for image_file in todolist:
  clearScreen()
  recordData = createRecord(image_file)
  createJSON(recordData)
  pressAnyKey()
