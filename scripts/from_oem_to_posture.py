import csv

def halfx(x1,x2):
    return 0.5*(float(x1)+float(x2))

mapping = [ 0, 1, 2,3, 4,5, 6,7,8,9,10,11,12,13,16,17,18,19,20,21,22,23,24,25,26,27,28,29,14,15]

temporal_line=0.0
fo=open("../identification/OEM_arms_60s_500Hz.posture","w")
with open("../identification/OEM_arms_60s_500Hz.csv","rb") as fi:
    
  infowriter=csv.writer(fo,delimiter=' ')
  
  inforeader=csv.reader(fi,delimiter=',')
  first=True

  for line in inforeader:
    v=line
    if not first:
      line_of_text= [temporal_line]
      for i in range(21):
        line_of_text.append(halfx(pv[mapping[i]],v[mapping[i]]))
      line_of_text.append(0.0)
      for i in range(7):
        line_of_text.append(halfx(pv[mapping[i+21]],v[mapping[i+21]]))
      line_of_text.append(0.0)

      line_of_text.append(halfx(pv[mapping[28]],v[mapping[28]]))                     
      line_of_text.append(halfx(pv[mapping[29]],v[mapping[29]]))
                          
      infowriter.writerow(line_of_text)
      temporal_line=temporal_line+0.001
    

    line_of_text=[temporal_line, \
                  v[0],v[1],v[2],v[3],v[4],v[5], \
                  v[6],v[7],v[8],v[9],v[10],v[11], \
                  v[12],v[13], \
                  v[16],v[17],v[18],v[19],v[20],v[21],v[22],'0.0', \
                  v[23],v[24],v[25],v[26],v[27],v[28],v[29],'0.0', \
                  v[14],v[15] ]
    infowriter.writerow(line_of_text)
    temporal_line=temporal_line+0.001
    pv = v
    first=False
    
fo.close()

fi.close()

