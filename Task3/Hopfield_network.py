import numpy as np
import matplotlib.pyplot as plt

class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.pattern_size = pattern_size
        self.weights = np.zeros((pattern_size, pattern_size))


    def train(self, patterns):
        patterns = [[-1 if x == 0 else x for x in pattern] for pattern in patterns] #0 -> -1
        for pattern in patterns:
            pattern = np.array(pattern).reshape(-1, 1)
            new_weights = np.dot(pattern, pattern.T)   #vynásobím pattern s transponovaným patternem
            new_weights = new_weights.astype(float)    #explicitly cast the result to float
            new_weights -= np.eye(self.pattern_size)   #odečtu jednotkovou maticí
            self.weights += new_weights


    def recover_sync(self, pattern, max_iter=20):
        pattern = [-1 if x == 0 else x for x in pattern]    #pro jistotu, kdybych zapomněl u patternů změnit 0 na -1

        for _ in range(max_iter):
            new_pattern = np.sign(np.dot(self.weights, pattern))    #vynásobení sloupce vah s patternem
            if np.array_equal(new_pattern, pattern):        #když se pattern nemeni, tak ho vrátím
                result = [0 if x == -1 else x for x in new_pattern]
                return result
            pattern = new_pattern
        
        result = [0 if x == -1 else x for x in new_pattern]
        return result


    def recover_async(self, pattern, max_iter=30, stop_iter=10): 
        pattern = [-1 if x == 0 else x for x in pattern]
        not_changed = 0
        new_pattern = pattern.copy()
        for _ in range(max_iter):
            index = np.random.randint(0, len(self.weights)) #náhodný index v rozmezí počtu vah
            activation = np.sign(np.dot(self.weights[:,index], pattern))
            pattern[index] = activation

            if np.array_equal(pattern, new_pattern):        #když se pattern nemeni, tak ho vrátím
                not_changed += 1
            else:
                new_pattern = pattern.copy()
                not_changed = 0

            if not_changed == stop_iter:
                print(f"\nPattern not changing for {stop_iter} iterations, returning current pattern, TOTAL ITERATIONS: {_}")
                pattern = [0 if x == -1 else x for x in pattern]
                return pattern

        pattern = [0 if x == -1 else x for x in pattern]
        return pattern

def pattern_to_image(pattern):
    image = np.array(pattern).reshape(int(np.sqrt(len(pattern))), -1)
    image = np.where(image == 0, 255, 0)
    return image
    
if __name__ == "__main__":
    patterns = [
        [0,1,1,1,0,
        1,0,0,0,1,
        0,0,1,1,0,
        0,1,0,0,0,
        1,1,1,1,1],
        [1,0,0,0,1,
         0,1,0,1,0,
         0,0,1,0,0,
         0,1,0,1,0,
         1,0,0,0,1]
    ]
    recover_pattern = [
        0,1,0,0,0,
        0,0,0,0,0,
        0,0,1,0,1,
        0,0,0,0,0,
        0,0,0,0,1
    ]
    """
    patterns = [
        [1, 1, 0,
         1, 1, 0,
         0, 0, 0],
        [0, 1, 1,
         0, 1, 1,
         0, 0, 0]
    ]

    #Pattern that will not work on synchronous recovery (it will not recover the pattern correctly)
    recover_pattern = [
        1, 0, 1,
        1, 0, 1,
        0, 0, 0
    ]
    """

    """
    recover_pattern = [
        1, 0, 1,
        1, 0, 0,
        0, 0, 0
    ]
    """


    hopfield_net = HopfieldNetwork(pattern_size=len(patterns[0]))
    hopfield_net.train(patterns)

    # Recover using synchronous update
    recovered_pattern_sync = hopfield_net.recover_sync(recover_pattern,max_iter=100)
    #print("Recovered pattern (synchronous):\n", recovered_pattern_sync)

    #Recover using asynchronous update
    recovered_pattern_async = hopfield_net.recover_async(recover_pattern,max_iter=100,stop_iter=20) #stop_iter => když se nemění pattern po 10 iteracích, tak ho vrátím
    #print("Recovered pattern (asynchronous):\n", recovered_pattern_async)

    # Display patterns as images
    fig, axs = plt.subplots(1, len(patterns)+3, figsize=(12, 4))
    for i, pattern in enumerate(patterns):
        image = pattern_to_image(pattern)
        axs[i].imshow(image, cmap='gray')

    image = pattern_to_image(recover_pattern)
    axs[len(patterns)].imshow(image, cmap='gray')
    image = pattern_to_image(recovered_pattern_sync)
    axs[len(patterns)+1].imshow(image, cmap='gray')
    image = pattern_to_image(recovered_pattern_async)
    axs[len(patterns)+2].imshow(image, cmap='gray')
    plt.show()



    