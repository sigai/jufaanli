from redis import Redis, ConnectionPool

pool = ConnectionPool()
r = Redis(connection_pool=pool)

# for i in range(60010,63000):
#     r.rpush("jufaanli:start", i)

for i in range(1000,2000):
    r.rpush("jufaanli:start", i)
