import sys
import glob
import os
from mutagen.easyid3 import EasyID3
import opencc
import shutil

#ID3を書き換え
def id3_jianti2fanti(mp3_path):
	tags = EasyID3(mp3_path)

	converter = opencc.OpenCC('s2t.json')

	tags['artist'] = converter.convert(tags['artist'][0])
	tags['album'] = converter.convert(tags['album'][0])
	tags['title'] = converter.convert(tags['title'][0])

	tags.save()
	
#ファイルをコピー
def fcopy_jianti2fanti(fromPath,toDir):
    basename = os.path.basename(fromPath)
    converter = opencc.OpenCC('s2t.json')
    basename_fanti = converter.convert(basename)
    toPath = toDir + "\\fanti\\" +basename_fanti
    shutil.copy(fromPath,toPath)
    
    return toPath

#main処理
dir_path = sys.argv[1]
path_mp3_files = glob.glob(dir_path + "\\*mp3") #拡張子が「*mp3」だけのファイルを返す

if len(path_mp3_files) > 0:#mp3があったら処理する
	#フォルダを作成
	os.makedirs(dir_path + "\\fanti", exist_ok=True)

	for path_mp3_i in path_mp3_files:  
	    print(path_mp3_i)
	    
	    #ファイルをコピー
	    path_fanti = fcopy_jianti2fanti(path_mp3_i,dir_path)
	    #ID3を書き換え
	    id3_jianti2fanti(path_fanti)
    
    