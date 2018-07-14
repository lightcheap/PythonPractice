#ライブラリの取り込み
import urllib.request
#URLを指定
url = "http://uta.pw/shodou/img/28/214.png"
# ダウンロードするpngをどんな名前で保存するか
savename = "test.png"

#ダウンロード
#urlretrieveは、ネット上からファイルをダウンロードし保存するのに使う
#urlretrieve(目的のURL, 保存先のファイル名)
urllib.request.urlretrieve(url, savename)
print("保存しました")