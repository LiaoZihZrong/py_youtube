from pytube import YouTube

def onProgress(stream, chunk, remaining):
    try:
        total = stream.filesize
        percent = (total - remaining) / total * 100
        show_num=[10,20,30,40,50,60,70,80,90,100]
        global sh_i
        #print(sh_i)
        if (percent > show_num[sh_i]) and (sh_i <= 8):
            print("下載中…{:05.2f}%".format(percent))
            sh_i=sh_i+1
        else:
            pass
            #print("percent: ",percent)
    except :
        #IndexError as e
        print("download something error-404")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(3):
        print("<程式將執行三遍，第",i+1,"遍>")
        sh_i = 0
        yt_path=input("input URL:")
        #yt=YouTube("https://youtu.be/sOome7baXD0", on_progress_callback=onProgress)
        try:
            yt = YouTube(yt_path, on_progress_callback=onProgress)
            print("開始下載")
            yt.streams.first().download()
            print("完成")
        except:
            print("URL something error--404")