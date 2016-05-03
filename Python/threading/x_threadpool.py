import threadpool


def thread_use():
    pool = threadpool.ThreadPool(10)
    # single parameter
    option = [1, 2]
    requests = threadpool.makeRequests(thread_sing_parameter, option)
    [pool.putRequest(req) for req in requests]
    pool.wait()

    # multiple parameters
    option = [([1, 2, 3], None), ([4, 5, 6], None)]
    requests = threadpool.makeRequests(thread_multiple_parameter, option)
    [pool.putRequest(req) for req in requests]
    pool.wait()


def thread_sing_parameter(one):
    print one


def thread_multiple_parameter(one, two, three):
    print one, two, three


if __name__ == '__main__':
    thread_use()
