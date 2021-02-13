import pytube

url_list = []

while True:
    url = input("Enter Your Video(s) Url(s) & (terminate by write STOP) ====>")
    if url == 'STOP':
        break
    # add url in urls arr
    url_list.append(url)

for x, video in enumerate(url_list):
    vd = pytube.YouTube(video)
    # get the video
    stream = vd.streams.get_by_itag(22)
    print(f'Downloading video {x} ...')
    # download it 
    stream.download()
    print('[FINISH]')
