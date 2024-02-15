# Element-wise tensor operations 

def relu(x):
    assert len(x.shape) == 2
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] = max(x[i,j], 0)
    return x

def add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i,j] += y[i,j]
    return x

def peek(x):
    print(x[:5,:10])


def main():
    import numpy as np
    x = np.random.random((20, 100))
    y = np.random.random((20, 100))
    z = add(x, y)
    z = relu(z)
    peek(z)


if __name__ == "__main__":
    main()
