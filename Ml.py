import cm_shinx4

SongURL = 'Desired Directory Or Web Page'
transcriber = cmu_shinx4.Tanscriber(SongURL)

for line in transcriber.transcript_stream(): print line
