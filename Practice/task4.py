music = ['metal','rock','pop','folk']
print(music)
print(music[2])
music[0]='nu metal'
print(music)
music.append('jazz')
print(music)
music.extend(['grunge',666])
print(music)
music.remove(666)
print(music)
print(666 in music)
print('nu metal'in music)
print(666 not in music)
print(music[0:3])


