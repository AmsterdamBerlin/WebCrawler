from twitter import *
t = Twitter(auth=OAuth("2778247768-PGdpSyfNtgtKHNX4rK3G4OLPpp45M4Y39f5PfNk","U6FdgUqQSxhpSm1vrLmNswU55NOWSYRQ0wrXiOFD5ezRg",
    "sjvwdDbjzGlDKeeZC3N5HcdI0", "sNSKZXreZL7XzYiVOwEhSPOy5dc6H23uSxKH3mgG1n3JoINk9u"))
# post a twitter
#statusUpdate = t.statuses.update(status='Nice, world!')
#print(statusUpdate)

# search one user`s timeline limited to last 5 twitters
pythonStatuses = t.statuses.user_timeline(screen_name="montypython", count=1)
print(pythonStatuses)
