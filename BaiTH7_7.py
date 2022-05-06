k = open('hung.txt','r')
lc=0
for line in k:
    for k in range(0,len(line)):    
        if (line[k]=='\n'):
            lc=lc+1
print('Số dòng trong tệp văn bản là %d'%(lc))

