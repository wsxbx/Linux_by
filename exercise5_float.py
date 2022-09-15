str = 'X-DSPAM-Confidence:0.8475'
moral_str = str.split(':')[1]
result = float(moral_str)
print(result)