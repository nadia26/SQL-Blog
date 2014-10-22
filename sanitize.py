# '

def sanitize(utext):
    q= utext
    print q
    bad = ''','"\:'''
    new = [28,29,30,31,32]
    for i in xrange(len(bad)):
        q.replace(unicode(bad[i]), str(new[i]))
    print q
    return q
        
print sanitize("hello, 'Mr. Wang' :".encode('base64','strict'))
