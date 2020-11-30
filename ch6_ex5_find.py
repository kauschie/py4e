inputstr = 'X-DSPAM-Confidence:0.8475'
colonpos = inputstr.find(':')
extstr = inputstr[colonpos+1:]
extnum = float(extstr)
print(extnum)
