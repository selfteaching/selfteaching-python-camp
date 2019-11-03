def sed(pattern, replacement,filein,fileout):
    fin = open(filein)
    fout = open(fileout,'w')
    for line in fin:
        line = line.replace(pattern,replacement)
        fout.write(line)

sed('Please','Tool','158-0.txt','copy.txt')