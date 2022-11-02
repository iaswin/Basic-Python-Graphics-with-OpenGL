def check():
    def glow():
        ts="glow1"
    def glow2():
        nonlocal ts
        ts="glow2"
    def glow3():
        global ts
        ts="glow3"
    ts="glowiv"
    glow()
    print("hello"+ts)
    glow2()
    print("hello"+ts)
check()
print("hello"+ts)